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
  vector<int> rank, par, g_size;
  UnionFind(int size) {
    rank.resize(size, 0); par.resize(size, 0); g_size.resize(size, 1);
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
      g_size[x] += g_size[y];
    } else {
      par[x] = y;
      g_size[y] += g_size[x];
      if (rank[x] == rank[y]) rank[y]++;
    }
  }
  int find(int x) {
    if (x == par[x]) return x;
    return par[x] = find(par[x]);
  }
  int group_size(int x) {
    x = find(x);
    return g_size[x];
  }
  int group_num() {
    return g_num;
  }
};

int N, M, Q;
int a[100005], b[100005], ans[100005];
vector<UnionFind> ufs;

UnionFind get_uf(int k) {
  UnionFind res = ufs[k/100];
  for (int i = k/100*100; i <= k; i++) {
    res.unite(a[i], b[i]);
  }
  return res;
}

int solve(int x, int y, int z) {
  int lo = 1, hi = M;
  int res = M;
  while (hi - lo >= 0) {
    int mi = (lo + hi)/2;
    UnionFind uf = get_uf(mi - 1);
    int num = 0;
    if (uf.same(x, y)) {
      num = uf.group_size(x); 
    } else {
      num = uf.group_size(x) + uf.group_size(y);
    }
  
    if (num >= z) {
      res = min(res, mi);
      hi = mi - 1;
    } else {
      lo = mi + 1;
    }
  }
  return res;
}

int main(void) {
  cin.tie(0);
  ios::sync_with_stdio(false);

  cin >> N >> M;
  rep(i, M) {
    cin >> a[i] >> b[i];
    a[i]--; b[i]--;
  }

  UnionFind uf(N);
  rep(i, M) {
    uf.unite(a[i], b[i]);
    if (i % 100 == 0) ufs.push_back(uf);
  }

  cin >> Q;
  while (Q--) {
    int x, y, z;
    cin >> x >> y >> z;
    x--; y--;
    cout << solve(x, y, z) << endl;
  }

  return 0;
}
