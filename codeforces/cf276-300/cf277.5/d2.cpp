#include <iostream>
#include <vector>
#define FOR(i,a,b) for(int i=(a); i<(b); i++)
#define REP(i,a) FOR(i,0,a)
using namespace std;

int main(void){
    int n,m,a,b;
    cin >> n >> m;
    vector<int> G[3001];
    REP(i,m){
        cin >> a >> b;
        G[a-1].push_back(b-1);
    }

    int path[n][n]; 
    REP(i,n) REP(j,n) path[i][j] = 0;

    REP(i,n)
        REP(j,G[i].size())
            REP(k,G[G[i][j]].size()){
                if (G[G[i][j]][k] == i) continue;
                path[i][G[G[i][j]][k]] += 1;
            }

    int ans = 0;
    REP(i,n)
        REP(j,n)
            ans +=  path[i][j]*(path[i][j]-1)/2;

    cout << ans << endl;
    return 0;
}
