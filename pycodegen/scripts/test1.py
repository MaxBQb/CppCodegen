from pycodegen import *


def test1():
    for i in range(1, 4):
        # language=c++
        code(f'std::cout << "{i}!" << std::endl;')
