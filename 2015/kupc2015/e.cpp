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

int T;
double H, W;

int main(void) {
  cin >> T;
  while (T--) {
    double ans = 0.0;
    cin >> H >> W;
    rep(i, 2) {
      double x = W/2.0, y = H;
      double mx = min(W, sqrt(x * x + y * y));
      double l = 0.0,  r = W/2.0;
      while (r - l > 1e-8) {
        double ml = (2.0*l + r)/3.0;
        double mr = (l + 2.0*r)/3.0;
        double dl = (H*H - 3.0/4.0*W*W + W*ml + ml*ml)/(2*H);
        double dr = (H*H - 3.0/4.0*W*W + W*mr + mr*mr)/(2*H);
        double tmpl = min(sqrt((x - ml)*(x - ml) + y*y), sqrt(W*W + dl*dl));
        double tmpr = min(sqrt((x - mr)*(x - mr) + y*y), sqrt(W*W + dr*dr));
        if (tmpl >= tmpr) {
          if (tmpl > mx) mx = tmpl;
          r = mr;
        }
        else if (tmpr > tmpl) {
          if (tmpr > mx) mx = tmpr;
          l = ml;
        }
      }
      ans = max(ans, mx);
      swap(H, W);
    }

    printf("%.16f\n", ans);
  }
  return 0;
}
