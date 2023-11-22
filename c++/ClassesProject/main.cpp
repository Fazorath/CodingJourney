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
    static const int ISIZE = 30;
    int temps[ISIZE];
    int aboveAverage = 0;
    int belowAverage = 0;
    int equalAverage = 0;
    double sum = 0;

public:
    void tempread()
    {       
        ifstream file("NovTemps.txt");
        for (int i = 0; i < ISIZE; i++)
        {
            file >> temps[i];
            sum += temps[i];
            // cout<<sum<<endl;
        }
    };

    int getAverage()
    {
        return sum / ISIZE;
    };

    int getAboveAverage()
    {
        for (int i = 0; i < ISIZE; i++)
        {
            if (temps[i] > getAverage())
            {
                aboveAverage += 1;
                // cout<<temps[i]<<endl;
            }
        }
        return aboveAverage;
    };

    int getBelowAverage()
    {
        for (int i = 0; i < ISIZE; i++)
        {
            if (temps[i] < getAverage())
            {
                belowAverage += 1;
                // cout<<temps[i]<<endl;
            }
        }
        return belowAverage;
    };

    int getEqualAverage()
    {
        for (int i = 0; i < ISIZE; i++)
        {
            if (temps[i] == getAverage())
            {
                equalAverage += 1;
                // cout<<temps[i]<<endl;
            }
        }
        return equalAverage;
    };
};

int main()
{
    TemperatureReader temp;
    temp.tempread();
    cout << "The average temperature for the month of November is: " << temp.getAverage() << " Degrees" << endl;
    cout << "The number of days above average was: " << temp.getAboveAverage() << endl;
    cout << "The number of days below average was: " << temp.getBelowAverage() << endl;
    cout << "The number of days equal to the average is: " << temp.getEqualAverage() << endl;

    return 0;
}
