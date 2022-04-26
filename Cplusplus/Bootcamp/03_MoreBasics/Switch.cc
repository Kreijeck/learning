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
    PermissionLevel user_jan = PermissionLevel::INSTRUCTOR;
    PermissionLevel user_peter = PermissionLevel::STUDENT;

    greet_permission_level(user_jan);
    greet_permission_level(user_peter);

    return 0;
}
