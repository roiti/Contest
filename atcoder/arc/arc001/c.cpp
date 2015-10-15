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

string c[8];

bool ok(int x, int y) {
  rep(yy, 8) if (yy != y && c[yy][x] == 'Q') return false;
  rep(xx, 8) if (xx != x && c[y][xx] == 'Q') return false;
  REP(d, -7, 8) {
    if (d == 0) continue;
    if (0 <= x + d && x + d < 8 && 0 <= y + d && y + d < 8) {
      if (c[y + d][x + d] == 'Q') return false;
    }
    if (0 <= x + d && x + d < 8 && 0 <= y - d && y - d < 8) {
      if (c[y - d][x + d] == 'Q') return false;
    }
  }
  return true;
}

bool dfs(int y) {
  if (y == 8) return true;

  rep(x, 8) if (c[y][x] == 'Q') return dfs(y + 1);

  rep(x, 8) {
    if (ok(x, y)) {
      c[y][x] = 'Q';
      if (dfs(y + 1)) return true;
      c[y][x] = '.';
    }
  }
  return false;
}

int main(void) {
  rep(y, 8) cin >> c[y];

  rep(y, 8) rep(x, 8) {
    if (c[y][x] == 'Q') {
      if (!ok(x, y)) {
        cout << "No Answer" << endl;
        return 0;
      }
    }
  }

  if (dfs(0)) {
    rep(y, 8) cout << c[y] << endl;
  } else {
    cout << "No Answer" << endl;
  }

  return 0;
}
