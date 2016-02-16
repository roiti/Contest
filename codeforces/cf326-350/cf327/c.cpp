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

const int inf = (int)1e8;
int dx[] = {1, 0, -1, 0}, dy[] = {0, 1, 0, -1};
int n, m;
string a[1005];
string num = "123";
int cost[3][1005][1005];

int main(void) {
  cin >> n >> m;
  rep(i, n) cin >> a[i];

  rep(i, 3) {
    rep(yy, n) {
      bool proc = false;
      rep(xx, m) {
        if (a[yy][xx] == num[i]) {
          proc = true;
          rep(y, n) rep(x, m) cost[i][y][x] = inf;
          priority_queue<tuple<int, int, int>> que;
          que.push(make_tuple(0, xx, yy));
          while (!que.empty()) {
            auto ele = que.top(); que.pop();
            int c = -get<0>(ele), x = get<1>(ele), y = get<2>(ele);
            if (cost[i][y][x] <= c) continue;
            cost[i][y][x] = c;
            rep(k, 4) {
              int nx = x + dx[k], ny = y + dy[k];
              if (!(0 <= nx && nx < m && 0 <= ny && ny < n)) continue;
              if (a[ny][nx] == '#') continue;
              if (a[ny][nx] == '.') {
                que.push(make_tuple(-(c + 1), nx, ny));
              }
              else {
                que.push(make_tuple(-c, nx, ny));
              }
            }
          }
          break;
        }
      }
      if (proc) break;
    }
  }

  int ans = inf;
  rep(y, n) rep(x, m) ans = min(ans, cost[0][y][x] + cost[1][y][x] + cost[2][y][x] - (a[y][x] == '.' ? 2:0));
  cout << (ans < inf ? ans:-1) << endl;
  return 0;
}

