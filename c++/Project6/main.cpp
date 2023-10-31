// Yoenis Hernandez
// COP2000.0M2
// Started - 10/24/23
// Last Updated: 10/31/23
// Write a program that displays the following menu:
// Geometry Calculator
// Split the project up into functions one for each shape and area i had to find.
// Then i also created a menu function and a user validate function one to call the menu and one to check what the user had inputted
// For my errors i am checking for them using while loops. I am checking for negative numbers and also for invalid input
// Added some QOL improvements to my end console statements by letting you see a shrunk version of the choices you wrote.
// Had alot of fun enjoying using functions and even went ahead and looked at how to summon them from other files meaning i can do this with only
// my main function and just #include <filename> makes it look really nice.

#include <iostream>
using namespace std;

// Menu function to call options
int menu()
{
    int answer;

    while (answer != 4 && answer != 3 && answer != 2 && answer != 1) // while loop to validate the input
    {
        cout << "Geometry Calculator" << endl;
        cout << "1. Calculate the area of a Circle" << endl;
        cout << "2. Calculate the area of a Rectangle" << endl;
        cout << "3. Calculate the area of a triangle" << endl;
        cout << "4. Quit" << endl;
        cout << endl
             << "Enter your choice (1-4): ";
        cin >> answer;
        if (answer != 4 && answer != 3 && answer != 2 && answer != 1) // If statement to check for invalid input
        {
            cout << endl
                 << "Invalid Choice Try Again" 
                 << endl
                 << endl;
        }
        else
        {
            break;
        }
    }
    return answer; /* code */
}

// Function to figure out circle area
void circlearea()
{
    float radius;
    cout << endl
         << "Enter the radius of the circle: ";
    cin >> radius;
    while (radius < 0) // Checking for negative numbers
    {
        cout << "Invalid input" << endl;
        cout << endl
             << "Enter the radius of the circle: ";
        cin >> radius;
    }
    float area = 3.14159 * radius * radius; // The math
    cout << endl
         << "The area of the circle is " << area << endl;
}

// Function to figure out rectangle area
void rectanglearea()
{
    float length;
    float height;
    cout << endl
         << "Enter the length of the rectangle: ";
    cin >> length;
    while (length < 0) // Checking for Negative Numbers
    {
        cout << "invalid length. Input again: ";
        cin >> length;
    }
    cout << endl
         << "Enter the Height of the rectangle: ";
    cin >> height;
    while (height < 0)
    {
        cout << "invalid Height. Input again: ";
        cin >> height;
    }
    float area = length * height;
    cout << endl;
    cout << endl;
    cout << "L:" << length << "  H:" << height << endl; // My little QOL change to see your final inputs
    cout << "The area of the rectangle is " << area << endl;
}

// Function to figure out triangle area
void trianglearea()
{
    float base;
    float height;

    cout << endl
         << "Enter the base of the triangle: ";
    cin >> base;
    while (base < 0) // While loop to validate the base
    {
        cout << "Invalid base. Input again: ";
        cin >> base;
    }
    cout << endl
         << "Enter the height of the triangle: ";
    cin >> height;
    while (height < 0) // While loop to validate the height
    {
        cout << "Invalid height. Input again: ";
        cin >> height;
    }
    cout << endl;
    cout << endl;
    cout << endl;
    cout << "B:" << base << "  H:" << height << endl;
    float area = (base * height) / 2;
    cout << "The area of the Triangle is: " << area << endl;        
}

// Function to validate the user input
void uservalidate(int answer)
{
    if (answer == 1) // Validation for the user input
    {
        cout << endl
             << "You chose: Area of a Circle using Radius" << endl; // Letting user know which they have chosen
        circlearea();                                               // Call Approriate function
    }
    else if (answer == 2)
    {
        cout << endl
             << "You chose: Area of a Rectangle using Lenght and Width" << endl;
        rectanglearea();
    }
    else if (answer == 3)
    {
        cout << endl
             << "You chose: Area of a Triangle using Base and Height" << endl;
        trianglearea();
    }
    else if (answer == 4)
    {
        cout << endl
             << "You chose: 4" << endl;
    }
    else
    {
        cout << endl
             << "Invalid input" << endl;
    }
}

// Main function that intializes the program
int main()
{
    int choice = menu();  // Call menu function and assign to int variable
    uservalidate(choice); // Call uservalidate function and pass the int variable. does its thang
    return 0;
}
