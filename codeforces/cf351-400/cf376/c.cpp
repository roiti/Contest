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

int n, m, k;
int c[200005];
map<int, int> cnt[200005];

int main(void) {
  cin.tie(0);
  ios::sync_with_stdio(false);

  cin >> n >> m >> k;

  UnionFind uf(200005);
  rep(i, n) {
    int ci;
    cin >> ci;
    c[i] = ci - 1;
  };

  while (m--) {
    int l, r;
    cin >> l >> r;
    l--; r--;
    uf.unite(l, r);
  }

  rep(i, n) {
    int x = uf.find(i); 
    cnt[x][c[i]] += 1; 
  }

  ll ans = 0;
  rep(i, 200005) {
    ll s = 0, mx = 0;
    for (auto v: cnt[i]) {
      s += v.second;
      mx = max(mx, (ll)v.second);
    }
    ans += s - mx;
  }

  cout << ans << endl;

  return 0;
}
