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

int root = 0;
int n;
vector<int> c[100005];
const int K = 20;
int parent[K][100005];
int depth[100005];

void bfs(int v, int p, int d) {
  queue<tuple<int, int, int>> que;
  que.push(make_tuple(v, p, d));
  while (!que.empty()) {
    auto ele = que.front(); que.pop();
    int vv = get<0>(ele), pp = get<1>(ele), dd = get<2>(ele);
    parent[0][vv] = pp;
    depth[vv] = dd;
    for (auto i: c[vv]) {
      que.push(make_tuple(i, vv, dd + 1));
    }
  }
}

void init() {
  bfs(root, -1, 0);
  for (int k = 0; k + 1 < K; k++) {
    for (int v = 0; v < n; v++) {
      if (parent[k][v] < 0) parent[k + 1][v] = -1;
      else parent[k + 1][v] = parent[k][parent[k][v]];
    }
  }
}

int lca(int u, int v) {
  if (depth[u] > depth[v]) swap(u, v);
  for (int k; k < K; k++) {
    if ((depth[v] - depth[u] >> k & 1)) {
      v = parent[k][v];
    } 
    if (u == v) return u;
  }
  for (int k = K - 1; k >= 0; k--) {
    if (parent[k][u] != parent[k][v]) {
      u = parent[k][u];
      v = parent[k][v];
    }
  }
  return parent[0][u];
}

int main(void) {
  cin.tie(0);
  ios::sync_with_stdio(false);

  cin >> n;
  rep(i, n) {
    int k;
    cin >> k;
    rep(j, k) {
      int cj;
      cin >> cj;
      c[i].push_back(cj);
    }
  }

  init();

  int q;
  cin >> q;
  rep(i, q) {
    int u, v;
    cin >> u >> v;
    cout << lca(u, v) << endl;
  }

  return 0;
}
