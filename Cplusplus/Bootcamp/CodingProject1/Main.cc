#include <iostream>
#include <stdlib.h>

#define LEN_X 10u
#define LEFT 'a'
#define RIGHT 'd'

void game()
{
    bool repeat = true;


    while (repeat)
    {
        unsigned int player = 0;
        unsigned int start = 0;
        unsigned int goal = LEN_X - 1;

        char move;
        bool finished = false;

        while (!finished)
        {
            for (unsigned int i = 0; i < LEN_X; i++)
            {
                if (i != player && i != start && i != goal)
                {
                    std::cout << '.';
                }
                else if (i == player)
                {
                    std::cout << 'P';
                }

                else
                {
                    std::cout << '|';
                }
            }

            std::cin >> move;
            //clear console
            system("clear");

            if (LEFT == move)
            {
                if (player > 0)
                {
                    player--;
                    std::cout << "You moved to the left" << std::endl;
                }
                else
                {
                    std::cout << "You bounced!!" << std::endl;
                }
            }
            else if (RIGHT == move)
            {
                if (player < goal)
                {
                    player++;
                    std::cout << "You moved to the right" << std::endl;
                }
                else
                {
                    std::cout << "You bounced!!" << std::endl;
                }
            }
            else
            {
                std::cout << "Ungültige Bewegung" << std::endl;
            }

            if (player == goal)
            {
                finished = true;
                std::cout << "you won the game!" << std::endl;
            }
        }
        std::cout << "Play again (1=Yes, 0=NO)" << std::endl;
        std::cin >> repeat;

        system("clear");
    }
}

int main()
{
    game();

    return 0;
}
