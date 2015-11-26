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
int n, m;
int x, y;
int B[405][405], R[405][405];

int main(void) {
  cin >> n >> m;
  rep(i, n) rep(j, n) R[i][j] = B[i][j] = (i != j ? inf:0);
  rep(i, m) {
    cin >> x >> y;
    x--; y--;
    R[y][x] = R[x][y] = 1;
  }

  rep(i, n) rep(j, n) {
    if (R[i][j] == inf) B[i][j] = 1;
  }
  rep(k, n) rep(i, n) rep(j, n) R[i][j] = min(R[i][j], R[i][k] + R[k][j]);
  rep(k, n) rep(i, n) rep(j, n) B[i][j] = min(B[i][j], B[i][k] + B[k][j]);

  int ans = max(R[0][n - 1], B[0][n - 1]);
  cout << (ans < inf ? ans:-1) << endl;

  return 0;
}
