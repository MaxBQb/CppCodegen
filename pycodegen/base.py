import cog


def code(block: str):
    cog.outl(block, dedent=True, trimblanklines=True)
