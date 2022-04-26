#include <iostream>

namespace ad
{
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

void print_vehicle_data(Vehicle &vehicle)
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

// Wenn struct auf pointer zugreift, geht dies mit -> (statt ".")
void print_vehicle_data_pointer(Vehicle *vehicle)
{
    std::cout << "Vehicle ID: " << vehicle->id << std::endl;
    std::cout << "Vehicle Velocity [kph]: " << vehicle->velocity << std::endl;

    switch (vehicle->lane)
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

} // namespace ad


int main()
{
    ad::Vehicle v1 = {1, 100.0f, ad::Lane::CENTER_LANE};

    // seit c++20 -> Designated Struct Initializer -> Variable mit angeben
    ad::Vehicle v2 = {.id = 1, .velocity = 100.0f, .lane = ad::Lane::CENTER_LANE};
    print_vehicle_data(v1);
    print_vehicle_data_pointer(&v1);

    std::cout << std::endl;
    std::cout << "Same again with named Params: " << std::endl;


    ad::print_vehicle_data(v2);
    ad::print_vehicle_data_pointer(&v2);

    return 0;
}
