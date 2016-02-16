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

int n, m;
int w[3005];
int dp[3005][3005][2];

int main(void) {
  cin >> n >> m;
  rep(i, n) cin >> w[i];

  rep(i, n + 1) rep(j, n) rep(k, 2) {
    if (i == 1 && k == 1) continue;
    dp[i][j][k] = -1e8;
  }

  REP(i, 1, n + 1) rep(j, n){
    dp[i][j][1] = max(dp[i - 1][(j - 1 + n)%n][0], dp[i - 1][(j - 1 + n)%n][1] + w[(j - 1 + n)%n]);
    dp[i][j][0] = max(dp[i][(j - 1 + n)%n][0], dp[i][(j - 1 + n)%n][1]);
  }
  int ans = -1e8;
  rep(i, n) rep(j, 2) ans = max(ans, dp[m - 1][i][j]);
  cout << ans << endl;

  return 0;
}
