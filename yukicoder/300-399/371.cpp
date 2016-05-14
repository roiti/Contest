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

ll L, H;

bool isprime(ll n) {
  if (n < 2) return false;
  if (n == 2) return true;
  if (n % 2 == 0) return false;
  for (ll i = 3; i * i <= n; i += 2)
    if (n % i == 0) return false;
  return true;
}

ll min_factor(ll N) {
  if (N == 2) return -1;
  if (N % 2 == 0) return 2;
  ll x = 3;
  while (x*x <= N) {
    if (N % x == 0) {
      return x;
    }
    x += 2;
  }
  return -1;
}

int main(void) {
  cin.tie(0);
  ios::sync_with_stdio(false);

  cin >> L >> H;

  ll ans = -1, mx = -1;

  ll s = (ll)sqrt(H);
  while (s > 1) {
    if (isprime(s)) {
      ll t = H/s;
      while (!isprime(t)) t--;
      if (L <= t*s) {
        mx = s;
        ans = t*s;
        break;
      }
    }
    s -= 1;
  }

  for (ll x = H; x >= max(L, H - (ll)1e4); x--) {
    ll val = min_factor(x);
    if (val > mx) {
      mx = val;
      ans = x;
    }
    if (val == mx) {
      ans = max(ans, x);
    }
  }

  cout << ans << endl;

  return 0;
}
