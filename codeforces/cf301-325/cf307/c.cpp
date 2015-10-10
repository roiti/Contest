#include <bits/stdc++.h>
using namespace std;
typedef long long ll;

#define REP(i, a, b) for (int i = (int)(a); i < (int)(b); i++)
#define rep(i, a) REP(i, 0, a)
#define EACH(i, a) for (auto i: a)
#define ITR(x, a) for (__typeof(a.begin()) x = a.begin(); x != a.end(); x++)
#define ALL(a) (a.begin()), (a.end())
#define ISIN(a, x) (a.find(x) != a.end())

int n, m;
int a[100005], b[100005];

bool ok(ll T) {
  rep(i, n) b[i] = a[i];
  int cur = 0;

  rep(i, m) {
    ll t = T - cur - 1;
    while (t && cur < n) {
      while (t && cur < n && b[cur] == 0) {
        cur++;
        t--;
      }
      ll use = min(t, (ll)b[cur]);
      b[cur] -= (int)use;
      t -= use;
    }
  }
  while (cur < n && b[cur] == 0) cur++;
  return cur == n;
}

int main(void) {
  cin >> n >> m;
  rep(i, n) cin >> a[i];

  ll l = 0, r = 1LL << 60;
  while (r > l) {
    ll t = (r + l) / 2;
    if (ok(t)) r = t;
    else l = t + 1;
  }
  cout << l << endl;

  return 0 ;
}
