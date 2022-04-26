#include <iostream>

int main()
{
    int number;
    bool is_prime = true;

    std::cout << "Please enter a number: ";
    std::cin >> number;

    for (int i = 2; i < number; i++)
    {
        if (number % i == 0)
        {
            is_prime = false;
            break;
        }
    }

    if (is_prime)
    {
        std::cout << number << " is a Prime Number!";
    }
    else
    {
        std::cout << number << " is NOT a Prime Number!";
    }


    return 0;
}
