#include <iostream>

// Enum values are integers
// Enum values in UPPERCASE
// Enum values are constant


// 1.) Two Enums cannot share the same names
// 2.) No Variable can have a name which already reserved by an enum
// 3.) Enums are not type safe

enum Anything
{
    FOO,
    BAR
};

enum PermissionLevel
{
    STUDENT = 1,
    TUTOR = 2,
    INSTRUCTOR = 3,
    ADMIN = 4

};

enum class ExamPersons
{
    STUDENT,
    INSTRUCTOR
};

//If no values declare, start with 0, number is set automatically
enum class PermissionLevel2
{
    STUDENT,    // 0
    TUTOR,      // 1
    INSTRUCTOR, // 2
    ADMIN       // 3

};

int main()
{
    // Declaration
    PermissionLevel user_jan = PermissionLevel::INSTRUCTOR;
    PermissionLevel user_peter = PermissionLevel::STUDENT;

    // bei Enum Class immer namespace verwenden!! Dafür können Namen doppelt belegt werden
    ExamPersons jan = ExamPersons::STUDENT;

    //When only one name is defined, it is possible without namespace
    Anything ich = FOO;

    return 0;
}
