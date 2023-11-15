#include <iostream>
using namespace std;

const int sides = 6;


class Dice {
    private:
        int dice[sides];
        int runs;
    public:
        void roll();
        

        void display();
};

int main(){
    HelloWorld hw;
    hw.sayHello();
    hw.sayGoodbye();
    hw.saySomething("Yannah Blaise");
    return 0;
}
