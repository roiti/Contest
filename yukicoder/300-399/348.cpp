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

int dx4[] = {1, 0, -1, 0}, dy4[] = {0, 1, 0, -1};
int dx8[] = {1, 1, 0, -1, -1, -1, 0, 1}, dy8[] = {0, 1, 1, 1, 0, -1, -1, -1};

int N, M;
char G[1005][1005];
int depth[1005][1005];
int ans[2];

bool is_inside(int x, int y) {
  return (0 <= x && x < M && 0 <= y && y < N);
}

int dfs_x(int x, int y) {
  G[y][x] = 'X';
  int res = 1;
  rep(i, 8) {
    int nx = x + dx8[i], ny = y + dy8[i];
    if (!is_inside(nx, ny)) continue;
    if (G[ny][nx] != 'x') continue;
    res = dfs_x(nx, ny) + 1;
  }
  return res;
}

void dfs_dot(int x, int y, int d) {
  depth[y][x] = d;
  rep(i, 4) {
    int nx = x + dx4[i], ny = y + dy4[i];
    if (!is_inside(nx, ny)) continue;
    if (G[ny][nx] != '.') continue;
    if (depth[ny][nx] != -1) continue;
    dfs_dot(nx, ny, d);
  }
}

int main(void) {
  cin.tie(0);
  ios::sync_with_stdio(false);

  cin >> N >> M;
  rep(y, N + 2) rep(x, M + 2) G[y][x] = '.';
  rep(y, N) rep(x, M) cin >> G[y + 1][x + 1];
  rep(y, N + 2) rep(x, M + 2) depth[y][x] = -1;
  N += 2; M += 2;

  int d = -1;
  rep(y, N) rep(x, M) {
    if (G[y][x] == 'x') {
      ans[d%2] += dfs_x(x, y);
    }
    if (G[y][x] == '.') {
      if (depth[y][x] == -1) dfs_dot(x, y, d + 1);
      d = depth[y][x];
    }
  }

  cout << max(ans[0], ans[1]) << endl;

  return 0;
}
