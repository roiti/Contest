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
#define mp make_pair
#define double long double

int n, m;
pair<double, double> pos[300005];
int exs[300005], rots[3000005];
const double pi = 3.141592653589793238462643383279; 
int main(void) {
  cin >> n >> m;
  rep(i, n + 1) pos[i] = mp(i, 0);

  rep(i, m) {
    int x, y, z;
    cin >> x >> y >> z;
    if (x == 1) {
      exs[y] += z;
    } else {
      rots[y] += z;
    }
  }

  int ex = 0, rot = 0;
  REP(i, 1, n + 1) {
    ex += exs[i];
    rot += rots[i];
    cout << ex << " " << rot << endl;
    pos[i].first += ex;
    double bx = pos[i - 1].first, by = pos[i].second;
    double x = pos[i].first, y = pos[i].second;
    pos[i].first = bx + (x - bx)*cos(rot/180.0*pi) + (y - by)*sin(rot/180.0*pi);
    pos[i].second = by + (y - by)*cos(rot/180.0*pi) - (x - bx)*sin(rot/180.0*pi);
  }

  REP(i, 1, n + 1) {
    printf("%.12Lf %.12Lf\n", pos[i].first, pos[i].second);
  }

  return 0;
}
