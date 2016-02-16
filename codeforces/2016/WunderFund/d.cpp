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

int n;
ll x, y;
vector<int> G[200005];
bool used[200005];

typedef pair<int, int> Res;
Res dfs(int p, int v) {
  used[v] = true;
  Res r(0, v);
  for (auto e: G[v]) {
    if (used[e]) continue;
    Res t = dfs(v, e);
    t.first += 1;
    if (r.first < t.first) r = t;
  }
  return r;
}

int main(void) {
  cin >> n >> x >> y;
  rep(i, n - 1) {
    int u, v;
    cin >> u >> v;
    u--; v--;
    G[u].push_back(v);
    G[v].push_back(u);
  }

  Res r = dfs(-1, 0);
  rep (i, n) used[i] = false;
  Res t = dfs(-1, r.second);

  //cout << t.first << endl;
  if (x < y) {
    cout << x*(t.first) + y*(n - t.first - 1) << endl;
  } else {
    cout << y*(n - 1) << endl;
  }
  return 0;
}
