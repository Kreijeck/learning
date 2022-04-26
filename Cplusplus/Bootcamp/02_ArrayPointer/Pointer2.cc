#include <iostream>

int main()
{
    // Heap allocation
    int *p = new int;
    *p = 4;

    std::cout << "Memory Adress of p: " << &p << std::endl;
    std::cout << "Memory Adress of pointed value: " << p << std::endl;
    std::cout << "Value of the memory Adress of pointed value: " << *p << std::endl;

    // Heap de-allocation
    // Speicher wird vom Heap wieder freigegeben
    delete p;
    // pointer auf nullpointer
    p = nullptr;

    //memory adress of heap variable
    std::cout << p << std::endl;


    return 0;
}
