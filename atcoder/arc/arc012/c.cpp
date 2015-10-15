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

const int N = 19;
string b[N];

bool is_end() {
  rep(y, N) rep(x, N) {
    if (b[y][x] != '.') {
      int nx, ny;
      nx = x;
      while (nx < N && b[y][nx] == b[y][x]) nx++;
      if (nx - x >= 5) return true;

      ny = y;
      while (ny < N && b[ny][x] == b[y][x]) ny++;
      if (ny - y >= 5) return true;

      nx = x, ny = y;
      while (nx < N && ny < N && b[ny][nx] == b[y][x]) nx++, ny++;
      if (nx - x >= 5) return true;

      nx = x, ny = y;
      while (0 <= nx && ny < N && b[ny][nx] == b[y][x]) nx--, ny++;
      if (ny - y >= 5) return true;
    }
  }
  return false;
}

int main(void) {
  rep(i, N) cin >> b[i];
  int black = 0, white = 0;
  rep(y, N) rep(x, N) {
    if (b[y][x] == 'o') black++;
    if (b[y][x] == 'x') white++;
  }

  if (black + white == 0) {
    cout << "YES" << endl;
    return 0;
  }
  if (black > white + 1 || white > black) {
    cout << "NO" << endl;
    return 0;
  }

  char last = (black == white ? 'x':'o');
  rep(y, N) rep(x, N) {
    if (b[y][x] == last) {
      b[y][x] = '.';
      if (!is_end()) {
        cout << "YES" << endl;
        return 0;
      }
      b[y][x] = last;
    }
  }
  cout << "NO" << endl;

  return 0;
}
