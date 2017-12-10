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

int dx[] = {1, 0, -1}, dy = {0, 1, 0};

int T, n, m;
char A[11][11];

void solve() {
  cin >> n >> m;
  rep(y, n) rep(x, m) cin >> A[y][x]; 

  while (1) {
    rep(y, n) rep(x, m) {
      if (A[y][x] != '*') continue;
      rep(i, 3) {
        int sx = x + dx, sy = y + dy;
        if (sx < 0 || sx >= m  || sy < 0 || sy >= n) continue;
        if (A[sy][sx] != '*') continue;

        int tx = x + 2*dx, ty = y + 2*dy;
        if (tx < 0 || tx >= m  || ty < 0 || ty >= n) continue;
        if (A[ty][tx] != '.') continue;

        A[y][x] = '.';
        A[sy][sx] = '.';
        A[ty][tx] = '.';
        ans.push_back(make_tuple(x + 1, y + 1, tx + 1, ty + 1));

        break;
      }
    }
  }
}

int main(void) {
  cin.tie(0);
  ios::sync_with_stdio(false);

  cin >> T;

  while (T--) solve();

  return 0;
}
