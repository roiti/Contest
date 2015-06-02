#include <iostream>
using namespace std;
long long fib[50];

int main(void) {
    fib[0] = fib[1] = 1;
    for (int i = 2; i < 50; i++) {
        fib[i] = fib[i - 1] + fib[i - 2];
    }
    int n;
    cin >> n;
    cout << fib[n] << endl;
    return 0;
}
