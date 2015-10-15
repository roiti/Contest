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

const ll mod = 1777777777;
ll N, K;
ll fact[800000];

ll comb(ll n, ll r) {
  if (n > mod) n = n % mod + mod;
  const int num = 800000;
  static ll rev[num + 1], revt[num + 1];
  static bool first = true;
  if (first) {
    rev[1]  = 1; REP(i, 2, num + 1) rev[i]  = rev[mod % i] * (mod - mod/i) % mod;
    revt[0] = 1; REP(i, 1, num + 1) revt[i] = revt[i - 1] * rev[i] % mod;
    first = false;
  }
  ll res = revt[r];
  rep(i, r) res = (res * (n - i) % mod) % mod;
  return res;
}

ll montmort(ll n) {
  if (n <= 1) return 0;
  if (n == 2) return 1;
  ll a1 = 0, a2 = 1, a3;
  REP(i, 3, n + 1) {
    a3 = (i - 1) * (a2 + a1) % mod;
    a1 = a2, a2 = a3;
  }
  return a2;
}
int main(void) {
  cin >> N >> K;
  ll ans = comb(N, K) * montmort(K) % mod;
  cout << ans << endl;

  return 0;
}
