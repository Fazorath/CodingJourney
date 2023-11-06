#include <iostream>
#include <fstream>
#include <string>
using namespace std;
int main(){
    int count, numtests, testscore, sum = 0;
    float average;  
    cout << "Enter total number of tests: ";
    cin >> numtests;

    for (count = 0; count < numtests; count++)
    {
        cout << "Enter test score: ";
        cin >> testscore;
        sum += testscore;
    }
    average = sum/numtests;
    cout << "Your average is " << average;
    return 0;
}
