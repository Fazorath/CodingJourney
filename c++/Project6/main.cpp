// Yoenis Hernandez
// COP2000.0M2
// 10/30/23
// Last Updated: 10/30/23
// Write a program that displays the following menu:

//     Geometry Calculator

//     1.  Calculate the area of a Circle
//     2.  Calculate the area of a Rectangle
//     3.  Calculate the area of a Triangle
//     4.  Quit

//      Enter your choice (1-4):

//      If the user enters 1, the program should ask for the radius of the circle and then display its area.   Use 3.14159 for PI.  If the user enters 2, the program should ask for the length and width of the rectangle, and then display the rectangle's area.  If the user enters 3, the program should ask for the triangle's base and its height, and then display its area.   If the user enters 4, the program should end.

//      Input Validation:  Decide how the program should handle illegal input for the menu choice or a negative value for any of the other inputs.
#include <iostream>
#include <string>
using namespace std;


int menu (){
    int answer;
    while (answer != 4 && answer != 3 && answer != 2 && answer != 1)
        {
        cout << "Geometry Calculator" << endl;
        cout << "1. Calculate the area of a Circle" << endl;
        cout << "2. Calculate the area of a Rectangle" << endl;
        cout << "3. Calculate the area of a triangle" << endl;
        cout << "4. Quit" << endl;
        cout << endl << "Enter your choice (1-4): ";
        cin >> answer;
        }
        return answer; /* code */
}

float circlearea(){
    float radius;
    cout << "Enter the radius of the circle: ";
    cin >> radius;
    while (radius < 0)
    {
        cout << "Invalid input" << endl;
        cout << "Enter the radius of the circle: ";
        cin >> radius; // Ask for radius again
    }
    float area = 3.14159 * radius * radius; // No need to declare area again
    cout <<endl << "The area of the circle is " << area << endl;
    return area;
}

// Starting the function for the Area of a Rectangle 
float rectanglearea(){
    float length;
    float height;
    cout << endl <<"Enter the length of the rectangle: ";
    cin >> length;
    cout << endl <<"Enter the Height of the rectangle: ";
    cin >> height;
    if (length < 0 )
    {
        cout << "invalid Lenght. Input again: ";
        cin >> length;
    }  
    if (height < 0 )
    {
        cout << "invalid Height. Input again: ";
        cin >> height;
    }
    float area = length * height;
    cout << endl << "The area of the rectangle is " << area << endl;
    return area;
}


void uservalidate(int answer){
   if (answer == 1){
       cout << endl << "You chose: Area of a Circle using Radius" << endl;
       circlearea();
   }
   else if (answer == 2){
        cout << endl << "You chose: Area of a Rectangle using Lenght and Width" << endl;
        rectanglearea();
   }
   else if (answer == 3){
       cout << endl << "You chose: 3" << endl;
   }
   else if (answer == 4){
       cout << endl << "You chose: 4" << endl;
   }
   else {
       cout << endl << "Invalid input" << endl;
   }
}

int main(){
    int choice = menu();
    uservalidate(choice);
    return 0;
}
