//Yoenis Hernandez
//COP2000.0M2 
// Open a text file using the fstream from chapter 5,
// Read from the file and find how many names and how many characters are in each name
// Used 1 loop initially but would result in something like this:
// '1 names were 8 characters long'
// To solve this i made another for loop that when encounters an amount of characters that only has 1 name it will produce a new cout:
// '1 name is 8 Characters long'
// Not sure if this is the best way to go about it.



#include <iostream>
#include <fstream>
#include <string>
using namespace std;


int main() {
    // Open file
    ifstream inputFile("Student.txt"); //Opens the txt file
    
    // File open Check
    if (!inputFile.is_open()) { // if file is not open
        cerr << "Failed to open the file 'students.txt'." << endl; // file open error
        return 1;
    }

    // Variables
    string name; // Names
    int totalCount = 0; // Letters in names
    const int maxLength = 50;  // Adjust the maximum name length as needed
    int nameLengthCount[maxLength] = { 0 };

    // While loop using file 
    while (inputFile >> name) { // While loop reading the lines in txt file, put it into name variable
        int nameLength = name.length(); // lenght of the name variable into namelenght int.
        if (nameLength < maxLength) { // if the lenght is less than the max
            nameLengthCount[nameLength]++; // add the previous name lenght variable to our  initial name lenght variable
        }
        // cout << totalCount; checking if was counting right
        totalCount++; // total number of names
    }
    inputFile.close(); // Always close the file !!!
    cout << "The file contains " << totalCount << " names\n" << endl;  // Total Names

    // For loop for character
    // I wasnt sure how to selevt when ther was only one name with a certain amount so i created 2 lists for it
   
    // loop character count that only starts after 2 character names
    for (int i = 2; i < maxLength; i++) { // for loop using variable i that increments by 1
        if (nameLengthCount[i] > 0) {  // if variable is greater than the current iteration of loop so 0,1,2,3,4 etc
            if (nameLengthCount[i] == 1) { // Break once it reaches the characters with only one name
                break;
            }
        cout << nameLengthCount[i] << " names are " << i << " characters long" << endl;// cout the amount of names and their characters.
           
        }
        
        }
   // Loop for when there is only 1 name with Certain amount of letters
   // Main purpose of having to do this was because my output would say '1 names were 8 characters long'
   // i wasnt sure how to 
    for (int i =7; i < maxLength; i++) { // Our case no names above 7 so we use 7 as our starting 
        if (nameLengthCount[i] > 0) {  // if variable is greater than the current iteration of loop so 0,1,2,3,4 etc
            cout << nameLengthCount[i] << " name is " << i << " characters long" << endl; // cout the amount of names and their characters.
        }
    }

    
    return 0;
}