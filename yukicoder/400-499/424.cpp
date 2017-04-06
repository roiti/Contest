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

int h, w;
int sx, sy, gx, gy;
int b[55][55];
bool used[55][55];

int dx[] = {1, 0, -1, 0};
int dy[] = {0, 1, 0, -1};

bool is_inside(int x, int y) {
  return (0 <= x && x < w && 0 <= y && y < h);
}

int main(void) {
  cin.tie(0);
  ios::sync_with_stdio(false);

  cin >> h >> w;
  cin >> sy >> sx >> gy >> gx;
  sx--; sy--; gx--; gy--;
  rep(i, h) {
    string s;
    cin >> s;
    rep(j, w) b[i][j] = s[j] - '0';
  }

  queue<pair<int, int>> que;
  que.push({sx, sy});
  while (!que.empty()) {
    auto p = que.front(); que.pop();
    int x = p.first, y = p.second;
    if (used[y][x]) continue;
    used[y][x] = true;
    if (x == gx && y == gy) break;

    rep(i, 4) {
      int nx = x + dx[i], ny = y + dy[i];
      //cout << (nx < w) << " " << (ny < h) << endl;
      if (!is_inside(nx, ny)) continue;
      if (used[ny][nx]) continue;
      if (abs(b[ny][nx] - b[y][x]) <= 1) que.push({nx, ny});
    }
    rep(i, 4) {
      int nx = x + dx[i], ny = y + dy[i];
      int n2x = x + 2*dx[i], n2y = y + 2*dy[i];
      if (!is_inside(n2x, n2y)) continue;
      if (used[n2y][n2x]) continue;
      if (b[y][x] == b[n2y][n2x] && b[ny][nx] < b[n2y][n2x]) que.push({n2x, n2y});
    }
  }

  cout << (used[gy][gx] ? "YES":"NO") << endl;

  return 0;
}
