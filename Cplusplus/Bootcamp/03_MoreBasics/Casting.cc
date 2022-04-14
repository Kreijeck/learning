#include <iomanip>
#include <iostream>

// 1a. C++: static_cast<> - converts object from type to another
// 1b. C: (newDtype)(varName)

int main()
{
    double number = 3.14;
    std::cout << std::setprecision(20) << number << std::endl;

    int num2 = number;
    std::cout << num2 << std::endl;

    //C-Casting
    // groß nach klein verliert genauigkeit
    float number3 = (float)(number);
    std::cout << number3 << std::endl;

    // klein nach Groß. alles prima!
    float number4 = (double)(number3);
    std::cout << number3 << std::endl;


    //C++-Casting
    // groß nach klein verliert genauigkeit
    float number5 = static_cast<float>(number);
    std::cout << number5 << std::endl;

    // klein nach Groß. alles prima!
    float number6 = static_cast<double>(number3);
    std::cout << number6 << std::endl;
    return 0;
}
