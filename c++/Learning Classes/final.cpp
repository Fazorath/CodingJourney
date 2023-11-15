// Yoenis Hernandez
// COP2000.0M2 
// 11/9/23
// Last Updated: 10/15/23
// Creates a class called dice with private variables and some public functions
// The variables specify the amount of times to roll the dice and also the counters for how many times each number is rolled
// Public includes the roll function and the display function
// Roll function using the <random> header creates a random number to use as a seed
// which is used to generate a random number in a range from 1 - 6
// Using a for loop to roll the dice the amount of times specified in the private variable
// We keep track of the amount of times each die is rolled using the variables specified in private
// Display function displays the results

#include <iostream>
#include <random>
using namespace std;

const int sides = 6; // Number of sides on the die

class Dice // Dice Class Needed
{
private:
	int numberofrolls = 100; // Number of times to roll the dice
	int number1 = 0; // Variables to keep track of the number of times each number is rolled
	int number2 = 0;
	int number3 = 0;
	int number4 = 0;
	int number5 = 0;
	int number6 = 0;

public:
	void roll() // Function to roll the Dice
	{
		random_device rd; // A random number generator not sure if this is the one to use sorry.
		mt19937 gen(rd()); // From my understanding this is the generator which is fed the numbers from the random_device rd
		uniform_int_distribution<int> distribution(1, sides); // Creates the random integers in a range which is specified with the distrubution

		for (int i = 0; i < numberofrolls; ++i) // For loop to roll the dice
		{
			int roll = distribution(gen); // Random roll
			
			if(roll == 1){ // if statements to count how many times each dice is rolled
				number1 += 1;
			}
			else if(roll == 2){
				number2 += 1;
			}
			else if(roll == 3){
				number3 += 1;
			}
			else if(roll == 4){
				number4 += 1;
			}
			else if(roll == 5){
				number5 += 1;
			}
			else if(roll == 6){
				number6 += 1;
			}	
			else
				cout << "Error" << endl;
		}
	}

	void display() // Function to display the results
	{
	cout << "The number " << "1" << " was rolled " << number1 << " times" << endl; // Displays the results
	cout << "The number " << "2" << " was rolled " << number2 << " times" << endl;
	cout << "The number " << "3" << " was rolled " << number3 << " times" << endl;
	cout << "The number " << "4" << " was rolled " << number4 << " times" << endl;
	cout << "The number " << "5" << " was rolled " << number5 << " times" << endl;
	cout << "The number " << "6" << " was rolled " << number6 << " times" << endl;
	};
};
int main()
{
	Dice TestDice; // Initialize class with TestDice
	TestDice.roll();  // Roll function using the TestDice class
	TestDice.display(); // Display function using the TestDice class

	return 0;
}
