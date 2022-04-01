#include <iostream>
// 1.) User Input: side length of square
// 2.) Compute the perimeter and area of square
// 3.) Print out the values of the console
int main()
{
    int x;
    unsigned int abs_x;
    std::cout << "Please enter an Integer: ";
    std::cin >> x;

    if (x < 0)
    {
        abs_x = -x;
    }
    else
    {
        abs_x = x;
    }

    std::cout << "Absolute from " << x << " is " << abs_x;

    return 0;
}
