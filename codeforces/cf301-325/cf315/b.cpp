#include <bits/stdc++.h>
using namespace std;
typedef long long ll;

#define REP(i, a, b) for (int i = (int)(a); i < (int)(b); i++)
#define rep(i, a) REP(i, 0, a)
#define EACH(i, a) for (auto i: a)
#define ITR(x, a) for (__typeof(a.begin()) x = a.begin(); x != a.end(); x++)
#define ALL(a) (a.begin()), (a.end())

ll n;
ll bell[4001];
ll comb[4001][4001];

const ll mod = 1000000007;

void gen_comb() {
  rep(i, n + 1) comb[i][0] = comb[i][i] = 1;
  REP(i, 2, n + 1) REP(j, 1, i + 1) {
    comb[i][j] = (comb[i - 1][j - 1] + comb[i - 1][j]) % mod;
  }
}

void gen_bell() {
  bell[0] = bell[1] = 1;
  REP(i, 1, n) rep(j, i + 1) bell[i + 1] = (bell[i + 1] + comb[i][j] * bell[j]) % mod;
}

int main(void) {
  // breath deeply and calm down
  cin >> n;

  gen_comb();
  gen_bell();

  ll ans = 0;
  rep(i, n) ans = (ans + comb[n][i] * bell[i]) % mod;

  cout << ans << endl;

  return 0;
}
