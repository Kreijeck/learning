#include <iostream>

// dType varName[numElements]
// Elemente müssen fest vergeben sein - keine Variable hier möglich

int main()
{
    // {} werden alle Werte mit 0 initialisiert
    float vector1[3] = {};
    //Gleichheitszeichen kann weggelassen werden
    float vector2[3]{};

    std::cout << "Enter values for Vector 1: " << std::endl;

    for (int i; i < 3; i++)
    {
        std::cin >> vector1[i];
    }

    // Initialize Vector2
    for (int i = 0; i < 3; i++)
    {
        vector2[i] = 2 * float(i);
    }

    //sum
    for (int i = 0; i < 3; i++)
    {
        std::cout << "Sum at pos " << i + 1 << ": " << vector1[i] << " + " << vector2[i] << " = "
                  << vector1[i] + vector2[i] << std::endl;
    }


    return 0;
}
