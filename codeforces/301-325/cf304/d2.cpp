
#include <iostream>
#include <cstdio>
#include <cmath>
using namespace std;

const int R = 5000100;

int p[R];

int main(void){
    for (int i = 2; i < R; i++) p[i] = 1;

    for (int i = 2; i < int(sqrt(R) + 1); i++) {
        if (p[i] > 0) {
            for (int j = 2 * i; j < R; j += i)
                p[j] = -i;
        }
    }

    for (int i = 2; i < R; i++) {
        if (p[i] < 0) {
            p[i] = p[i / -p[i]] + 1;
        }
    }

    for (int i = 2; i < R; i++) p[i] += p[i - 1];

    int t, a, b;
    cin >> t;
    while (t--) {
        scanf("%d %d", &a, &b);
        printf("%d\n", p[a] - p[b]);
    }
    return 0;
}
