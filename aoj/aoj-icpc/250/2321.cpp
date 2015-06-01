#include <iostream>
#define rep(i,a) for (int i = 0; i < (a); i++)
using namespace std;

int n, m, l, s, e;
int L[100], T[100], dp[1 << 17];

int main(void){
    while (cin >> n, n) {
        rep(i, 1 << 17) dp[i] = 0;
        rep(i, n) {
            cin >> m >> l;
            L[i] = l;
            int t = 0;
            rep(j, m) {
                cin >> s >> e;
                t |= (1 << (e-6)) - (1 << (s-6));
            }
            T[i] = t;
        }
        
        int mx = 1;
        rep(i,n) {
            rep(bit, mx) {
                if ((bit & T[i]) == 0 && dp[bit]) {
                    dp[bit | T[i]] = max(dp[bit | T[i]], dp[bit] + L[i]);
                    mx = max(mx, (bit | T[i]) + 1);
                }
                dp[T[i]] = max(dp[T[i]], L[i]);
                mx = max(mx, T[i]+1);
            }
        }
        int ans = 0;
        rep(i, 1 << 17) ans = max(ans, dp[i]);
        cout << ans << endl;
    }
    return 0;
}


