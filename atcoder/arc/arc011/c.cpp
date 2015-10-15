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

const int INF = (int)1e8;
int N;
string C[1005];
int G[1005][1005], before[1005];

int diff(string &a, string &b) {
  int n = a.size();
  int res = 0;
  rep(i, n) res += (a[i] == b[i] ? 0:1);
  return res;
}

vector<int> dijkstra(int s) {
  vector<bool> used(N, false);
  vector<int> cost(N, INF);
  fill(before, before + N, -1);
  cost[s] = 0;
  while (1) {
    int v = -1;
    rep(u, N) if (!used[u] && (v == -1 || cost[u] < cost[v])) v = u;
    if (v == -1) break;
    used[v] = true;
    rep(u, N)
      if (cost[u] > cost[v] + G[v][u]) {
        cost[u] = cost[v] + G[v][u];
        before[u] = v;
      }
  }
  return cost;
}

vector<int> get_path(int t) {
  vector<int> path;
  for (;t != -1; t = before[t]) path.push_back(t);
  reverse(ALL(path));
  return path;
}

int main(void) {
  cin >> C[0] >> C[1];
  cin >> N;
  N += 2;
  REP(i, 2, N) cin >> C[i];
  rep(i, N) rep(j, N) {
    G[i][j] = (diff(C[i], C[j]) == 1 ? 1:INF);
  }

  if (C[0] == C[1]) {
    cout << 0 << endl;
    cout << C[0] << endl;
    cout << C[1] << endl;
    return 0;
  }

  vector<int> cost = dijkstra(0);
  if (cost[1] < INF) {
    vector<int> path = get_path(1);
    cout << cost[1] - 1 << endl;
    EACH(i, path) cout << C[i] << endl;
  } else {
    cout << -1 << endl;
  }

  return 0;
}
