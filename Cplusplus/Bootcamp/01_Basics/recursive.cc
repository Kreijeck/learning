#include <iostream>

unsigned long long factorial(unsigned int n)
{
    if (n > 1)
    {
        return n * factorial(n - 1);
    }
    else
    {
        return 1;
    }
}

unsigned int sum(unsigned int n)
{
    if (n > 1)
    {
        return n + sum(n - 1);
    }
    else
    {
        return 1;
    }
}

int main()
{
    unsigned int n = 10;
    unsigned long long n_fac = factorial(n);
    unsigned int n_sum = sum(n);

    std::cout << "n! = " << n_fac << std::endl;
    std::cout << "sum of n = " << n_sum << std::endl;

    return 0;
}
