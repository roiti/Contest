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
int N;
ll A[2005];

ll comb(ll n, ll r) {
  const int num = 5050;
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

ll H(ll n, ll r) {
  return comb(n + r - 1, r);
}

int main(void) {
  cin >> N;
  rep(i, N) cin >> A[i];
  ll ans = 1;
  int i = 0;
  REP(j, 1, N) {
    if (A[j] != -1) {
      ll n = A[j] - A[i] + 1;
      ll r = j - i - 1;
      ans = ans * H(n, r) % mod;
      i = j;
    }
  }

  cout << ans << endl;

  return 0;
}
