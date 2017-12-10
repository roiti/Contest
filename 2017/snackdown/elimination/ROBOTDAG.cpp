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

int G[1005][1005];
int T, N, M, K;
int in[105];
int u[105], v[105];
int dp[105][105];

int solve() {
  rep(i, 105) rep(j, 105) G[i][j] = 0;
  rep(i, 105) rep(j, 105) rep(k, 105) dp[i][j][k] = bitset<105>("0");
  cin >> N >> M >> K;
  rep(i, M) {
    cin >> u[i] >> v[i];
    u[i]--; v[i]--;
    in[v[i]]++;
    G[u[i]][v[i]] = 1;
  }

  rep(i, N) {
    if (G[0][i]) {
      dp[i][0] = 1;
      cnt++;
    }
  }
  
  if (cnt != K) return -1;

  rep(i, N) {
    rep(j, N) rep(k, N) used[j][k] = false;
    REP(t, 1, N) {
    rep(j, N) {
      if (v[j] == u[i])
        nxt = nxt | dp[u[j]][v[j]][t - 1];
    }
    dp[u[i]][v[i]][t] = nxt;
  }
}

int main(void) {
  cin.tie(0);
  ios::sync_with_stdio(false);

  cin >> T;
  while (T--)
      cout << solve() << endl;

  return 0;
}
