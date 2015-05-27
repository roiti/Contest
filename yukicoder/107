#include <iostream>
#define rep(i,a) for(int i = 0; i < (a); i++)
using namespace std;

int N, D[17], dp[1 << 17];

int bitcount(int n) {
    int res = 0;
    for(; n; n /= 2) res += n%2;
    return res;
}

int main(void){
    cin >> N;
    rep(i, N) cin >> D[i];
    
    int bad = 0;
    rep(i, N) if (D[i] < 0) bad |= 1 << i;
    
    dp[0] = 100;
    rep(bit, 1 << N) {
        rep(i, N) {
            if (dp[bit] == 0 || bit & 1 << i) continue;
            int beat = bitcount(bit & bad);
            dp[bit | 1 << i] = max(dp[bit | 1 << i], min(100*(beat+1), dp[bit]+D[i]));
        }
    }
    cout << dp[(1 << N)-1] << endl;
    return 0;
}
