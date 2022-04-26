#include <iostream>

// Enum values are integers
// Enum values in UPPERCASE
// Enum values are constant

enum PermissionLevel
{
    STUDENT = 1,
    TUTOR = 2,
    INSTRUCTOR = 3,
    ADMIN = 4

};

struct UserData
{
    char *name;
    unsigned int id;
    PermissionLevel permission_level;
};


void greet_permission_level(PermissionLevel level)
{
    switch (level)
    {
    case PermissionLevel::STUDENT:
        std::cout << "Hello Student" << std::endl;
        break;
    case PermissionLevel::TUTOR:
        std::cout << "Hello Tutor" << std::endl;
        break;
    case PermissionLevel::INSTRUCTOR:
        std::cout << "Hello Instructor" << std::endl;
        break;
    case PermissionLevel::ADMIN:
        std::cout << "Hello Admin" << std::endl;
        break;

    default:
        std::cout << "Default case, something level not found in Permission!!" << std::endl;
        break;
    }
}

int main()
{
    // Declaration
    PermissionLevel permission_level_jan = PermissionLevel::INSTRUCTOR;
    PermissionLevel permission_level_peter = PermissionLevel::STUDENT;

    //Usage of Enum
    greet_permission_level(permission_level_jan);
    greet_permission_level(permission_level_peter);

    //Usage of struct
    UserData user_jan = {"Jan", 108014222, permission_level_jan};

    greet_permission_level(user_jan.permission_level);

    UserData user_peter;
    user_peter.name = "Peter";
    user_peter.id = 1080153466;
    user_peter.permission_level = permission_level_peter;
    greet_permission_level(user_peter.permission_level);

    return 0;
}
