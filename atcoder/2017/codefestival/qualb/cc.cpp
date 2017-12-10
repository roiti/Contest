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
int A[100005], B[100005];
set<int> G[100005], H[100005];
bool used[100005];

void dfs(int s, int t) {
  for (auto v: H[t]) {
    if (HAS(G[s], v) || v == s) continue;
    G[s].insert(v);
    G[v].insert(s);
    dfs(s, v);
  }
}

int main(void) {
  cin.tie(0);
  ios::sync_with_stdio(false);

  cin >> N >> M;
  rep(i, M) {
    cin >> A[i] >> B[i];
    A[i]--; B[i]--;
    G[A[i]].insert(B[i]);
    G[B[i]].insert(A[i]);
  }

  rep(i, N) {
    for (auto v: G[i]) {
      for (auto u: G[v]) {
        if (HAS(G[i], u) || u == i) continue;
        H[i].insert(u);
      }
    }
  }

  rep(i, N) {
    for (auto j: G[i]) {
      dfs(i, j);
    }
  }

  int ans = 0;
  rep(i, N) ans += G[i].size();
  ans = ans/2 - M;

  cout << ans << endl;

  return 0;
}
