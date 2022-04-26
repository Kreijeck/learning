#include <iostream>

int main()
{
    int year;
    std::cout << "Please enter a year: ";
    std::cin >> year;

    if (year % 4 == 0 and year % 100 != 0)
    {
        std::cout << year << " is a leap year (Schaltjahr)" << std::endl;
    }
    else if (year % 400 == 0)
    {
        std::cout << year << " is a leap year (Schaltjahr)" << std::endl;
    }
    else
    {
        std::cout << year << " is NOT a leap year (Schaltjahr)" << std::endl;
    }
    return 0;
}
