#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
template<typename T> using Graph = vector<vector<T>>;

#define REP(i, a, b) for (int i = (int)(a); i < (int)(b); i++)
#define rep(i, a) REP(i, 0, a)
#define EACH(i, a) for (auto i: a)
#define ITR(x, a) for (__typeof(a.begin()) x = a.begin(); x != a.end(); x++)
#define ALL(a) (a.begin()), (a.end())
#define HAS(a, x) (a.find(x) != a.end())
#define endl '\n'
#define to first
#define cost second

int n;
bool used[100005];
vector<pair<int, int>> tr[100005];

pair<int, int> dfs1(int s, int d) {
  used[s] = true;
  pair<int, int> res = {s, d};
  for (auto p: tr[s]) {
    if (used[p.to]) continue;
    auto tp = dfs1(p.to, d + p.cost);
    if (tp.cost > res.cost) res = tp;
  }
  return res;
}

int dfs2(int s) {
  used[s] = true;
  int res = 0;
  for (auto p: tr[s]) {
    if (used[p.to]) continue;
    res = max(res, dfs2(p.to) + p.cost);
  }
  return res;
}

int diameter() {
  auto p = dfs1(0, 0);
  rep(i, n) used[i] = false;
  return dfs2(p.to);
}

int main(void) {
  cin.tie(0);
  ios::sync_with_stdio(false);

  cin >> n;
  rep(i, n - 1) {
    int s, t, w;
    cin >> s >> t >> w;
    tr[s].push_back({t, w});
    tr[t].push_back({s, w});
  }

  cout << diameter() << endl;

  return 0;
}
