#include <bits/stdc++.h>
using namespace std;
typedef long long ll;

#define REP(i, a, b) for (int i = (int)(a); i < (int)(b); i++)
#define rep(i, a) REP(i, 0, a)
#define EACH(i, a) for (auto i: a)
#define ITR(x, a) for (__typeof(a.begin()) x = a.begin(); x != a.end(); x++)
#define ALL(a) (a.begin()), (a.end())

const ll MOD = 1000000007;
const int MX = 100005;

int N;
ll dp[5][MX];

int main(void) {
  cin >> N;
  rep(i, N) {
    int d;
    cin >> d;
    dp[0][d] = dp[1][d] = dp[2][d] = ++dp[3][d];
  }

  REP(i, 1, 5) {
    REP(j, 1, MX) dp[i - 1][j] = (dp[i - 1][j] + dp[i - 1][j - 1]) % MOD;
    REP(j, 1, MX) dp[i][j] = (dp[i][j] * dp[i - 1][j / 2]) % MOD;
  }

  cout << dp[3][MX - 1] << endl;
    
  return 0;
}
