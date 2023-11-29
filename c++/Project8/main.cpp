// Yoenis Hernandez
// COP 2000
// 11/28/23
// read in a file of names
// read and store the file names into an array of 30 names
// sort the array using selection sort or buuble sort
// list the names in ascending alpabetical order


#include <iostream>
#include <string>
#include <fstream>

using namespace std;

class SortNames
{
private:
    static const int ISIZE = 30;
    string names[ISIZE];
    bool display = true;

public:
    void readNames()
    {
        ifstream inputFile("Names.txt");
        if (inputFile.is_open())
        {
            for (int i = 0; i < ISIZE; i++)
            {
                inputFile >> names[i];
            }
            inputFile.close();
        }
        else
        {
            cout << "Error opening file" << endl;
            bool display = false;
        }
    }
    void sortNames()
    {
        int minIndex;
        string minValue;
        for (int i = 0; i < ISIZE - 1; i++)
        {
            minIndex = i;
            minValue = names[i];
            for (int j = i + 1; j < ISIZE; j++)
            {
                if (names[j] < minValue)
                {
                    minValue = names[j];
                    minIndex = j;
                }
            }
            names[minIndex] = names[i];
            names[i] = minValue;
        }
    }

    void displayNames()
    {
        for (int i = 0; i < ISIZE; i++)
        {
            cout << names[i] << endl;
        }  
    }
};

int main(){
    SortNames names;
    names.readNames();
    names.sortNames();
    if (bool display = true){
        names.displayNames();
    }
    return 0;
}
