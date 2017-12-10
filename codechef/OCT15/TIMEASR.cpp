#include <bits/stdc++.h>
using namespace std;
typedef long long ll;

#define REP(i, a, b) for (int i = (int)(a); i < (int)(b); i++)
#define rep(i, a) REP(i, 0, a)
#define EACH(i, a) for (auto i: a)
#define ITR(x, a) for (__typeof(a.begin()) x = a.begin(); x != a.end(); x++)
#define ALL(a) (a.begin()), (a.end())

int main(void) {
  // breath deeply and calm down
  int T;
  cin >> T;
  while (T--) {
    double A;
    scanf("%lf", &A);
    vector<string> ans;
    rep(h, 12) rep(m, 60) {
      double rh = 30 * h + 30 * m / 60.0;
      double rm = 6 * m;
      double rd = abs(rh - rm);
      if (rd > 180.0) rd = 360.0 - rd;
      if (abs(rd - A) <= 1/120.0 + 1e-6) {
        char t[6];
        sprintf(t, "%02d:%02d", h, m);
        string time(t);
        ans.push_back(time);
      } 
    }
    sort(ALL(ans));
    EACH(line, ans) printf("%s\n", line.c_str());
  }
  return 0;
}
