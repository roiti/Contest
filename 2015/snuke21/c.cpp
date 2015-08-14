#include <iostream>
#include <string>
using namespace std;
#define REP(i, a, b) for(int i = (int)(a); i < (int)(b); i++)
#define rep(i, a) REP(i, 0, a)
const int R = 1 << 12;
int mask = R - 1;
int b[10010], dp[R], e[R];

int main(void) {
    int n;
    cin >> n;
    rep(i, n) {
        string s;
        cin >> s;
        rep(j, 12)
            if (s[j] == 'o') b[i] |= 1 << j;
    }
    rep(i, n) e[b[i]] = 1;

    rep(i, R) {
        int x = 0;
        REP(j, 1, R) {
            if (!e[j] || (i & j) == 0) continue;
            int t = dp[i & (j ^ mask)] + 1;
            x = max(x, t);
        }
        dp[i] = x;
    }
    cout << dp[mask] << endl;
    return 0;
}

