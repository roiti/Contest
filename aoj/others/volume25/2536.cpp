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

struct UnionFind {
  int g_num;
  vector<int> rank, par;
  UnionFind(int size) {
    rank.resize(size, 0); par.resize(size, 0);
    for (int i = 0; i < size; i++) par[i] = i, rank[i] = 0;
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
    } else {
      par[x] = y;
      if (rank[x] == rank[y]) rank[y]++;
    }
  }
  int find(int x) {
    if (x == par[x]) return x;
    return par[x] = find(par[x]);
  }
  int group_num() {
    return g_num;
  }
};

// O(|E|log(|V|))
template<class T>
struct Kruskal {
  int V;
  typedef pair<T, pair<int, int>> edge;
  vector<edge> es;

  Kruskal(int V_) : V(V_){};
  void add(int u, int v, T cost) {
    es.push_back({cost, {u, v}});
  }
  int exec() {
    sort(es.begin(), es.end());
    UnionFind uf(V);
    T res = 0;
    for (int i = 0; i < es.size(); i++) {
      edge e = es[i];
      int u = e.second.first, v = e.second.second;
      if (!uf.same(u, v)) {
        uf.unite(u, v);
        res += e.first;
      }
    }
    return res;
  }
};

int main(void) {
  cin.tie(0);
  ios::sync_with_stdio(false);

  int n, m;
  while (true) {
    cin >> n >> m;
    if (n == 0 && m == 0) break;
    Kruskal<int> tree(n);
    rep(i, m) {
      int s, t, c;
      cin >> s >> t >> c;
      tree.add(s, t, c);
    }
    cout << tree.exec() << endl;
  }

  return 0;
}
