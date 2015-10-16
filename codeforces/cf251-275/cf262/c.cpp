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

int n, m, w;
ll a[100005], s[200005];

bool ok(ll h) {
  rep(i, 200005) s[i] = 0;
  ll mm = m;
  ll d = 0;
  rep(i, n) {
    d -= s[i];
    if (a[i] + d < h) {
      ll k = h - (a[i] + d);
      s[i + w] = k;
      d += k;
      mm -= k;
    }
  }
  return mm >= 0;
}

int main(void) {
  cin >> n >> m >> w;
  rep(i, n) cin >> a[i];

  ll l = 0, r = 3000000000;
  while (r >= l) {
    ll m = (l + r) / 2;
    if (!ok(m)) r = m - 1;
    else l = m + 1;
  }

  cout << r << endl;

  return 0;
}
