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

double pi = 3.14159265358979;
int n, R, v;
double s, f;

double half(double d) {
  double l = 0, r = 2*pi;
  rep(i, 60) {
    double m = (l + r)/2;
    if (m + sin(m) > d) {
      r = m;
    } else {
      l = m;
    }
  }
  return r;
}

int main(void) {
  cin >> n >> R >> v;
  double w = 2*R*pi;
  while (n--) {
    cin >> s >> f;
    double d = f - s;
    int k = d/w;
    d -= k*w;
    double theta = half(d/w*pi);
    double ans = k*w/v + w/v*theta/pi;
    printf("%.8lf\n", ans);
  }

  return 0;
}
