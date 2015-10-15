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

const ll inf = 1LL << 40;
int n, m, Y, Z;
map<int, int> p;
map<char, int> idx;
string b;
ll dp[5005][1 << 10][11];


int main(void) {
  cin >> n >> m >> Y >> Z;
  rep(i, m) {
    char ci;
    int pi;
    cin >> ci >> pi;
    idx[ci] = i;
    p[i] = pi;
  }
  cin >> b;

  rep(i, n) rep(j, m) rep(mask, 1 << m) dp[i][mask][j] = -inf;
  rep(j, m) dp[0][0][j] = 0;
  REP(i, 1, n + 1) {
    int k = idx[b[i - 1]];
    rep(j, m) rep(mask, 1 << m) dp[i][mask][j] = dp[i - 1][mask][j];
    rep(j, m) rep(mask, 1 << m) {
      bool combo = (i > 1 && k == j && (mask & (1 << j)));
      dp[i][mask | (1 << k)][k] = max(dp[i][mask | (1 << k)][k], dp[i - 1][mask][j] + p[k] + (combo ? Y:0));
    }
  }
  rep(j, m) dp[n][(1 << m) - 1][j] += Z;

  ll ans = -inf;
  rep(mask, 1 << m) rep(j, m) {
    ans = max(ans, dp[n][mask][j]);
  }
  cout << ans << endl;

  return 0;
}
