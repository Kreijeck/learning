#include <iostream>


// wenn es geht, wird zur Compiletime berechnet und nicht zur Runtime.
// falls nicht möglich wird es zur Runtime berechnet
constexpr int fac(int n)
{
    if (n > 1)
    {
        return n * fac(n - 1);
    }
    else
    {
        return 1;
    }
}

int main()
{
    int l = fac(3);

    //erlaubt, da jetzt fac(3) schon zur Compiletime berechnet wird
    int a[fac(3)]{};

    return 0;
}
