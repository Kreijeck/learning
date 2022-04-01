#include <iostream>


int main()
{
    double number1;
    double number2;
    double result;

    std::cout << "Please enter a number: ";
    std::cin >> number1;

    std::cout << "Please enter another number: ";
    std::cin >> number2;

    // Multiplikation
    result = number1 * number2;
    std::cout << "number1 * number2 = " << result << std::endl;

    // Addition
    result = number1 + number2;
    std::cout << "number1 + number2 = " << result << std::endl;

    //Subtraktion
    result = number1 - number2;
    std::cout << "number1 - number2 = " << result << std::endl;

    //Division
    result = number1 / number2;
    std::cout << "number1 / number2 = " << result << std::endl;

    return 0;
}
