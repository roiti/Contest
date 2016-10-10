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

template<typename T> T gcd(T a, T b) {
  while (b) swap(a %= b, b);
  return a;
}

template<typename T> T extgcd(T a, T b, T& x, T& y) {
  T res = a;
  if (b == 0) {
    x = 1;
    y = 0;
  } else {
    res = extgcd(b, a % b, y, x);
    y -= (a / b) * x;
  }
  return res;
}

pair<ll, ll> crt(ll a0, ll m0, ll a1, ll m1) {
  ll g = gcd(m0, m1);
  if (a0%g != a1%g) return {-1, -1};
  if (g > 1) {
    m0 /= g, m1 /= g;
    while (true) {
      ll gt = gcd(m0, g);
      if (gt == 1) break;
      m0 *= gt;
      g /= gt;
    }
    m1 *= g;
    a0 %= m0, a1 %= m1;
  }
  ll x, y;
  g = extgcd(m0, m1, x, y);
  ll mod = m0*m1;
  ll res = a0*(y + mod)%mod*m1 + a1*(x + mod)%mod*m0;
  return {res%mod, mod};
}

pair<ll, ll> crt(vector<ll> a, vector<ll> m) {
  ll res = 0, mod = 1;
  for (int i = 0; i < a.size(); i++) {
    tie(res, mod) = crt(res, mod, a[i], m[i]);
    if (res == -1) return {-1, -1};
  }
  return {res, mod};
}

int n, m, k;

int main(void) {
  cin.tie(0);
  ios::sync_with_stdio(false);

  cin >> n >> m >> k;
  while (k--) {
    ll x, y;
    cin >> x >> y;
    ll ans = -1;
    ll X[] = {x, x, 2*n - x, 2*n - x};
    ll Y[] = {y, 2*m - y, 2*m - y, y};
    rep(i, 4) {
      ll res = 0, mod = 1;
      tie(res, mod) = crt(X[i], 2*n, Y[i], 2*m);
      if (res == -1) continue;
      if (ans == -1) ans = res;
      else ans = min(ans, res);
    }
    cout << ans << endl;
  }

  return 0;
}
