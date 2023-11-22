#include <iostream>
#include <fstream>
#include <string>
#include <array>

using namespace std;

int main()
{

    const int ISIZE = 30;
    int temps[ISIZE];
    ifstream dataFile;
    dataFile.open("NovTemps.txt");
    if (!dataFile)
        cout << "Error opening data file\n";
    else // Input daily sales
    {
        for (int day = 0; day < ISIZE; day++)
            dataFile >> sales[day];
        dataFile.close();
    }
    cout << "The sales for the 5 days are:\n";
    for (int day = 0; day < ISIZE; day++)
        cout << sales[day] << endl;
}
