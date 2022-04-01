#include <iostream>

int main()
{
    int sum = 0;
    // while wird Bedingung am Anfang überprüft!
    while (sum < 20)
    {
        std::cout << "\nDie Summe beträgt " << sum << ", Bitte nächsten Wert eintragen: ";
        int input;
        std::cin >> input;
        sum += input;
    }

    // do while wird Bedingung am Ende überprüft!
    do
    {
        std::cout << "\nDie Summe beträgt " << sum << ", Bitte nächsten Wert eintragen: ";
        int input;
        std::cin >> input;
        sum += input;
    } while (sum < 20);


    return 0;
}
