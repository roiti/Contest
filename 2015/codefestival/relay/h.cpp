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

int dx[] = {1,0,-1,0}, dy[] = {0, 1, 0, -1};
int H,W;
string A[505];
bool used[505][505];

int main(void) {
  cin >> H >> W;
  rep(i, H) cin >> A[i];
  rep(y, H) rep(x, W) used[y][x] = false;

  priority_queue<tuple<int, int, int>> que;
  que.push(make_tuple(0, 0, 0));
  while (!que.empty()) {
    auto ele = que.top(); que.pop();
    int cost = -get<0>(ele), x = get<1>(ele), y = get<2>(ele);
    if (used[y][x]) continue;
    used[y][x] = true;
    if (x == W - 1 && y == H - 1) {
      cout << cost << endl;
      break;
    }
    rep(i, 4) {
      int nx = x + dx[i], ny = y + dy[i];
      if (0 <= nx && nx < W && 0 <= ny && ny < H) {
        if (A[ny][nx] != A[y][x])
          que.push(make_tuple(-(cost + 1), nx, ny));
        else
          que.push(make_tuple(-cost, nx, ny));
      }
    }
  }

  return 0;
}
