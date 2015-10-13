#include <bits/stdc++.h>
using namespace std;
typedef long long ll;

#define REP(i, a, b) for (int i = (int)(a); i < (int)(b); i++)
#define rep(i, a) REP(i, 0, a)
#define EACH(i, a) for (auto i: a)
#define ITR(x, a) for (__typeof(a.begin()) x = a.begin(); x != a.end(); x++)
#define ALL(a) (a.begin()), (a.end())

int n;
int x[2005], y[2005];

int gcd(int a, int b) {
  while (b) swap(a %= b, b);
  return a;
}

int main(void) {
  // breath deeply and calm down
  cin >> n;
  rep(i, n) cin >> x[i] >> y[i];

  ll ans = (ll)n * (n - 1) * (n - 2) / 6;

  rep(i, n) {
    map<pair<int, int>, int> cnt;
    REP(j, i + 1, n) {
      int xx = x[j] - x[i];
      int yy = y[j] - y[i];

      int g = gcd(abs(xx), abs(yy));
      xx /= g, yy /= g;
      if (xx < 0) xx *= -1, yy *= -1;
      if (xx == 0) yy = 1;
      if (yy == 0) xx = 1;

      if (cnt.find(make_pair(xx, yy)) != cnt.end()) cnt[make_pair(xx, yy)]++;
      else cnt[make_pair(xx, yy)] = 1;
    }
    ITR(it, cnt) {
      int v = (*it).second;
      ans -= v * (v - 1) / 2;
    }
  }

  cout << ans << endl;

  return 0;
}
