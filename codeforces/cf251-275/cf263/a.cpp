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
int a[300005];

int main(void) {
  cin >> n;
  rep(i, n) scanf("%d", &a[i]);
  sort(a, a + n);
  ll s = 0;
  rep(i, n) s += a[i];
  ll ans = 0;
  int away = 0;
  rep(i, n) {
    ans += s + away;
    s -= a[i];
    away = a[i];
  }

  cout << ans << endl;

  return 0;
}
