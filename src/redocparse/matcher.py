
from __future__ import annotations

import dataclasses as dc
import inspect
import os
import re
import traceback
import typing as t

@dc.dataclass
class Matcher:
    r""" Allows for recursive pattern matching.
    
        Its main function is the :meth:`process` method, which uses its nested :attr:`group_matchers` and :attr:`inner_matchers` to process parts of matched text.
    
        Instances of this class can be used as decorators around functions - this will set the decorated function as that instance's :attr:`on_match` callback.
        
        Provides functionality for processing a handful of specified files. See :meth:`process_files` for more information. """


    match_pattern_str: dc.InitVar[str] = r"[\w\W]*"
    r""" The string pattern that will be used to match text for this :class:`Matcher` to :meth:`process`. Upon instantiation, the pattern is compiled using :func:`re.compile`.
    
        The default pattern matches all characters. """

    on_match: t.Callable[..., str] = lambda: ""
    r""" Returns a processed string.
        
        The positional arguments to this callback function must match the number of unnamed groups in the instance's :attr:`match_pattern`, and the keyword arguments must match the named groups in that pattern. """

    inner_matchers: list[Matcher] = dc.field(default_factory=list)
    r""" Each item :meth:`process`\ es the entirety of the :attr:`match_pattern`'s match.
    
        This list should be populated using the :meth:`matcher` decorator method. """
    
    group_matchers: dict[str, Matcher] = dc.field(default_factory=dict)
    r""" Each item takes a single named group in the :attr:`match_pattern`, :meth:`process`\ es it, and returns the processed text to be given to the :attr:`on_match` callback as a keyword argument.
    
        This dict should be populated using the :meth:`group` decorator method. """

    match_pattern: re.Pattern[str] = dc.field(init=False)
    r""" The compiled version of :attr:`match_pattern_str`. """

    def __post_init__(self, take_pat: str):
        self.match_pattern = re.compile(take_pat)
    
    def __call__(self, callback: t.Callable[..., str]):
        self.on_match = callback
        return self
    
    def process(self, text: str, *, match_logs: list[MatchLog] | None=None, stack: tuple[str, ...]=tuple()) -> str:
        r""" Returns processed text based on an input string.
        
            The input string is matched against the :attr:`match_pattern` using :meth:`~re.Pattern.finditer`, and each resulting :class:`re.Match`'s :meth:`~re.Match.groups` is :meth:`process`\ ed by one of the :attr:`group_matchers` to correct the :meth:`~re.Match.groups` for the :attr:`on_match` callback.
            
            The processed text is collected, then appended to by calling all of the :attr:`inner_matchers`' :meth:`process` methods on the entirety of the :class:`re.Match`'s match :meth:`~re.Match.group`.
            
            ``match_logs`` and ``stack`` are arguments intended for internal use.
            
            * ``match_logs`` is a list that collects each :class:`re.Match`'s info if it exists. This function alters the contents of that list.

            * ``stack`` is a tuple of strings denoting which :class:`Matcher` is processing the text. """

        stack += (self.on_match.__name__,)
        processed = ""
        for re_match in self.match_pattern.finditer(text):
            # process groups
            named_groups = re_match.groupdict()
            unnamed_groups = [group for group in re_match.groups() if not group in named_groups.values()]
            processed_groups = {}
            for groupname, group in named_groups.items():
                processed_groups[groupname] = self.group_matchers[groupname].process(group, match_logs=match_logs, stack=stack)
            full_match = re_match.group()
            if "full_match" in inspect.signature(self.on_match).parameters:
                processed_groups["full_match"] = full_match
            
            onmatch_processed = self.on_match(*unnamed_groups, **processed_groups)

            if match_logs is not None:
                match_logs.append(MatchLog(stack, re_match.re.pattern, full_match, re_match.start(), onmatch_processed))
            processed += onmatch_processed

            for inner_matcher in self.inner_matchers:
                got = inner_matcher.process(full_match, match_logs=match_logs, stack=stack)
                processed += got
        
        return processed

    def group(self, groupname: str):
        r""" Returns a :class:`Matcher` that has been added to the instance's :attr:`group_matchers` under the given ``groupname``.
        
            A group matcher should exist for each named group in the :attr:`match_pattern`. Unnamed groups will be passed in order and unchanged to the :attr:`on_match` callback. """

        self.group_matchers[groupname] = Matcher()
        return self.group_matchers[groupname]
    
    def matcher(self, match_pattern_str: str=r"[\w\W]*"):
        r""" Returns a new :class:`Matcher` that has been added to the instance's list of :attr:`inner_matchers`. """

        self.inner_matchers.append(Matcher(match_pattern_str))
        return self.inner_matchers[-1]
    
    def quick_steps(self, steps: dict[str, str | t.Callable[[re.Match[str]], str]]):
        r""" Adds a collection of simple substitution :class:`Matcher`\ s to the list of :attr:`inner_matchers`.
        
            Each pair in ``steps`` should be a regex pattern string mapped to either a replacement value or a lambda :attr:`on_match` callback. """

        for regex, replacer in steps.items():
            substitutor = (lambda full_match: re.sub(regex, replacer, full_match))
            substitutor.__name__ = f'<"{regex}"->"{replacer}">'
            self.inner_matchers.append(Matcher(on_match=substitutor))
    
    def process_files(self, files: ta_DocsFiles, outfile: str, logsfolder: str):
        r""" :meth:`process`\ es the specified files all at once by appending them all together. The structure of the ``docsfiles`` dict is outlined in :func:`read_files`.
            
            Writes the processed text to ``outfile`` and the :class:`MatchLog`\ s to the ``logfile``. """

        all_content, indices = get_contents(read_files(files), "\n\n")
        logs: list[MatchLog] = []
        try:
            processed = self.process(all_content, match_logs=logs)
            with open(outfile, "w") as f:
                f.write(processed)
        except Exception as e:
            traceback.print_exception(e)
        logcontents = process_logs(logs, indices)
        new_logfile(logsfolder, logcontents)

@dc.dataclass
class FileIndex:
    index: int
    filename: str
    content: str

@dc.dataclass
class MatchLog:
    r""" Stores information about a pattern match that happened inside of a :class:`Matcher`. """

    stack: tuple[str, ...]
    r""" The stack of :class:`Matcher`s called to reach this match.
    
        The string items should be each :class:`Matcher`'s :attr:`on_match` callback function ``.__name__`` or, if the callback is a lambda, a representation of that lambda. """

    pat: str
    """ The regular expression used on the :attr:`content`. """

    content: str
    """ The text that was matched against. """
    
    start: int
    """ The index of the first letter in the match in :attr:`content`. """

    replacement: str
    """ The processed text returned by the :attr:`on_match` callback function. """

def single_line(s: str):
    return s.replace("\n", r"\n")

def process_logs(logs: list[MatchLog], indices: list[FileIndex], abbr: int=300):
    logcontents = ""
    start = 0
    current_file = indices[0]
    for log in logs:
        start += log.start
        if start >= indices[0].index:
            current_file = indices.pop(0)
        line = current_file.content[:start].count("\n")
        logcontents += (
f"""
### {'.'.join(log.stack)} matched
**{current_file.filename.split(os.path.sep)[-1]}**, line {line}, [link](<file:{os.path.sep * 2}{os.path.abspath(current_file.filename)}#{line}>)
re:
* {log.pat}
full match:
> {single_line(log.content)[:abbr]}
returned:
> {single_line(log.replacement)[:abbr]}

"""
        )
    return logcontents

ta_DocsFiles = dict[str, "str | list[str] | ta_DocsFiles"]

def read_files(docsfiles: ta_DocsFiles, *, outer_root: str="") -> dict[str, str]:
    """ Flattens the ``docsfiles`` dict (which potentially has nested dicts denoting inner folder paths), reads the specified files, and returns a dict with each filepath mapped to that file's content.
    
        The ``docsfiles`` dict is a map of filepaths. Each key denotes a folder name. A folder name can be mapped to a string, a list, or another ``docsfiles`` dict.
        
        * When the mapped value is a string,
        
        * * if that string is "*", all of the files in the folder are read.
        
        * * If that string is anything else, it reads the string as a specific file in the folder.
        
        * When the mapped value is a list, each of the list's values is a specific file within that folder.
        
        * When the mapped value is a dict, recurse. 

        The ``outer_root`` argument is meant only for recursion - it is prepended to each path when reading files. """

    file_contents: dict[str, str] = {}
    for inner_root, files in docsfiles.items():
        root = os.path.join(outer_root, inner_root)
        if isinstance(files, str):
            if files == "*":
                for file in os.listdir(root):
                    path = os.path.join(root, file)
                    with open(path, "r") as f:
                        file_contents[path] = f.read()
            else:
                path = os.path.join(root, files)
                with open(path, "r") as f:
                    file_contents[path] = f.read()
        elif isinstance(files, list):
            for file in files:
                path = os.path.join(root, file)
                with open(path, "r") as f:
                    file_contents[path] = f.read()
        else:
            file_contents |= read_files(files, outer_root=root)
    return file_contents
    
def get_contents(file_contents: dict[str, str], file_separator: str):
    r""" Returns two values:
    
        * A single string of all contents in ``file_contents``'s values joined by ``file_separator``, and
        
        * A list of pairs:

        * * The first item is the index of the starting character in the string of all contents for a file.

        * * The second item is that file's filepath.
        
        The list of pairs is meant to be used by :class:`MatchLog`\ s to determine in which file a pattern match was found. """

    fileindices: list[FileIndex] = []
    all_contents = ""
    total_chars = 0
    for filename, content in file_contents.items():
        fileindices.append(FileIndex(total_chars, filename, content))
        with_sep = content + file_separator
        all_contents += with_sep
        total_chars += len(with_sep)
    return all_contents, fileindices

def new_logfile(logfolder: str, content: str):
    r""" Creates a new file in the folder at the specified path and writes the given contents to that file. If the specified path isn't a folder, creates a folder at that path.
    
        The created file will have a number as its filename. """

    if not os.path.isdir(logfolder):
        if os.path.exists(logfolder):
            raise Exception(f"Tried to use '{logfolder}' as a folder for storing logfiles, but it already exists and isn't a directory. ")
        os.mkdir(logfolder)
    oldlogs_folder = os.path.join(logfolder, "old")
    if not os.path.exists(oldlogs_folder):
        os.mkdir(oldlogs_folder)
    
    logfile = os.path.join(logfolder, "log.md")
    if os.path.exists(logfile):

        logfiles = os.listdir(oldlogs_folder)
        lognumber = int(logfiles[-1][:-3]) if logfiles else 0
        with open(os.path.join(logfolder, str(lognumber + 1) + ".md"), "w") as f:
            with open(logfile, "r") as lf:
                f.write(lf.read())
    with open(logfile, "w") as f:
        f.write(content)
