#include <iostream>
#include <cstdlib>
#include <ctime>

class Dice {
public:
    Dice() {
        // Seed the random number generator with the current time
        std::srand(static_cast<unsigned int>(std::time(nullptr)));
    }

    int roll() const {
        // Generate a random number between 1 and 6 (inclusive)
        return rand() % 6 + 1;
    }
};

int main() {
    const int numRolls = 100;
    int rollCounts[6] = {0}; // Initialize an array to count the occurrences of each number

    Dice die;

    for (int i = 0; i < numRolls; ++i) {
        int result = die.roll();
        rollCounts[result - 1]++; // Adjust index to match array (1-based die)
    }

    // Display the results
    for (int i = 0; i < 6; ++i) {
        std::cout << "The number " << (i + 1) << " was rolled " << rollCounts[i] << " times\n";
    }

    return 0;
}
