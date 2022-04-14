#include <iostream>

// ohne Leerzeichen, ohne ;
//wird vom precompiler als Zahl im Code gesetzt
#define NUM_VEHICLES 3

//echte Variable im precompiler -> bessere Lösung, bspw für Debuggen
constexpr int DEFAULT_VEHICLE_ID = -1;

//const -> teilweise während compiletime noch nicht definiert
const int NUM_VEHICLES_Alt = 4;
const float DEFAULT_VELOCITY = 0.0f;

enum class Lane
{
    RIGHT_LANE,
    CENTER_LANE,
    LEFT_LANE
};

struct Vehicle
{
    int id;
    float velocity;
    Lane lane;
};

// Werte von Vehicle werden nur gelesen nicht geschrieben -> daher const angeben
//const Wert darf nicht verwendendet werden
//const&: Read-only
void print_vehicle_data(const Vehicle &vehicle)
{
    std::cout << "Vehicle ID: " << vehicle.id << std::endl;
    std::cout << "Vehicle Velocity [kph]: " << vehicle.velocity << std::endl;

    switch (vehicle.lane)
    {
    case Lane::CENTER_LANE:
        std::cout << "Vehicle Lane Association: CENTER LANE" << std::endl;
        break;

    case Lane::LEFT_LANE:
        std::cout << "Vehicle Lane Association: LEFT LANE" << std::endl;
        break;

    case Lane::RIGHT_LANE:
        std::cout << "Vehicle Lane Association: RIGHT LANE" << std::endl;
        break;

    default:
        break;
    }
}


int main()
{
    Vehicle v1 = {.id = 1, .velocity = 100.0f, .lane = Lane::CENTER_LANE};
    Vehicle v2 = {.id = 2, .velocity = 90.0f, .lane = Lane::RIGHT_LANE};
    Vehicle v3 = {.id = DEFAULT_VEHICLE_ID, .velocity = 130.0f, .lane = Lane::LEFT_LANE};

    Vehicle vehicles_in_scene[NUM_VEHICLES] = {v1, v2, v3};

    for (int i = 0; i < NUM_VEHICLES; i++)
    {
        print_vehicle_data(vehicles_in_scene[i]);
    }


    return 0;
}
