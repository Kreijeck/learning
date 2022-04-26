#include <iostream>

int main()
{
    // &: Memory Address - Reference
    // *p: Value of that memory adress- Dereference
    int number = 5;
    std::cout << "Value of number: " << number << std::endl;
    std::cout << "Adress of number: " << &number << std::endl;

    int *p = &number;

    number = 12;

    std::cout << "Value of p: " << p << std::endl;
    std::cout << "Adress of p: " << &p << std::endl;
    std::cout << "Value of memory adress that p points to: " << *p << std::endl;


    return 0;
}
