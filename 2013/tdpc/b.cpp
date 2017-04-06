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

int A, B;
int a[1005], b[1005];
int dp[1005][1005][2];

int main(void) {
  cin.tie(0);
  ios::sync_with_stdio(false);

  cin >> A >> B;
  rep(i, A) cin >> a[i];
  rep(i, B) cin >> b[i];

  for (int i = A; i > 0; i--) {
    for (int j = B; j > 0; j--) {
      if ((A + B - i - j)%2 == 0)
        dp[i - 1][j][0] = max(dp[i - 1][j][0], dp[i][j][0] + a[A - i]);
      else
        dp[i][j - 1][1] = max(dp[i][j - 1][1], dp[i][j][1] + b[B - j]);
    }
  }
  
  int ans = 0;
  rep(i, A + 1) rep(j, B + 1) ans = max(ans, dp[i][j][0]);
  cout << ans << endl;

  return 0;
}
