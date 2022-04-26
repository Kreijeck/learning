#include <iostream>

int main()
{
    for (int i = 1; i <= 3; i++)
    {
        std::cout << i << ".ter Durchlauf" << std::endl;
    }

    // nested for Loop:
    for (int i = 0; i < 4; i++)
        for (int i = 0; i < 4; i++)
        {
            for (int j = 0; j < 3; j++)
            {
                std::cout << "i=" << i << " j=" << j << std::endl;
            }
        }

    return 0;
}
