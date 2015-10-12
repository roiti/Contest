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
int l[100005];

int main(void) {
  cin >> n;
  rep(i, n) cin >> l[i];
  sort(l, l + n);
  ll ans = 0;
  ll mx = -1;
  int i = n - 1;
  while (i > 0) {
    if (l[i] - l[i - 1] <= 1) {
      if (mx == -1) {
        mx = min(l[i], l[i - 1]);
      } else {
        ans += mx * min(l[i], l[i - 1]);
        mx = -1;
      }
      i -= 2;
    } else {
      i -= 1;
    }
  }
  cout << ans << endl;

  return 0;
}
