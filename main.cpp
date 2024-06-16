#include <iostream>

int main() {
    /*#py
        import cog
        for i in range(1, 4):
            cog.outl(f'std::cout << "{i}!" << std::endl;')
    #py{*/
    std::cout << "1!" << std::endl;
    std::cout << "2!" << std::endl;
    std::cout << "3!" << std::endl;
    //#py} (checksum: 131f858367ecbfd26647b2293061d884)
    std::cout << "Hello, World!" << std::endl;
    return 0;
}
