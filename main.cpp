#include <iostream>

int main() {
    /*#py
        scripts.test1(4)
    #py{*/
    std::cout << "1!" << std::endl;
    std::cout << "2!" << std::endl;
    std::cout << "3!" << std::endl;
    std::cout << "4!" << std::endl;
    //#py} (checksum: 69c26b6fc05a904729370892bfe6a448)

    //#py twice() #py{
    #if 0 // Untouched code input
    std::cout << "Hello, World!" << std::endl;
    #else // Generated code output
    std::cout << "Hello, World!" << std::endl;
    std::cout << "Hello, World!" << std::endl;
    #endif // Generated code output end
    //#py} (checksum: 0e9fa840682f5f80df6f41a182096d3a)

    return 0;
}
