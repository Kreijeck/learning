#include <iostream>

using std::cin;
using std::cout;
using std::endl;

int main()
{
    //1D Array (Vector)
    int my_array1[3] = {1, 2, 3};

    //2d-Array (Matrix)
    // array[row][col]
    int my_matrix[3][2] = {{1, 2}, {3, 4}, {5, 6}};

    for (int i = 0; i < 3; i++)
    {
        for (int j = 0; j < 2; j++)
        {
            cout << "i= " << i << ", j = " << j << ", value = " << my_matrix[i][j] << endl;
        }
    }
}
