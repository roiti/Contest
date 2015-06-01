#include <iostream>
#include <stdio.h>
#include <algorithm>
#include <string.h>
#define REP(i,a,b) for (int i = (a); i < (b); i++)
#define rep(i,a) REP(i,0,a)

using namespace std;

int n,m,k;

int main(void){
    while (cin >> n >> m >> k && n) {
        int dp[n][n * m + 1];
        memset(dp,0,sizeof(dp));
        rep(i, m) dp[0][i + 1] = 1;
        REP(i, 1, n) rep(j, m * n + 1) REP(k, max(0, j - m), j) dp[i][j] += dp[i - 1][k];

        long long s = 0;
        rep(i, m * n + 1) s += dp[n - 1][i];

        double ans = 0.0;
        rep(i, m * n + 1) ans += 1.0 * dp[n - 1][i] / s * max(1, i - k);
        printf("%.10f\n", ans);
    }
    return 0;
}


