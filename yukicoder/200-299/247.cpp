#include <bits/stdc++.h>
using namespace std;
typedef long long ll;

#define REP(i, a, b) for (int i = (int)(a); i < (int)(b); i++)
#define rep(i, a) REP(i, 0, a)
#define EACH(i, a) for (auto i: a)
#define ITR(x, a) for (__typeof(a.begin()) x = a.begin(); x != a.end(); x++)
#define ALL(a) (a.begin()), (a.end())
#define ISIN(a, x) (a.find(x) != a.end())

int C, N;
int a[105];
int dp[100005];
const int INF = 1000000000;

int main(void) {
  // breath deeply and calm down
  cin >> C;
  cin >> N;
  rep(i, N) cin >> a[i];
  rep(i, C + 1) dp[i] = INF;
  dp[0] = 0;
  rep(i, C + 1)
    rep(j, N)
      if (i - a[j] >= 0)
        dp[i] = min(dp[i], dp[i - a[j]] + 1);

  cout << (dp[C] < INF ? dp[C]:-1) << endl;

  return 0;
}
