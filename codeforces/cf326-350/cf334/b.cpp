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

const ll mod = (ll)1e9 + 7;
ll k, p;

class UnionFind {
 public:
    int g_num;
    vector<int> rank, par;

    UnionFind() {}
    UnionFind(int size) {
        rank.resize(size, 0);
        par.resize(size, 0);
        for (int i = 0; i < size; i++) {
            par[i] = i;
            rank[i] = 0;
        }
        g_num = size;
    }

    bool same(int x, int y) {
        return find(x) == find(y);
    }

    void unite(int x, int y) {
        x = find(x);
        y = find(y);
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

int main(void) {
  cin >> p >> k;
  ll ans = 1;
  if (k == 0) {
    rep(i, p - 1) ans = ans * p % mod;
    cout << ans << endl;
    return 0;
  }

  UnionFind uf(p);
  int cnt = 0;
  rep(x, p) {
    if (x == k*x%p) {
      if (k > 1) cnt += 1;
    }
    else {
      uf.unite(x, k*x % p);
    }
  }

  rep(i, uf.group_num() - cnt) ans = (ans * p) % mod;
  cout << ans << endl;

  return 0;
}
