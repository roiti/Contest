#include <bits/stdc++.h>
using namespace std;
typedef long long ll;

#define REP(i, a, b) for (int i = (int)(a); i < (int)(b); i++)
#define rep(i, a) REP(i, 0, a)
#define EACH(i, a) for (auto i: a)
#define ITR(x, a) for (__typeof(a.begin()) x = a.begin(); x != a.end(); x++)
#define ALL(a) (a.begin()), (a.end())
#define HAS(a, x) (a.find(x) != a.end())

int N, T;
int A[51];
bool dp[51][100005];

int main(void) {
  cin >> N;
  cin >> T;
  rep(i, N) cin >> A[i];
  rep(i, N) rep(j, T + 1) dp[i][j] = false;
  dp[N][T] = true;
  for (int i = N - 1; i > -1; i--) rep(j, T + 1) {
    if (j * A[i] <= T && dp[i + 1][j * A[i]]) dp[i][j] = true;
    if (j + A[i] <= T && dp[i + 1][j + A[i]]) dp[i][j] = true;
  }

  string ans;
  int c = A[0];
  REP(i, 1, N) {
    if (dp[i + 1][c + A[i]]) {
      ans += "+";
      c += A[i];
    } else {
      ans += "*";
      c *= A[i];
    }
  };
  cout << ans << endl;
  return 0;
}
