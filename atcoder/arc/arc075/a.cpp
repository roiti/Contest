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

int N;
int s[105];
int dp[10005];

int main(void) {
  cin.tie(0);
  ios::sync_with_stdio(false);

  cin >> N;
  rep(i, N) cin >> s[i];

  rep(i, N) {
      for (int j = 10000; j >= 0; j--){
          if (dp[j] > 0) dp[j + s[i]] = 1;
      }
      dp[s[i]] = 1;
  }

  int ans = 0;
  rep(i, 10005) if (dp[i] && i%10 != 0) ans = i;

  cout << ans << endl;

  return 0;
}
