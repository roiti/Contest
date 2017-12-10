#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
template<typename T> using Graph = vector<vector<T>>;

#define REP(i, a, b) for (int i = (int)(a); i < (int)(b); i++)
#define rep(i, a) REP(i, 0, a)
#define EACH(i, a) for (auto i: a)
#define ITR(x, a) for (__typeof(a.begin()) x = a.begin(); x != a.end(); x++)
#define ALL(a) (a.begin()), (a.end())
#define HAS(a, x) (a.find(x) != a.end())
#define endl '\n'

const ll inf = (ll)1e9;

int n;
int w[100005];
ll dp[105][105];

ll solve(int l, int r) {
  if (r - l == 1) return 0;
  if (dp[l][r]) return dp[l][r];

  ll res = (ll)1e9;
  REP(i, l + 1, r) res = min(res, solve(l, i) + solve(i, r));

  REP(i, l, r) res += w[i];
  
  return dp[l][r] = res;
}

int main(void) {
  cin.tie(0);
  ios::sync_with_stdio(false);

  cin >> n;
  rep(i, n) cin >> w[i];

  if (n > 100) return 0;
  cout << solve(0, n) << endl;
  return 0;
}
