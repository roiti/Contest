#include <bits/stdc++.h>
using namespace std;
typedef long long ll;

#define REP(i, a, b) for (int i = (int)(a); i < (int)(b); i++)
#define rep(i, a) REP(i, 0, a)
#define EACH(i, a) for (auto i: a)
#define ITR(x, a) for (__typeof(a.begin()) x = a.begin(); x != a.end(); x++)
#define ALL(a) (a.begin()), (a.end())
#define ISIN(a, x) (a.find(x) != a.end())

int N, S, K;
const ll mod = 1000000007;
ll dp[105][20005];

int main(void) {
  cin >> N >> S >> K;
  for (int i = 0; i < S + N; i += N) dp[1][i] = 1;
  REP(i, 2, N + 1) {
    int m = N + 1 - i;
    rep(j, S + 1) {
      if (j >= K * m) dp[i][j] = (dp[i][j] + dp[i - 1][j - K * m]) % mod;
      if (j >= m)     dp[i][j] = (dp[i][j] + dp[i][j - m]) % mod;
    }
  }

  cout << dp[N][S] << endl;

  return 0;
}
