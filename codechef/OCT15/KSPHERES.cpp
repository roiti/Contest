#include <bits/stdc++.h>
using namespace std;
typedef long long ll;

#define REP(i, a, b) for (int i = (int)(a); i < (int)(b); i++)
#define rep(i, a) REP(i, 0, a)
#define EACH(i, a) for (auto i: a)
#define ITR(x, a) for (__typeof(a.begin()) x = a.begin(); x != a.end(); x++)
#define ALL(a) (a.begin()), (a.end())

int N, M, C;
int U[100005], L[100005], cnt_u[1005], cnt_l[1005];
ll dp[1005][1005];
const ll mod = 1000000007;

ll sum(ll a[]) {
    ll res = 0;
    rep(i, C + 1) res = (res + a[i]) % mod;
    return res;
}

int main(void) {
  // breath deeply and calm down
  cin >> N >> M >> C;
  rep(i, N) scanf("%d", &U[i]);
  rep(i, M) scanf("%d", &L[i]);
  rep(i, N) cnt_u[U[i]]++;
  rep(i, M) cnt_l[L[i]]++;

  rep(i, C + 1) dp[0][i] = (ll)cnt_u[i] * cnt_l[i] % mod;

  REP(seq, 1, C + 2) {
    ll s = 0;
    REP(r, 1, C + 1) {
      s = (s + dp[seq - 1][r - 1]) % mod;
      dp[seq][r] = dp[0][r] * s % mod;
    }
  }

  REP(i, 1, C + 1) {
    cout << sum(dp[i]) << " ";
  }
  cout << endl;

  return 0;
}
