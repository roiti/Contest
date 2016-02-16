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

int h, w, q;
string A[505];
int W[505][505], H[505][505];

int main(void) {
  cin >> h >> w;
  rep(i, h) cin >> A[i];
  rep(i, h) REP(j, 1, w) {
    if (A[i][j - 1] == '.' && A[i][j] == '.') W[i][j] = W[i][j - 1] + 1;
    else W[i][j] = W[i][j - 1];
  }
  rep(j, w) REP(i, 1, h) {
    if (A[i - 1][j] == '.' && A[i][j] == '.') H[i][j] = H[i - 1][j] + 1;
    else H[i][j] = H[i - 1][j];
  }

  cin >> q;
  while (q--) {
    int r1, c1, r2, c2;
    scanf("%d %d %d %d", &r1, &c1, &r2, &c2);
    r1--; c1--; r2--; c2--;

    int ans = 0;
    REP(r, r1, r2 + 1) {
      ans += W[r][c2] - W[r][c1];
    }
    REP(c, c1, c2 + 1) {
      ans += H[r2][c] - H[r1][c];
    }
    printf("%d\n", ans);
  }

  return 0;
}
