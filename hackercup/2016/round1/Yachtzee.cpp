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
ll A, B;
ll C[100005];

int main(void) {
  cin >> T;
  int testcase = 0;

  while (testcase++ < T) {
    cin >> N >> A >> B;
    rep(i, N) cin >> C[i];

    ll sum = 0;
    rep(i, N) sum += C[i];

    long double ans = 0.0;

    ll S = 0, T = 0;
    rep(i, N) {
      T += C[i];
      ll x = (B - T)/sum + 1;
      ll y = (A - S + sum)/sum - 1;
      
      if (x >= 0) {
        ans += (min(B, T + x*sum) - max(A, S + x*sum))/2.0;
      }

      if (y >= 0) {
        ans += (min(B, T + y*sum) - max(A, S + y*sum))/2.0;
      }

      if (y >= x ) {
        ans += (max(0LL, y) - max(0LL, x)) * C[i]/2.0;
      }

      S += C[i];
    }

    printf("Case #%d: %.12Lf\n", testcase, ans);
  }
  return 0;
}
