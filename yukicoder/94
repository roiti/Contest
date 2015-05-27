#include <iostream>
#include <algorithm>
#include <math.h>
#define FOR(i,a,b) for(int i=(a); i<b; i++)
#define REP(i,a) FOR(i,0,a)
#define inf (1<<16)
using namespace std;

int G[1000][1000];
int N;

void warshall(){
    REP(k,N)
        REP(i,N)
            REP(j,N)
                G[i][j] = min(G[i][j],G[i][k]+G[k][j]);
}

int S(int ax, int ay, int bx, int by){
    return (bx-ax)*(bx-ax)+(by-ay)*(by-ay);
}

int main(void){
    cin >> N;
    int X[N],Y[N];
    REP(i,N) cin >> X[i] >> Y[i];
    REP(i,N){
        REP(j,N){
            if (S(X[i],Y[i],X[j],Y[j]) <= 100 ){
                G[i][j] = G[j][i] = 1;
            }else{
                G[i][j] = G[j][i] = inf;
            }
        }
    }
    warshall();
    double ans = 1.0;
    REP(i,N)
        REP(j,N)
            if (G[i][j] < inf)
                ans = max(ans,sqrt(S(X[i],Y[i],X[j],Y[j]))+2);
    printf("%.10f",ans);
    return 0;
}