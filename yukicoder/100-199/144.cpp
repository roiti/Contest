#include <iostream>
#include <cstdio>
using namespace std;
int main(void){
    int N;
    double p;
    cin >> N >> p;
    double P[N+1];
    for (int i = 0; i < N+1; i++) P[i] = 1.0;
    double ans = 0.0;
    for (int i = 2; i < N+1; i++) {
        ans += P[i];
        for (int j = 2*i; j < N+1; j += i) {
            P[j] *= 1.0-p;
        }
    }
    printf("%.10f",ans);
    return 0;
}
