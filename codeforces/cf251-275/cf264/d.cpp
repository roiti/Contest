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

int n, k;
int a[1005], ok[1005][1005];
int memo[1005];

int dfs(int cur) {
  if (memo[cur] > -1) return memo[cur];
  memo[cur] = 1;
  rep(i, n) if (ok[cur][i]) memo[cur] = max(memo[cur], 1 + dfs(i));
  return memo[cur];
}

int main(void) {
  cin >> n >> k;
  rep(i, n) rep(j, n) ok[i][j] = 1;
  rep(i, n) ok[i][i] = 0;
  rep(j, k) {
    rep(i, n) cin >> a[i], a[i]--;
    rep(x, n) REP(y, x + 1, n) ok[a[y]][a[x]] = 0;
  }

  rep(i, n) memo[i] = -1;
  int ans = 0;
  rep(i, n) ans = max(ans, dfs(i));
  cout << ans << endl;

  return 0;
}
