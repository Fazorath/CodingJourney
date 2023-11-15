#include <iostream>
using namespace std;

class HelloWorld {
    public:
        void sayHello() {
            cout << "First time using a class" << endl;
        }
        void sayGoodbye() {
            cout << "Goodbye!" << endl;
        }
        void saySomething(string s) {
            cout << s << endl;
        }
};

int main(){
    HelloWorld hw;
    hw.sayHello();
    hw.sayGoodbye();
    hw.saySomething("Yannah Blaise");
    return 0;
}