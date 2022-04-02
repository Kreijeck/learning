#include <iostream>

using std::cin;
using std::cout;
using std::endl;

//int* input_array <=> int input_array[]
int array_maximum(int *input_array, unsigned int length)
{
    int current_max = 0;
    for (unsigned int i = 0; i < length; i++)
    {
        if (i == 0)
        {
            current_max = input_array[i];
        }
        else if (input_array[i] > current_max)
        {
            current_max = input_array[i];
        }
    }
    return current_max;
}

int main()
{
    unsigned int array_size = 10;
    //array auf dem Heap kann dynamisch deklariert werden
    // Heap Allocation
    int *p = new int[array_size];
    // Size of the pointer itself in Bytes
    cout << "Size of p: " << sizeof(p) << endl;
    // Size of the first array element, that the pointer points to
    cout << "size of *p: " << sizeof(*p) << endl;

    for (unsigned int i = 0; i < array_size; i++)
    {
        p[i] = i;
    }

    for (unsigned int i = 0; i < array_size; i++)
    {
        cout << p[i] << endl;
        cout << &p[i] << endl;
    }

    cout << "Das Maximum ist: " << array_maximum(p, array_size);

    // Heap Deallocation
    delete[] p;

    return 0;
}
