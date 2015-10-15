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

int N;
vector<int> edge[100005];

pair<int, int> dfs(int v, int prev, int dist) {
  pair<int, int> res = make_pair(dist, v);
  EACH(u, edge[v]) {
    if (u == prev) continue;
    res = max(res, dfs(u, v, dist + 1));
  }
  return res;
}

int main(void) {
  cin >> N;
  rep(i, N - 1) {
    int x, y;
    cin >> x >> y;
    x--; y--;
    edge[x].push_back(y);
    edge[y].push_back(x);
  }

  auto p = dfs(0, -1, 0);
  auto q = dfs(p.second, -1, 0);

  cout << p.second + 1 << " " << q.second + 1 << endl;

  return 0;
}
