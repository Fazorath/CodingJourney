//  Constructor
//
// A constructor in C++ is a special 'MEMBER FUNCTION' 
// having the same name as that of its class which is used 
// to initialize some valid values to the data members of an object.
// It is executed automatically whenever an object of a class is created.

// Destructor
//
// A destructor is a special member function that is called when an object
// is when the object is explicitly destroyed by a call to delete.

// Private Member Function
//
// A private member function is a member function that can only be accessed
// by other member functions of the same class. 

// Reference Varaibles
// allow a function to access the parameter's original argument.
// another name for an already existing variable.
// #include <iostream>
// using namespace std;
 
// int getValue(int);

// int main()
// {
//    int x = 2;
   
//    cout << getValue(x) << endl;
//    return 0;
// }

// int getValue(int num)
// {
//    return num + 5;
// }

#include <iostream>
using namespace std;
 
void doSomething(int);

int main()
{
   int x = 2;
 
   cout << x << endl;
   doSomething(x);
   cout << x << endl;
   return 0;
}

void doSomething(int num)
{
   num = 0;
   cout << num << endl;
}
