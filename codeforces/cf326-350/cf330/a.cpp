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

int n;
ll x[200005];

int main(void) {
  cin >> n;
  rep(i, n) cin >> x[i];

  sort(x, x + n);
  ll ans = 1e12;
  int d = (n - 2) / 2;
  rep(i, n - d - 1) {
    ans = min(ans, x[i + d + 1] - x[i]);
  }
  cout << ans << endl;

  return 0;
}
