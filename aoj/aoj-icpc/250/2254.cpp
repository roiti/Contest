#include <iostream>
#include <algorithm>
#include <string.h>
#include <stdio.h>
#define REP(i,a,b) for (int i = (a); i < (b); i++)
#define rep(i,a) REP(i,0,a)
using namespace std;

const int INF = 1 << 28;

int sp, N;
int t[16][17], dp[1 << 16];

int main(void){
    while (cin >> N && N) {
        rep(i, N) rep(j, N + 1) cin >> t[i][j];

        rep(i, 1 << N) dp[i] = INF;
        dp[0] = 0;
        rep(bit, 1 << N) {
            rep(i, N) {
                if (bit & 1 << i) continue;
                int cost = t[i][0];
                rep(j, N) if (!(bit & 1 << j) && i != j) cost = min(cost, t[i][j+1]);
                int now = bit | 1 << i;
                dp[now] = min(dp[now], dp[bit] + cost);
            }
        }
        cout << dp[(1 << N) - 1] << endl;
    }
    return 0;
}


