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
#define double long double

int n;
double prob[100005];
ll p;
ll l[100005], r[100005];

int main(void) {
  cin.tie(0);
  ios::sync_with_stdio(false);
  cin >> n >> p;
  rep(i, n) cin >> l[i] >> r[i];
  
  rep(i, n) prob[i] = (double)(r[i]/p - (l[i] - 1)/p)/(r[i] - l[i] + 1);
//  rep(i, n) cout << prob[i] << " ";
//  cout << endl;

  double ans = 0;
  rep(i, n) {
    ans += 2000 - 2000*(1 - prob[i])*(1 - prob[(i + 1)%n]);
  }

  cout << setprecision(10) << ans << endl;

  return 0;
}
