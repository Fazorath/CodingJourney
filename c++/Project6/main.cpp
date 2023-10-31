// Yoenis Hernandez
// COP2000.0M2
// 10/30/23
// Last Updated: 10/30/23
// Write a program that displays the following menu:
// Geometry Calculator

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

   
    while (length < 0 )
    {
        cout << "invalid length. Input again: ";
        cin >> length;
    }  
    cout << endl <<"Enter the Height of the rectangle: ";
    cin >> height;
    while (height < 0 )
    {
        cout << "invalid Height. Input again: ";
        cin >> height;
    }
    float area = length * height;
    cout << endl;
    cout << endl;
    cout << "L:" << length << "  H:" << height << endl;
    cout << "The area of the rectangle is " << area << endl;
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
       cout << endl << "You chose: Area of a Triangle using Base and Height" << endl;
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
