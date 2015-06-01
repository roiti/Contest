#include <iostream>
#define REP(i,a,b) for(int i = (a); i < (b); i++)
#define rep(i,a) REP(i,0,a)
using namespace std;
const int R = 20010;
int N,M,C[16],x[R],dp[R][256], inf = 1 << 28;

int main(void){
    while (1) {
        cin >> N >> M;
        if (N == 0) break;
        rep(i,R) rep(j,256) dp[i][j] = inf;
        rep(i,M) cin >> C[i];
        rep(i,N) cin >> x[i];
        
        dp[0][128] = 0;
        rep(i,N) rep(j,256) rep(k,M) {
                    int nxt = max(0, min(255,j+C[k]));
                    int cost = (x[i]-nxt)*(x[i]-nxt);
                    dp[i+1][nxt] = min(dp[i+1][nxt], dp[i][j]+cost);
        }
        
        int ans = inf;
        rep(i,256) ans = min(ans, dp[N][i]);
        cout << ans << endl;
    }
    return 0;    
}


