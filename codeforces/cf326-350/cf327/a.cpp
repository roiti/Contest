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
int a[500005], b[500005];

int main(void) {
  cin >> n;
  rep(i, n) scanf("%d", &a[i]);
  a[n] = a[n - 1];

  ll ans = 0, cnt = 0;
  rep(i, n) {
    if (a[i] == a[i + 1]) {
      if (a[i - cnt] == 1 && a[i] == 1) {
        REP(j, i - cnt, i) a[j] = 1;
      }
      else if (a[i - cnt] == 1 && a[i] == 0) {
        REP(j, i - cnt, i - cnt/2) a[j] = 1;
        REP(j, i - cnt/2, i) a[j] = 0;
      }
      else if (a[i - cnt] == 0 && a[i] == 1) {
        REP(j, i - cnt, i - cnt/2) a[j] = 0;
        REP(j, i - cnt/2, i) a[j] = 1;
      }
      else {
        REP(j, i - cnt, i) a[j] = 0;
      }
      ans = max(ans, cnt/2);
      cnt = 0;
    }
    else {
      cnt++;
    }
  }

  cout << ans << endl;
  rep(i, n) {
    if (i < n - 1) printf("%d ", a[i]);
    else printf("%d\n", a[i]);
  }
  return 0;
}
