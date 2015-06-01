#include <iostream>
#include <cstdio>
#include <cmath>

using namespace std;
int main(void){
    while (1) {
        int N;
        cin >> N;
        if (N == 0) break;
        int l[N];
        for (int i = 0; i < N; i++) cin >> l[i];
        
        double H = 1e10;
        int s,a,c;
        for (int S = 0; S < 16; S++) {
            for (int A = 0; A < 16; A++) {
                for (int C = 0; C < 16; C++) {
                    
                    int R = S;
                    int L[256];
                    for (int i = 0; i < 256; i++) L[i] = 0;
                    for (int i = 0; i < N; i++) {
                        R = (A*R+C)%256;
                        L[(l[i]+R)%256] += 1;
                    }
                    double tmp = 0.0;
                    for (int i = 0; i < 256; i++) {
                        if (L[i] > 0) {
                            tmp += -(double)L[i]/N*log2((double)L[i]/N);
                        }
                    }
                    if (tmp < H) {
                        H = tmp;
                        s = S; a = A; c = C;
                    }
                }
            }
        }
        printf("%d %d %d\n",s,a,c);
    }
    return 0;
}


