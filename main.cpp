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

    /*#py
        macro(i=range(1,5,2), j=(j for j in range(2, 8) if j%3 == 2), std="std::c")
    #py{*/
    #if 0 // Untouched code input
    {{std}}out << "Hello, " << {{j}} << {{i}} << "!" << std::endl;
    {{std}}out << "Middle!" << std::endl;
    {{std}}out << "Bye, {{j}}-{{i}}!" << std::endl;
    #else // Generated code output
    std::cout << "Hello, " << 2 << 1 << "!" << std::endl;
    std::cout << "Middle!" << std::endl;
    std::cout << "Bye, 5-3!" << std::endl;
    #endif // Generated code output end
    //#py} (checksum: c32d33a60b68081cc5d66c47e31c3649)

    return 0;
}
