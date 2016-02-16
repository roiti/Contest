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

const int inf = (int)1e7;
int dx[] = {1, 0, -1, 0};
int dy[] = {0, 1, 0, -1};

int H, W;
int sx, sy, cx, cy, gx, gy;
int dist[501][501];
string S[501];

bool is_inside(int x, int y) {
  return (0 <= x && x < W && 0 <= y && y < H);
}

int solve(int sx, int sy, int gx, int gy) {
  rep(i, H) rep(j, W) dist[i][j] = inf;
  queue<pair<int, int>> que;
  que.push({sx, sy});
  dist[sy][sx] = 0;

  while (!que.empty()) {
    auto ele = que.front(); que.pop();
    int x = ele.first, y = ele.second;

    rep(i, 4) {
      int nx = x + dx[i], ny = y + dy[i];
      if (!is_inside(nx, ny)) continue;
      if (S[ny][nx] == '#') continue;
      if (dist[ny][nx] > dist[y][x] + 1) {
        dist[ny][nx] = dist[y][x] + 1;
        que.push({nx, ny});
      }
    }
  }
  return dist[gy][gx];
}

int main(void) {
  cin.tie(0);
  ios::sync_with_stdio(false);

  cin >> H >> W;
  rep(i, H) cin >> S[i];

  rep(y, H) {
    rep(x, W) {
      if (S[y][x] == 'S') sx = x, sy = y;
      if (S[y][x] == 'C') cx = x, cy = y;
      if (S[y][x] == 'G') gx = x, gy = y;
    }
  }

  int ans = solve(sx, sy, cx, cy) + solve(cx, cy, gx, gy);

  cout << (ans < inf ? ans:-1) << endl;

  return 0;
}
