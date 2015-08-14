#include <iostream>
#define REP(i,a,b) for (int i = (int)(a); i < (int)(b); i++)
#define rep(i,a) REP(i,0,a)
using namespace std;
typedef long long ll;

int n, m, b, mod;
int a[501], dp[510][510];

int main(void){
    cin >> n >> m >> b >> mod;
    rep(i, n) cin >> a[i];

    dp[0][0] = 1;
    
    rep(i, n)
        REP(j, 1, m + 1)
            REP(k, a[i], b + 1)
                dp[j][k] = (dp[j][k] + dp[j - 1][k - a[i]]) % mod;

    int ans = 0;
    rep(i, b + 1) ans = (ans + dp[m][i]) % mod;
    cout << ans << endl;
    
    return 0;
}
