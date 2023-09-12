
import os
import sys

import inflect
p = inflect.engine()

sys.path.append(os.path.abspath("./src"))

import redocparse.matcher as m

def namify(s: str):
    return "".join([w[0].upper() + w[1:] for w in s.split()])

def make_singular(s: str):
    singular = p.singular_noun(s)
    if isinstance(singular, str): return singular
    return s

@m.Matcher(r"[\w\W]+")
def root():
    return f"""
from __future__ import annotations

import dataclasses as dc
import typing as t

from dubious.discord.disc import Snowflake

"""

@root.matcher(r"###### (.+?) Structure[\w\W]+?\s+\|\n\n")
def disc_class(name: str):
    return f"@dc.dataclass\nclass {namify(name)}:\n"

noneable = " | None"

field_pat = r"\| ([a-zA-Z_]+?\??)[ \\\*]+\| (?P<ftype>.+?) +\| (?P<desc>.+?) +\|"
@disc_class.matcher(field_pat)
def format_field(name: str, *, ftype: str, desc: str):
    if name == "Field": return ""
    elif name == "global": name = "_global"

    if "#" in ftype:
        ftype, extra_desc = ftype.split("#")
        desc += extra_desc

    if name.endswith("?"):
        # the steps for ftype might have already added " | None"
        if not ftype.endswith(" | None"):
            ftype += " | None"
        ftype += " = dc.field(kw_only=True, default=None)"
        name = name[:-1]
    
    return f'    {name}: {ftype}\n    """ {desc} """\n\n'

format_ftype = format_field.group("ftype").add(m.substitution_matchers({
    # Raw types
    r"string": "str",
    r"(?:integer)|(?:number)": "int",
    r"double": "float",
    r"boolean": "bool",
    r"snowflake": "Snowflake",
    r"ISO8601 timestamp": "str",
    r"file contents": "Any",

    # Noneable fields (prepended or appended with "?")
    r"^\?(.+)": r"\1 | None",
    r"(.+)\?$": r"\1 | None",

    # Internal type references
    r"\[(.+?)\].*":
        lambda name:
            namify(name),
    
    # Collections
    r".*?(?:[a|A]rray|[l|L]ist) of (.+)":
        lambda itype: 
            f"list[{make_singular(itype)}]",
    r".*?[m|M]ap of (.+) to (.+)":
        lambda ktype, itype:
            f"dict[{make_singular(ktype)}, {make_singular(itype)}]",

    # Fixing audit log things
    r"^mixed(.*)": r"t.Any# \1",
}))

format_desc = format_field.group("desc").add(m.substitution_matchers({
    r"\[(.+?)\]\(.+\)": r"`\1`"
}))


if __name__ == "__main__":
    root.process_files({
        "src/discord/discord-api-docs": {
            "docs": {
                "interactions": "*",
                "resources": "*",
                "topics": [
                    "OAuth2.md",
                    "Permissions.md",
                    "Teams.md",
                ],
            },
        },
    }, "src/discord/api.py", logsfolder="src/discord/logs")