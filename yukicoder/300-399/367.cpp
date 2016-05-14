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

int dx[] = {2, 2, 1, 1, -1, -1, -2, -2};
int dy[] = {1, -1, 2, -2, 2, -2, 1, -1};

int dx2[] = {1, -1, -1, 1};
int dy2[] = {1, 1, -1, -1};

const int inf = 1e8;

int H, W;
int mn[505][505][2];
string s[505];

bool is_inside(int x, int y) {
  return (0 <= x && x < W && 0 <= y && y < H);
}

int main(void) {
  cin.tie(0);
  ios::sync_with_stdio(false);

  cin >> H >> W;
  rep(i, H) cin >> s[i];
  
  int sx = 0, sy = 0, gx = 0, gy = 0;
  rep(y, H) rep(x, W) {
    mn[y][x][0] = mn[y][x][1] = inf;
    if (s[y][x] == 'S') sx = x, sy = y;
    if (s[y][x] == 'G') gx = x, gy = y;
  }

  int ans = -1;
  priority_queue<tuple<int, int, int, int>> que;
  que.push(make_tuple(0, sx, sy, 0));

  while (!que.empty()) {
    auto ele = que.top(); que.pop();
    int cost = -get<0>(ele), x = get<1>(ele), y = get<2>(ele), z = get<3>(ele);

    if (x == gx && y == gy) {
      ans = cost;
      break;
    }

    if (s[y][x] == 'R') z = 1 - z;

    if (z == 0) {
      rep(i, 8) {
        int nx = x + dx[i], ny = y + dy[i];
        if (!is_inside(nx, ny)) continue;
        if (mn[ny][nx][z] <= cost + 1) continue;
        mn[ny][nx][z] = cost + 1;
        que.push(make_tuple(-(cost + 1), nx, ny, z));
      }
    } else {
      rep(i, 4) {
        int nx = x + dx2[i], ny = y + dy2[i];
        if (!is_inside(nx, ny)) continue;
        if (mn[ny][nx][z] <= cost + 1) continue;
        mn[ny][nx][z] = cost + 1;
        que.push(make_tuple(-(cost + 1), nx, ny, z));
      }
    }
  }
  
  cout << ans << endl;

  return 0;
}
