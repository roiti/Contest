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

int N, M;
int a[200005], b[200005], y[200005];
int Q;
int v[100005], w[100005];
int ans[100005];

struct UnionFind {
  int g_num;
  vector<int> rank, par, g;
  UnionFind(int size) {
    rank.resize(size, 0); par.resize(size, 0); g.resize(size, 0);
    for (int i = 0; i < size; i++) par[i] = i, rank[i] = 0, g[i] = 1;
    g_num = size;
  }
  bool same(int x, int y) {
    return find(x) == find(y);
  }
  void unite(int x, int y) {
    x = find(x); y = find(y);
    if (x == y) return;
    g_num--;
    if (rank[x] > rank[y]) {
      par[y] = x;
      g[x] += g[y];
    } else {
      par[x] = y;
      g[y] += g[x];
      if (rank[x] == rank[y]) rank[y]++;
    }
  }
  int find(int x) {
    if (x == par[x]) return x;
    return par[x] = find(par[x]);
  }
  int group(int x) {
    if (x == par[x]) return g[x];
    return group(par[x]);
  }
  int group_num() {
    return g_num;
  }
};

int main(void) {
  cin.tie(0);
  ios::sync_with_stdio(false);

  cin >> N >> M;
  rep(i, M) cin >> a[i] >> b[i] >> y[i];
  cin >> Q;
  rep(i, Q) cin >> v[i] >> w[i];

  priority_queue<tuple<int, int, int>> road_que, man_que;
  rep(i, M) road_que.push(make_tuple(y[i], a[i] - 1, b[i] - 1));
  rep(i, Q) man_que.push(make_tuple(w[i], i, v[i] - 1));
  UnionFind uf(N);

  for (int year = 200005; year >= 0; year--) {
    while (!man_que.empty() && year == get<0>(man_que.top())) {
      auto ele = man_que.top(); man_que.pop();
      int wi = get<0>(ele), i = get<1>(ele), vi = get<2>(ele);
      ans[i] = uf.group(vi);
    }

    while (!road_que.empty() && year == get<0>(road_que.top())) {
      auto ele = road_que.top(); road_que.pop();
      int yi = get<0>(ele), ai = get<1>(ele), bi = get<2>(ele); 
      uf.unite(ai, bi);
    }
  }

  rep(i, Q) cout << ans[i] << endl;

  return 0;
}
