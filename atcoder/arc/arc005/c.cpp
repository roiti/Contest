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

int dx[] = {1, 0, -1, 0}, dy[] = {0, 1, 0, -1};
int H, W;
string c[501];
int visited[501][501];

int main(void) {
  cin >> H >> W;
  rep(y, H) rep(x, W) visited[y][x] = -1;
  rep(i, H) cin >> c[i];
  int sx, sy, gx, gy;
  rep(y, H) rep(x, W) {
    if (c[y][x] == 's') sx = x, sy = y;
    if (c[y][x] == 'g') gx = x, gy = y;
  }

  priority_queue<tuple<int, int, int>> que;
  que.push(make_tuple(2, sx, sy));
  while (!que.empty()) {
    auto pxy = que.top(); que.pop();
    int p = get<0>(pxy), x = get<1>(pxy), y = get<2>(pxy);
    if (visited[y][x] > p) continue;
    if (x == gx && y == gy) break;

    rep(i, 4) {
      int nx = x + dx[i], ny = y + dy[i];
      if (!(0 <= nx && nx < W && 0 <= ny && ny < H)) continue;
      int np = p - (c[ny][nx] == '#' ? 1:0);
      if (visited[ny][nx] >= np) continue;
      visited[ny][nx] = np;
      que.push(make_tuple(np, nx, ny));
    }
  }

  cout << (visited[gy][gx] > -1 ? "YES":"NO") << endl;

  return 0;
}
