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
int a[10000];

int calc(int l, int r, int h) {
  if (l > r) return 0;

  int mn = 1000000010;
  REP(i, l, r + 1) mn = min(mn, a[i]);

  int res = mn - h;
  int pre = -1;
  REP(i, l, r + 2) {
    if (a[i] > mn && pre == -1) pre = i;
    if (a[i] <= mn && pre >= 0) {
      res += calc(pre, i - 1, mn);
      pre = -1;
    }
  }
  return min(res, r - l + 1);
}

int main(void) {
  cin >> n;
  rep(i, n) cin >> a[i];

  cout << calc(0, n - 1, 0) << endl;
  return 0;
}
