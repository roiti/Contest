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

int N;
int a[105][105];
int dp[105][105];

int main(void) {
  cin.tie(0);
  ios::sync_with_stdio(false);

  cin >> N;
  rep(i, N) rep(j, i + 1) cin >> a[i][j];
  
  dp[0][0] = a[0][0];
  REP(i, 1, N) {
    rep(j, i + 1) {
      if (j > 0) 
        dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - 1]) + a[i][j];
      else
        dp[i][j] = dp[i - 1][j] + a[i][j];
    }
  }

  int ans = 0;
  rep(i, N) ans = max(ans, dp[N - 1][i]);

  cout << ans << endl;

  return 0;
}
