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

const ll mod = (ll)1e9 + 7;
int n, k, x, b;
int a[50005];
int cnt[10];
ll dp[1005][100];

int main(void) {
  cin.tie(0);
  ios::sync_with_stdio(false);
  cin >> n >> b >> k >> x;
  rep(i, n) cin >> a[i];
  rep(i, n) cnt[a[i]]++;
  
  ll ans = 0;
  REP(i, 1, 10) {
    dp[0][i] = cnt[i];
  }

  rep(i, min(999LL, b)) {
    rep(j, 100) {
      rep(k, 10) {
        dp[i + 1][(j*10 + k)%x] = (dp[i + 1][(j*10 + k)%x] + cnt[k]*dp[i][j])%mod;
      }
    }
  }

  while (b > 1000) {
    rep(j, 100) {
      rep(k, 10) {
        dp[1001][(j*10 + k)%x] = (dp[1000][j]%mod*dp[1000][j])%mod;
      }
    }
    rep(i, 100) {
      dp[1000][i] = dp[1001][i];
    }
    b -= 1000;
  }
  return 0;
}
