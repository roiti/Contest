#include <iostream>
#include <vector>
#include <utility>
#define REP(i, a, b) for(int i = (int)(a); i < (int)(b); i++)
#define rep(i, a) REP(i, 0, a)
using namespace std;
const long long inf = 1000000000L;
 
int N, M;
long long G[301][301];
vector<pair<int, int>> start;
 
int main(void){
  rep(i, 301) rep(j, 301) G[i][j] = inf;
  cin >> N >> M;
  rep(loop, M) {
    int u, v, l;
    cin >> u >> v >> l;
    u--; v--;
    if (min(u, v) == 0) {
      start.push_back(make_pair(max(u, v), l));
      continue;
    }
    G[u][v] = G[v][u] = l;
  }
  rep(k, N) rep(i, N) rep(j, N) G[i][j] = min(G[i][j], G[i][k] + G[k][j]);
  long long ans = inf;
  rep(i, start.size()) {
    int v1 = start[i].first, l1 = start[i].second;
    REP(j, i + 1, start.size()) {
      int v2 = start[j].first, l2 = start[j].second;
      ans = min(ans, l1 + G[v1][v2] + l2);
    }
  }
  cout << (ans < inf ? ans : -1) << endl;
  return 0;
}
