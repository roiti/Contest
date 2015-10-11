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

int R, C, K;
string s[505];
int upper[505][505], under[505][505];

int main(void) {
  cin >> R >> C >> K;
  rep(i, R) cin >> s[i];
  rep(c, C) {
    int cnt1 = 0, cnt2 = 0;
    rep(r, R) {
      if (s[r][c] == 'o') cnt1++;
      else cnt1 = 0;
      upper[r][c] = cnt1;
    }
    for (int r = R - 1; r > -1; r--) {
      if (s[r][c] == 'o') cnt2++;
      else cnt2 = 0;
      under[r][c] = cnt2;
    }
  }

  int ans = 0;
  REP(r, K - 1, R - K + 1){
    REP(c, K - 1, C - K + 1) {
      bool ok = true;
      REP(k, -(K - 1), K) 
        if (min(upper[r][c + k], under[r][c + k]) < K - abs(k)) ok = false;
      if (ok) ans++;
    }
  }

  cout << ans << endl;

  return 0;
}
