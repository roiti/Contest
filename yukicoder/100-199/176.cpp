#include <iostream>
using namespace std;
int main(void){
    long long A, B, T;
    cin >> A >> B >> T;
    long long over = min((A-T%A)%A, (B-T%B)%B);
    for (long long i = 1; i < 10000000; i++) { 
        if (T >= i*A) over = min(over, (B-(T%A+i*A)%B)%B);
        if (T >= i*B) over = min(over, (A-(T%B+i*B)%A)%A);
    }
    cout << T+over << endl;
    return 0;
}
