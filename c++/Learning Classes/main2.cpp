#include <cstdlib> 
#include <iostream>
using namespace std;

const int sides = 6;


class Dice {
    private:
        int dice[sides];
        int numberofrolls = 100;
    public:
        void roll()
        {
        for(int i = 0; i < numberofrolls; ++i){
            int roll = rand() % sides;
            dice[roll] += 1;
            }
        }

        void display(){
            for(int i = 0; i < sides; ++i){
                cout << "The number " << i+1 << " was rolled " << dice[i] << " times" << endl;
            }
        }
};

int main(){
    Dice d1;
    d1.roll();
    d1.display();
}
