#include <bits/stdc++.h>
using namespace std;
typedef long long ll;

#define REP(i, a, b) for (int i = (int)(a); i < (int)(b); i++)
#define rep(i, a) REP(i, 0, a)
#define EACH(i, a) for (auto i: a)
#define ITR(x, a) for (__typeof(a.begin()) x = a.begin(); x != a.end(); x++)
#define ALL(a) (a.begin()), (a.end())

const int NMAX = 100005;
const int AMAX = 100005;
int n;
int a[NMAX], need[AMAX], cnt[AMAX];

void rec(int m, int step, bool up, int rem) {
  if (m >= AMAX) return;
  need[m] += step;
  cnt[m]++;
  if (up)
    rec(2 * m, step + 1, true, 0);
  else {
    if (rem == 1) rec(2 * m, step + 1, true, 0);
    if (m > 1)    rec(m / 2, step + 1, false, m % 2);
  }
}

int main(void) {
  cin >> n;
  rep(i, n) cin >> a[i];

  rep(i, n) rec(a[i], 0, false, 1);

  int ans = NMAX * 100;
  rep(i, AMAX) {
    if (cnt[i] == n)
      ans = min(ans, need[i]);
  }

  cout << ans << endl;
  return 0;
}
