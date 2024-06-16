from pycodegen import *


def test1(n: int):
    for i in range(1, n+1):
        # language=c++
        code(f'std::cout << "{i}!" << std::endl;')
