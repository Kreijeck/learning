#include <iostream>

// ReturnType FunctionName (ParameterList - optional)
//{
// FunctionCode
//}

// Function ohne Parameter
int user_input()
{
    int number;
    std::cout << "Please enter a number: ";
    std::cin >> number;

    return number;
}

// function mit Parameter
bool is_even(int number)
{
    if (number % 2 == 0)
    {
        return true;
    }
    else
    {
        return false;
    }
}

int main()
{
    int number = user_input();
    std::cout << number << std::endl;
    bool check = is_even(number);
    std::cout << "Die Zahl is gerade? " << std::boolalpha << check;

    return 0;
}
