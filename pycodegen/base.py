import contextlib
from types import GeneratorType

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


def index_of(lines: list[str], text: str):
    try:
        return [e.strip() for e in lines].index(text)
    except ValueError:
        return -1


def get_code_input():
    lines = get_code_lines()
    if not is_codein_wrapped():
        return lines

    end_index = index_of([e.strip() for e in lines], __GEN_BETWEEN)
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


def macro(**kwargs):
    def make_callable(rng: range):
        it = iter(rng)
        return lambda: next(it)

    kwargs = {
        k: make_callable(v) if isinstance(v, (range, GeneratorType)) else v
        for k, v in kwargs.items()
    }

    with wrap_code_input() as raw:
        for line in raw:
            for k, v in kwargs.items():
                key = "{{" + k + "}}"
                if key in line:
                    line = line.replace(key, str(v() if callable(v) else v))
            code(line)
