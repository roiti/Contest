#include <iostream>
#define rep(i,a) for (int i = 0; i < (a); i++)
using namespace std;
int const INF = 1 << 28;
int n, m, s, g1, g2, b1, b2, c;
int G[101][101];

int main(void){
    while (cin >> n >> m >> s >> g1 >> g2, n) {
        s--, g1--, g2--;
        rep(i, 101) rep(j, 101) G[i][j] = (i == j ? 0:INF);
        rep(i, m) {
            cin >> b1 >> b2 >> c;
            G[b1-1][b2-1] = c;
        }
        rep(k, n) rep(i, n) rep(j, n) G[i][j] = min(G[i][j], G[i][k]+G[k][j]);
        int ans = INF;
        rep(i, n) {
            ans = min(ans, G[s][i]+G[i][g1]+G[i][g2]);
            ans = min(ans, G[s][i]+G[i][g1]+G[g1][g2]);
            ans = min(ans, G[s][i]+G[i][g2]+G[g2][g1]);
        }
        cout << ans << endl;
    }
    return 0;
}


