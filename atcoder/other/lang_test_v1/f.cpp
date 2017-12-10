#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
 
#define REP(i, a, b) for (int i = (int)(a); i < (int)(b); i++)
#define rep(i, a) REP(i, 0, a)
#define EACH(i, a) for (auto i: a)
#define ITR(x, a) for (__typeof(a.begin()) x = a.begin(); x != a.end(); x++)
#define ALL(a) (a.begin()), (a.end())
#define HAS(a, x) (a.find(x) != a.end())
#define endl '\n'
 
const int INF = 100000000;
int N;
int x[1001], y[1001], t[1001], r[1001];
double G[1001][1001];
 
double dist(int x1, int y1, int x2, int y2) {
  return sqrt((x1 - x2) * (x1 - x2) + (y1 - y2) * (y1 - y2));
}
 
vector<double> dijkstra(int s) {
  vector<bool> used(N, false);
  vector<double> cost(N, INF);
  cost[s] = 0.0;
 
  while (1) {
    int v = -1;
    rep(u, N) if (!used[u] && (v == -1 || cost[u] < cost[v] )) v = u;
 
    if (v == -1) break;
    used[v] = true;
 
    rep(u, N) cost[u] = min(cost[u], cost[v] + G[v][u]);
  }
  return cost;
}
 
int main(void) {
  cin >> N;
  rep(i, N) cin >> x[i] >> y[i] >> t[i] >> r[i];
  rep(i, N) rep(j, N) {
    G[i][j] = dist(x[i], y[i], x[j], y[j]) / min(t[i], r[j]);
  }
 
  vector<double> cost = dijkstra(0);
  sort(ALL(cost));
 
  double ans = 0;
  REP(i, 1, N) ans = max(ans, cost[i] + N - i - 1);
  printf("%.10f\n", ans);
 
  return 0;
}
