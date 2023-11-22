// Yoenis Hernandez
// COP 2000
// 11/18/23

// Using OOP, write a C++ program that will indicate the number of days in a month where the temperature was above average,
// below average, and at the average for the month of November.
// Using an array to count the number of days above average, below average, and at average,
// read in an input file named NovTemps.txt that gives the temperature for each day of the month.
// The input file should be located in the current directory.
// If the temperature is above the average temperature,
// increment the counter in the array that holds the count for the days above average.
// If the temperature is below the average temperature, increment the counter in the array that holds the count
// for the days below average.  If the temperature is equal to the average temperature, increment the counter in
// the array that holds the count for the days equal to the average.

// When the end of file has been reached, display the count for the number of days above average, below average, and equal to the average.

// Be sure to place variables within the private accessor area of the class.
// Use a constructor to initialize the array elements to 0.  No global variables are allowed.
// A submission of all code in main() will result in a grade of 0.

#include <iostream>
#include <fstream>
#include <string>

using namespace std;

class TemperatureReader
{
private:
    static const int ISIZE = 30; // size of array
    int temps[ISIZE];           // array to hold temps
    int counters[3] = {0};      // counters array: 0 - belowAverage, 1 - equalAverage, 2 - aboveAverage
    int sum = 0; // sum of all temps

public:
    void tempread() // function to read file into array
    {       
        ifstream file("NovTemps.txt");
        for (int i = 0; i < ISIZE; i++)
        {
            file >> temps[i]; // read file into array
            sum += temps[i];  // sum of all temps
            // cout<<sum<<endl; // Checking to see if the sum was being added correctly
        }
    };

    int getAverage() // function to get AVERAGE
    {
        return sum / ISIZE; // return average using sum variable and the size of array. Easy and simple :)
    };

    int getAboveAverage() // // function to get number of days ABOVE average
    {
        for (int i = 0; i < ISIZE; i++)
        {
            if (temps[i] > getAverage()) // using getAverage() and checking against the items in array
            {
                counters[2] += 1;
                // cout<<temps[i]<<endl;
            }
        }
        return counters[2];
    };

    int getBelowAverage() //Function to get number of days BELOW average
    {
        for (int i = 0; i < ISIZE; i++)
        {
            if (temps[i] < getAverage()) // using getAverage() and checking against the items in array
            {
                counters[0] += 1;
                // cout<<temps[i]<<endl; // Checking to see if the temps were being read correctly
            }
        }
        return counters[0];
    };

    int getEqualAverage() // Function to get number of days EQUAL to average
    {
        for (int i = 0; i < ISIZE; i++)
        {
            if (temps[i] == getAverage()) // using getAverage() and checking against the items in array
            {
                counters[1] += 1;
            }
        }
        return counters[1];
    };
};


int main()
{
    TemperatureReader temp; // create object
    temp.tempread();       // call function to read file into array
    // The needed outputs using functions provided by the class i made
    cout << "The average temperature for the month of November is: " << temp.getAverage() << " Degrees" << endl;
    cout << "The number of days above average was: " << temp.getAboveAverage() << endl;
    cout << "The number of days below average was: " << temp.getBelowAverage() << endl;
    cout << "The number of days equal to the average is: " << temp.getEqualAverage() << endl;

    return 0;
}
