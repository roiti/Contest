#include <bits/stdc++.h>
using namespace std;
typedef long long ll;

#define REP(i, a, b) for (int i = (int)(a); i < (int)(b); i++)
#define rep(i, a) REP(i, 0, a)
#define EACH(i, a) for (auto i: a)
#define ITR(x, a) for (__typeof(a.begin()) x = a.begin(); x != a.end(); x++)
#define ALL(a) (a.begin()), (a.end())

int H, W;
int C[101][101];

int main(void) {
  cin >> H >> W;
  rep(y, H) rep(x, W) cin >> C[y][x];
  rep(y, H) rep(x, W) if ((y + x) % 2 == 1) C[y][x] *= -1;

  int ans = 0;
  rep(yl, H) REP(yr, yl + 1, H + 1) {
    rep(xl, W) {
      int tmp = 0;
      int x = xl;
      while (x < W) {
	REP(y, yl, yr) tmp += C[y][x];
	if (tmp == 0) ans = max(ans, (yr - yl) * (x -xl + 1));
	x++;
      }
    }
  }

  cout << ans << endl;

  return 0;
}
