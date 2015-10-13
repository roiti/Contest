#include <bits/stdc++.h>
using namespace std;
typedef long long ll;

#define REP(i, a, b) for (int i = (int)(a); i < (int)(b); i++)
#define rep(i, a) REP(i, 0, a)
#define EACH(i, a) for (auto i: a)
#define ITR(x, a) for (__typeof(a.begin()) x = a.begin(); x != a.end(); x++)
#define ALL(a) (a.begin()), (a.end())
#define HAS(a, x) (a.find(x) != a.end())

int n;
ll a[2005][2005];
ll l[4005], r[4005];

int main(void) {
  ios::sync_with_stdio(false);
  cin >> n;
  rep(i, n) rep(j, n) {
    cin >> a[i][j];
    l[i + j] += a[i][j];
    r[2000 + i - j] += a[i][j];
  }

  int k;
  int xx[2], yy[2];
  ll ans[2] = {-1, -1};
  rep(y, n) rep(x, n) {
    k = (x + y) % 2;
    ll tmp = l[y + x] + r[2000 + y - x] - a[y][x];
    if (tmp > ans[k]) {
      ans[k] = tmp;
      xx[k] = x + 1;
      yy[k] = y + 1;
    }
  }

  cout << ans[0] + ans[1] << endl;
  cout << yy[0] << " " << xx[0] << " " << yy[1] << " " << xx[1] << endl;

  return 0;
}
