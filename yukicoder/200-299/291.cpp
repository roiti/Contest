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

string S;
int dp[102][22][22][22][22];

inline void update(int &a, int b) {
  a = max(a, b);
}

int main(void) {
  cin >> S;
  int N = S.size();
  memset(dp, -1, sizeof(dp));
  dp[0][0][0][0][0] = 0;
  rep(i, N) rep(k, 21) rep(u, 21) rep(r, 21) rep(o, 21) {
    if (dp[i][k][u][r][o] == -1) continue;
    update(dp[i + 1][k][u][r][o], dp[i][k][u][r][o]);
    if (S[i] == 'K' || S[i] == '?') update(dp[i + 1][k + 1][u][r][o], dp[i][k][u][r][o]);
    if ((S[i] == 'U' || S[i] == '?') && k) update(dp[i + 1][k - 1][u + 1][r][o], dp[i][k][u][r][o]);
    if ((S[i] == 'R' || S[i] == '?') && u) update(dp[i + 1][k][u - 1][r + 1][o], dp[i][k][u][r][o]);
    if ((S[i] == 'O' || S[i] == '?') && r) update(dp[i + 1][k][u][r - 1][o + 1], dp[i][k][u][r][o]);
    if ((S[i] == 'I' || S[i] == '?') && o) update(dp[i + 1][k][u][r][o - 1], dp[i][k][u][r][o] + 1);
  }

  int ans = 0;
  rep(k, 21)rep(u, 21) rep(r, 21) rep(o, 21) update(ans, dp[N][k][u][r][o]);
  cout << ans << endl;

  return 0;
}
