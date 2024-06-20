import contextlib
# noinspection PyUnresolvedReferences
import cog


def code(block: str):
    cog.outl(block, dedent=True, trimblanklines=True)


__GEN_START = "#if 0 // Untouched code input"
__GEN_BETWEEN = "#else // Generated code output"
__GEN_END = "#endif // Generated code output end"


def get_code_lines() -> list[str]:
    return cog.previous.strip().split("\n")


def is_codein_wrapped():
    lines = get_code_lines()
    return lines[0].endswith(__GEN_START) and lines[-1].endswith(__GEN_END)


def get_code_input():
    lines = get_code_lines()
    if not is_codein_wrapped():
        return lines

    end_index = [e.strip() for e in lines].index(__GEN_BETWEEN)
    return lines[1:end_index]


@contextlib.contextmanager
def wrap_code_input():
    code(__GEN_START)
    raw_code = get_code_input()
    for line in raw_code:
        code(line)
    code(__GEN_BETWEEN)
    yield raw_code
    code(__GEN_END)


def twice():
    with wrap_code_input() as raw:
        code(raw[0])
        code(raw[0])
