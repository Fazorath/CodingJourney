#include <iostream>
using namespace std;

int main()
{
    const int SIZE = 5;
    double x[SIZE];
    for (int i = 2; i <= SIZE; i++)
    {
        x[i] = 0.0;
    }
    cout << x << endl;
    return 0;
}
