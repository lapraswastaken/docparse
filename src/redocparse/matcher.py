
from __future__ import annotations

import dataclasses as dc
import inspect
import os
import re
import traceback
import typing as t

@dc.dataclass
class Log:
    index: int = 0
    messages: list[str | Log] = dc.field(default_factory=list)
    
    def inner(self, cls: type[t.Self] | None=None):
        new_scope = cls() if cls else self.__class__()
        self.messages.append(new_scope)
        return new_scope

    def write(self, msg: str):
        self.messages += msg.split("\n")
        return self

    def as_str(self, indent=0):
        string = ""
        for line in self.messages:
            if isinstance(line, str):
                string += "  " * (indent) + line + "\n"
            else:
                string += line.as_str(indent+1)
        return string

    def depth(self):
        depth = 1
        for msg in self.messages:
            if not isinstance(msg, str):
                depth += msg.depth()
        return depth
    
    def pop(self):
        last = self.messages.pop()
        if isinstance(last, str): raise Exception()
        return last

@dc.dataclass
class Matcher:
    r""" Allows for recursive pattern matching.
    
        Its main function is the :meth:`process` method, which uses its nested :attr:`group_matchers` and :attr:`inner_matchers` to process parts of matched text.
    
        Instances of this class can be used as decorators around functions - this will set the decorated function as that instance's :attr:`on_match` callback.
        
        Also Provides functionality for processing a handful of specified files. See :meth:`process_files` for more details. """


    match_pattern_str: dc.InitVar[str]
    r""" The string pattern that will be used to match text for this :class:`Matcher` to :meth:`process`. Upon instantiation, the pattern is compiled using :func:`re.compile` and set to :attr:`match_pattern`.
    
        The default pattern matches all characters. """
    
    use_name: dc.InitVar[str | None] = None
    r""" An optional name for this :class:`Matcher`. This will be displayed when logging whenever :attr:`match_pattern` matches. 
    
        This value goes directly into :attr:`name`. If not specified, :attr:`name` will be the ``.__name__`` of the :attr:`on_match` function. """
    
    name: str = dc.field(init=False)
    r""" The name for this :class:`Matcher`. """

    on_match: t.Callable[..., str] = dc.field(init=False)
    r""" Returns a processed string.
        
        The positional arguments to this callback function must match the number of unnamed groups in the instance's :attr:`match_pattern`, and the keyword arguments must match the named groups in that pattern. """

    inner_matchers: list[Matcher] = dc.field(init=False, default_factory=list)
    r""" Each item :meth:`process`\ es the entirety of the :attr:`match_pattern`'s match.
    
        This list should be populated using the :meth:`matcher` decorator method. """
    
    group_matchers: dict[str, MatcherList] = dc.field(init=False, default_factory=dict)
    r""" Each :class:`MatcherList` takes a single named group in the :attr:`match_pattern`, :meth:`process`\ es it, and returns the processed text to be given to the :attr:`on_match` callback as a keyword argument.
    
        This dict should be populated using the :meth:`group` decorator method. """

    match_pattern: re.Pattern[str] = dc.field(init=False)
    r""" The compiled version of :attr:`match_pattern_str`. """

    def __post_init__(self, take_pat: str, use_name: str | None):
        self.match_pattern = re.compile(take_pat)
        self.name = use_name if use_name else "no name"
    
    def __call__(self, callback: t.Callable[..., str]):
        self.on_match = callback
        if self.name == "no name":
            self.name = callback.__name__
        return self

    def group(self, groupname: str, use_name: str | None=None):
        r""" Returns a :class:`MatcherList` that has been added to the instance's :attr:`group_matchers` under the given ``groupname``.
        
            A :class:`MatcherList` should exist for each named group in the :attr:`match_pattern`. Unnamed groups will be passed to the :attr:`on_match` callback, in order and unchanged . """

        self.group_matchers[groupname] = MatcherList(use_name and use_name or groupname)
        return self.group_matchers[groupname]
    
    def matcher(self, match_pattern_str: str=r"[\w\W]*", use_name: str | None=None):
        r""" Returns a new :class:`Matcher` that has been added to the instance's list of :attr:`inner_matchers`. """

        self.inner_matchers.append(Matcher(match_pattern_str, use_name))
        return self.inner_matchers[-1]
    
    def add(self, matchers: list[Matcher]):
        r""" Adds a list of :class:`Matcher`\ s to :attr:`.inner_matchers`."""

        self.inner_matchers += matchers

    def process(self, text: str, *, _indices: list[tuple[int, str, str]] | None=None, _log: Log | None=None, _current_index: int=0) -> str:
        r""" Returns text that has been processed by the :attr:`on_match` callback and each matching one within.
        
            The input string is matched against the :attr:`match_pattern` using :meth:`~re.Pattern.finditer`, and each resulting :class:`re.Match`'s :meth:`~re.Match.groups` is :meth:`process`\ ed by one of the :attr:`group_matchers` to correct the :meth:`~re.Match.groups` for the :attr:`on_match` callback.
            
            The processed text is collected, then appended to by calling all of the :attr:`inner_matchers`' :meth:`process` methods on the entirety of the :class:`re.Match`'s match :meth:`~re.Match.group`. """

        processed = ""
        matches = list(self.match_pattern.finditer(text))
        if _log and len(matches):
            _log.write(f"\n{self.name}:")

        yaml_single_line: t.Callable[[str], str] = (
            lambda s: "'" + s
                .replace("\n", r"\n")
                .replace("'", r",")
                [:400] + "'"
        )

        for re_match in matches:
            list_matches_log = _log and _log.inner()
            match_detail_log = None
            if _log and list_matches_log:
                if _indices:
                    current_file, content = [
                        (name, content)
                        for index, name, content in _indices
                        if index <= _current_index
                    ].pop()
                    _current_index += re_match.start()
                    line = content[:_current_index].count("\n") + 1
                    match_detail_log = (list_matches_log
                        .write(f"- match in: {current_file.split(os.path.sep)[-1]}").inner()
                            .write(f"line: {line}")
                            .write(f"link: file:{os.path.sep*2}{os.path.abspath(current_file)}#{line}"))
                match_detail_log = match_detail_log or list_matches_log.inner()
                (match_detail_log
                    .write(f"re:").inner()
                        .write(f"r\"{re_match.re.pattern}\""))
                (match_detail_log
                    .write(f"full match:").inner()
                        .write(yaml_single_line(re_match.group())))
            inner_processed = self._process_match(re_match, _indices, list_matches_log, _current_index)
            processed += inner_processed
            if list_matches_log:
                match_detail_log = match_detail_log or list_matches_log.inner()
                (match_detail_log
                    .write(f"processed:").inner()
                        .write(yaml_single_line(inner_processed)))
        
        return processed
    
    def _process_match(self, re_match: re.Match[str], indices: list[tuple[int, str, str]] | None, log: Log | None, current_index: int):
        named_groups = re_match.groupdict()
        unnamed_groups = [
            group
            for group in re_match.groups()
            if not group in named_groups.values()
        ]
        kwarg_groups = {
            groupname: self.group_matchers[groupname].process(group,
                _indices=indices,
                _log=log and log.inner(),
                _current_index=current_index)
            for groupname, group in named_groups.items()
        }

        processed = self.on_match(*unnamed_groups, **kwarg_groups)

        for inner_matcher in self.inner_matchers:
            got = inner_matcher.process(re_match.group(),
                _indices=indices,
                _log=log and log.inner(),
                _current_index=current_index)
            processed += got

        return processed
    
    def process_files(self, files: ta_DocsFiles, outfile: str, *, logsfolder: str | None=None):
        r""" :meth:`process`\ es the specified files all at once by appending them all together. The structure of the ``docsfiles`` dict is outlined in :func:`read_files`.
            
            Writes the processed text to ``outfile`` and the :class:`MatchLog`\ s to the ``logfile``. """

        all_content, indices = get_contents(read_files(files), "")
        log = Log() if logsfolder is not None else None
        try:
            processed = self.process(all_content, _indices=indices, _log=log)
            with open(outfile, "w") as f:
                f.write(processed)
        except Exception as e:
            traceback.print_exception(e)
        finally:
            if logsfolder and log:
                new_logfile(logsfolder, log.as_str())

def substitution_matchers(substitutions: dict[str, str | t.Callable[..., str]]):
    r""" Returns a collection of simple substitution :class:`Matcher`\ s.
    
        Each pair in ``substitutions`` should be:
        * A regex pattern string, mapped to 
        * * Either a replacement value or
        * * A lambda :attr:`on_match` callback.
        
        Replacement strings will have any instances of an escaped number (e.g. ``r"\1"``) set to the value of the matched group at that index, similar to :func:`re.sub`. See :func:`re.sub`'s documentation for a further explanation. """
    
    matchers: list[Matcher] = []
    for regex, replacer in substitutions.items():
        substitutor: t.Callable[..., str] = substitution_cb(replacer) if isinstance(replacer, str) else replacer
        matchers.append(Matcher(regex, use_name=f'<r"{regex}"->r"{replacer}">')(substitutor))
    return matchers

def substitution_cb(replacer: str):
    def sub(*groups: str):
        return re.sub(r"\\(\d+)", lambda m: groups[int(m.group(1))-1], replacer)
    return sub

@dc.dataclass
class MatcherList:
    name: str
    """ A name used for debugging. Usually specified already by :meth:`Matcher.group` as the ``groupname`` for the group or the ``use_name`` argument if it exists. """
    matchers: list[Matcher] = dc.field(default_factory=list)
    """ The list of matchers to be called in succession using :meth:`.process()`. """

    def matcher(self, match_pattern_str: str, use_name: str | None=None):
        """ Creates a new :class:`Matcher`, adds it to :attr:`.matchers`, and returns it. """

        self.matchers.append(Matcher(match_pattern_str, use_name))
        return self.matchers[-1]
    
    def process(self, text: str, *,
        _indices: list[tuple[int, str, str]] | None=None,
        _log: Log | None=None,
        _current_index: int=0
    ) -> str:
        """ Calls the :meth:`~Matcher.process` method of all items in :attr:`.matchers`. """

        processed = ""
        for matcher in self.matchers:
            processed += matcher.process(text,
                _indices=_indices,
                _log=_log,
                _current_index=_current_index)
        return processed
    
    def add(self, matchers: list[Matcher]):
        r""" Adds a list of :class:`Matcher`\ s to :attr:`.matchers`. """

        self.matchers += matchers
        return self

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

    indices: list[tuple[int, str, str]] = []
    all_contents = ""
    total_chars = 0
    for filename, content in file_contents.items():
        indices.append((total_chars, filename, content))
        with_sep = content + file_separator
        all_contents += with_sep
        total_chars += len(with_sep)
    return all_contents, indices

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
    
    logfile = os.path.join(logfolder, "log.yaml")
    if os.path.exists(logfile):
        logfiles = os.listdir(oldlogs_folder)
        lognumber = int(logfiles[-1][:-5]) if logfiles else 0
        with open(os.path.join(logfolder, str(lognumber + 1) + ".yaml"), "w") as f:
            with open(logfile, "r") as lf:
                f.write(lf.read())
    
    with open(logfile, "w") as f:
        f.write(content)
