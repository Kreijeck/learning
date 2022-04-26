#include <iostream>

// dType varName[numElements]
// Elemente müssen fest vergeben sein - keine Variable hier möglich

int main()
{
    float user_balances[10] = {};

    for (int i = 0; i < 10; i++)
    {
        std::cout << "Index" << i << ": " << user_balances[i] << std::endl;
    }

    for (int i = 0; i < 10; i++)
    {
        user_balances[i] = 2.f * float(i);
    }


    for (int i = 0; i < 10; i++)
    {
        std::cout << "Index" << i << ": " << user_balances[i] << std::endl;
    }


    return 0;
}
