#include <iostream>
#define REP(i,a,b) for(int i = (a); i < (b); i++)
#define rep(i,a) REP(i,0,a)
using namespace std;

const int INF = 1 << 28;
int N, M, L, K, A, H, x, y, t;
int d[101][101], dd[101][101], c[101];

int main(void){
    while (cin >> N >> M >> L >> K >> A >> H, N) {
        rep(i, 101) rep(j, 101) d[i][j] = dd[i][j] = INF;
        rep(i, L) cin >> c[i];
        rep(i, K) {
            cin >> x >> y >> t;
            d[x][y] = d[y][x] = t;
        }
        
        rep(k, N) rep(i, N) rep(j, N) d[i][j] = min(d[i][j], d[i][k]+d[k][j]);
        
        rep(i, L) {
            dd[  0][i+1] = dd[i+1][  0] = (d[A][c[i]] <= M ? d[A][c[i]]:INF);
            dd[L+1][i+1] = dd[i+1][L+1] = (d[H][c[i]] <= M ? d[H][c[i]]:INF);
        }
        
        rep(i, L) rep(j, L) dd[i+1][j+1] = (d[c[i]][c[j]] <= M ? d[c[i]][c[j]]:INF);
        
        dd[0][L+1] = dd[L+1][0] = (d[A][H] <= M ? d[A][H]:INF);
        rep(k, L+2) rep(i, L+2) rep(j, L+2) dd[i][j] = min(dd[i][j], dd[i][k]+dd[k][j]);
        
        int time = dd[0][L+1];
        if (time < INF) cout << time + max(0, time-M) << endl;
        else cout << "Help!" << endl;
    }
    return 0;
}


