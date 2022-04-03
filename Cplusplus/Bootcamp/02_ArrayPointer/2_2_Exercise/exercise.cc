#include <iostream>

#include "exercise.h"

// Exercise 1
void push_back(int *&input_array, const unsigned int &size, const int &value)
{
    int *ext_array = new int[size + 1];
    for (unsigned int i = 0; i < size; i++)
    {
        ext_array[i] = input_array[i];
    }
    delete[] input_array;
    ext_array[size] = value;

    input_array = ext_array;
}

// Exercise 2
void pop_back(int *&input_array, const unsigned int &size)
{
    int *ext_array = new int[size - 1];
    for (unsigned int i = 0; i < size - 1; i++)
    {
        ext_array[i] = input_array[i];
    }

    delete[] input_array;

    input_array = ext_array;
}
