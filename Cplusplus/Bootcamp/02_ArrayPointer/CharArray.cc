#include <iostream>

using std::cin;
using std::cout;
using std::endl;

int main()
{
    // einfache Anführungszeichen für jeden Buchstaben
    char my_name[] = {
        'T',
        'o',
        'm',
    };
    //Endzeichen das string zu ende ist
    char my_name2[] = {'T', 'o', 'm', '\0'};
    cout << my_name << endl;
    cout << my_name2 << endl;

    // doppelte Anführungszeichen für ein Wort, am schluss wird ein Zeichen \0 hinzugefügt
    char last_name[] = "Thomas";
    cout << last_name << endl;
    return 0;
}
