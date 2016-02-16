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

int N, M, L;
ll A[10005], B[10005];
ll C[1005], D[1005];
ll dp[10005];

int main(void) {
  cin >> N >> M >> L;
  rep(i, N) cin >> A[i] >> B[i];
  rep(i, M) cin >> C[i] >> D[i];

  ll ans = 0;
  rep(i, N) dp[A[i]] = max(dp[A[i]], B[i]);
  rep(i, M) {
    for (int j = L; j >= C[i]; j--){
      if (dp[j - C[i]]) dp[j] = max(dp[j], dp[j - C[i]] + D[i]);
    }
  }

  rep(i, L + 1) ans = max(ans, dp[i]);

  cout << ans << endl;
  return 0;
}
