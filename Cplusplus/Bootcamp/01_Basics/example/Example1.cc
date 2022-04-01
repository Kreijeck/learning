#include <iostream>
// 1.) User Input: side length of square
// 2.) Compute the perimeter and area of square
// 3.) Print out the values of the console
int main()
{
    float perimeter;
    float area;
    float side;

    std::cout << "Please enter the side length: ";
    std::cin >> side;
    area = side * side;
    perimeter = 4 * side;
    std::cout << "Area: " << area << std::endl;
    std::cout << "perimeter: " << perimeter << std::endl;

    return 0;
}
