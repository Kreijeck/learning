#include <iostream>

// dType varName[numElements]
// Elemente müssen fest vergeben sein - keine Variable hier möglich

int main()
{
    int array1[5] = {2, 3, 4, 51, 0};

    for (int i = 0; i < 5; i++)
    {
        std::cout << "Index" << i << ": " << array1[i] << std::endl;
    }

    // kann auch direkt initialisiert werden -> Groesse automatisch klar
    int array2[] = {20, 21, 22};

    // !!Variable Länge über Variable ist verboten!!!
    int k = 6;
    int array3[k];

    array3[2] = 5;

    for (int i = 0; i < k; i++)
    {
        std::cout << array3[i] << std::endl;
    }


    return 0;
}
