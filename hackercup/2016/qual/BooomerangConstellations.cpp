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

int T, N;
int X[2005], Y[2005];

int main(void) {
  cin >> T;
  int ncase = 1;
  while (T--) {
    cin >> N;
    rep(i, N) cin >> X[i] >> Y[i];

    int ans = 0;
    rep(i, N) {
      map<int, int> cnt;
      rep(j, N) {
        if (i == j) continue;
        int dd = (X[j] - X[i])*(X[j] - X[i]) + (Y[j] - Y[i])*(Y[j] - Y[i]);
        cnt[dd]++;
      }
      ITR(x, cnt) ans += (*x).second*((*x).second - 1)/2;
    }
    printf("Case #%d: %d\n", ncase, ans);
    ncase++;
  }
  return 0;
}
