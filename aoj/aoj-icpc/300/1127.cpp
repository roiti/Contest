#include <iostream>
#include <cmath>
#include <cstdio>
#define REP(i,a,b) for(int i = (a); i < (b); i++)
#define rep(i,a) REP(i,0,a)
using namespace std;

const int INF = 1 << 28;
int n;
double xyzr[101][4], cost[101][101];

double calc(int i,int j) {
    double d = 0.0;
    rep(k,3) d += (xyzr[i][k]-xyzr[j][k])*(xyzr[i][k]-xyzr[j][k]);
    d = sqrt(d);
    return max(0.0, d-xyzr[i][3]-xyzr[j][3]);
}

int main(void){
    while (cin >> n, n) {
        rep(i,n) rep(j,4) cin >> xyzr[i][j];
        
        rep(i,n) REP(j,i+1,n) cost[i][j] = cost[j][i] = calc(i,j);
        double mincost[n];
        bool used[n];
        rep(i,n) {
            mincost[i] = INF;
            used[i] = false;
        }
        mincost[0] = 0.0;
        double ans = 0.0;
        
        while (1) {
            int v = -1;
            rep(u,n) {
                if (!used[u] && (v == -1 || mincost[u] < mincost[v])) v = u;
            }
            if (v == -1) break;
            used[v] = true;
            ans += mincost[v];
            rep(u,n) mincost[u] = min(mincost[u], cost[u][v]);
        }
        printf("%.3f\n",ans);
    }
    return 0;
}


