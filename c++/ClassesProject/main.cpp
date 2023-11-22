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

class TempCheck {
    private:
        int daysAbove = 0;
        int daysBelow = 0;
        int daysEqual = 0;
        int days = 0;
        int totalTemp = 0;
        int averageTemp = 0;
        int temp = 0;
        int tempArray[30] = {0};
        double sum = 0;
    
    public:

    void readtxt() {
        ifstream file("NovTemps.txt");
        if (!file) {
            cout << "Unable to open file";
            return; // exit if file not found
        }

        string line;
        while (getline(file, line)) {
            sum = stod(line);
            days++;
        }
        cout << "Days: " << days << endl;
        cout << "Sum: " << sum << endl;
        file.close();
    }
    int getAverage() {
        averageTemp = sum / days;
        return averageTemp;
    }


};



int main() {
    // ifstream file("NovTemps.txt");
    // if (!file) {
    //     cout << "Unable to open file";
    //     return 1; // exit if file not found
    // }

    // string line;
    // double sum = 0;
    // int count = 0;
    // while (getline(file, line)) {
    //     sum += stod(line);
    //     count++;
    // }

    // if (count > 0) {
    //     double average = sum / count;
    //     cout << "Average: " << average << endl;
    // }

    // file.close();
    // return 0;

    TempCheck temp;
    temp.readtxt();
    temp.getAverage();
    // cout << temp.getAverage() << endl;
}
