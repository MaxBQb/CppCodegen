import re

from . import *


def interface():
    lines = get_code_lines()
    classname = next(re.finditer(r"class\s+(\w+)\b", lines[0])).group(1)
    pubsec = "public:"
    dtor = f"virtual ~{classname}() = 0 {'{}'}"
    start = index_of(lines, pubsec)
    has_pubsec = start != -1
    if not has_pubsec:
        start = index_of(lines, "{") != -1
    for line in lines[:start+1]:
        code(line)
    if not has_pubsec:
        code(pubsec)
        cog.outl("    "+dtor)
    for line in lines[start+1:-1]:
        sline = line.strip()
        if sline and not sline.startswith("virtual"):
            tab = next(re.finditer(r"(\s*)\S", line)).group(1)
            cog.outl(f"{tab}virtual {sline.removesuffix(';')} = 0;")
        else:
            cog.outl(line)
    code(lines[-1])
