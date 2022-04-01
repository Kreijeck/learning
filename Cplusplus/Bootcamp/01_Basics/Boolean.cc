#include <iostream>

int main()
{
    bool check1 = false;
    bool check2 = true; // 1

    if (check1)
    {
        std::cout << "Check 1 is true";
    }

    std::cout << check2 << std::endl;
    std::cout << std::boolalpha << check2 << std::endl;

    return 0;
}
