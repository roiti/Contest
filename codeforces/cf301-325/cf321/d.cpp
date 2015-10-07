#include <bits/stdc++.h>
using namespace std;
typedef long long ll;

#define REP(i, a, b) for (int i = (int)(a); i < (int)(b); i++)
#define rep(i, a) REP(i, 0, a)
#define EACH(i, a) for (auto i: a)
#define ITR(x, a) for (__typeof(a.begin()) x = a.begin(); x != a.end(); x++)
#define ALL(a) (a.begin()), (a.end())

int n, m, k;
int a[18], c[18][18];
const ll INF = 0x3f3f3f3f;
ll dp[1 << 18][18];

int main(void) {
  // breath deeply and calm down
  cin >> n >> m >> k;
  rep(i, n) cin >> a[i];

  rep(i, k) {
    int x, y;
    cin >> x >> y;
    x--; y--;
    cin >> c[x][y];
  }

  rep(mask, 1 << n) rep(i, n) dp[mask][i] = -INF;
  rep(i, n) dp[1 << i][i] = a[i];

  rep(mask, 1 << n) rep(i, n) {
    rep(j, n)
      if (!(mask >> j & 1))
          dp[mask | (1 << j)][j] = max(dp[mask | (1 << j)][j], dp[mask][i] + a[j] + c[i][j]);
  }

  ll ans = 0;
  rep(mask, 1 << n) rep(i, n)
      if (__builtin_popcount(mask) == m)
          ans = max(ans, dp[mask][i]);

  cout << ans << endl;

  return 0;
}
