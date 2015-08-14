#include <iostream>
#include <algorithm>
#define FOR(i,a,b) for(int i=(a); i<(b); i++)
#define REP(i,a) FOR(i,0,a)
#define inf (1<<27)
using namespace std;
 
const int MAXN = 301;
int N,M,a,b,t;
int G[MAXN][MAXN];
 
void warshall_floyd(){
  REP(k,N) REP(i,N) REP(j,N)
    G[i][j]= min(G[i][j], G[i][k]+G[k][j]);
}
 
int main(void){
  REP(i,MAXN) REP(j,MAXN) G[i][j] = (i == j ? 0:inf);
  cin >> N >> M;
  REP(i,M){
    cin >> a >> b >> t;
    a--; b--;
    G[a][b] = G[b][a] = t;
  }
    
  warshall_floyd();
    
  int ans = inf;
  REP(i,N){
    int tmp = 0;
    REP(j,N)
      tmp = max(tmp,G[i][j]);
    ans = min(ans,tmp);
  }
  cout << ans << endl;
  return 0;
}
