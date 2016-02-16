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

const int inf = (int)1e7;
int n;
int p[100005];
int dp[100005];

int main(void) {
  cin >> n;
  rep(i, n) cin >> p[i];
  rep(i, n) dp[i] = inf;
  
  rep(i, n) {
    *lower_bound(dp, dp + n, p[i]) = p[i];
  }

  cout << n - (lower_bound(dp, dp + n, inf) - dp) << endl;

  return 0;
}
