#include <iostream>
#include <cstdio>
using namespace std;

double prob[110][110][110];

double comb(int a, int b, int c) {
    return 1.0 * a * b / (a * b + b * c + c * a);
}

int main(void){
    int r, s, p;
    cin >> r >> s >> p;
    prob[r][s][p] = 1.0;
    for (int i = r; i > -1; i--) {
        for (int j = s; j > -1; j--) {
            for (int k = p; k > -1; k--) {
                if (k > 0) prob[i][j][k] += prob[i + 1][j][k] * comb(i + 1, k, j);
                if (i > 0) prob[i][j][k] += prob[i][j + 1][k] * comb(j + 1, i, k);
                if (j > 0) prob[i][j][k] += prob[i][j][k + 1] * comb(k + 1, j, i);
            }
        }
    }
    
    double a1 = 0.0, a2 = 0.0, a3 = 0.0;
    for (int i = 1; i <= r; i++) a1 += prob[i][0][0];
    for (int i = 1; i <= s; i++) a2 += prob[0][i][0];
    for (int i = 1; i <= p; i++) a3 += prob[0][0][i];
    printf("%.12f %.12f %.12f", a1, a2, a3);

    return 0;
}
