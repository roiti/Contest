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

int dx[] = {1, 0, -1, 0}, dy[] = {0, 1, 0, -1};

int Y, X, K;
char A[805][805];
int sx, sy;

int main(void) {
  cin.tie(0);
  ios::sync_with_stdio(false);
  // breath deeply and calm down

  cin >> Y >> X >> K;
  rep(y, Y) rep(x, X) cin >> A[y][x];
  rep(y, Y) rep(x, X) if (A[y][x] == 'S') sx = x, sy = y;

  queue<pair<int, int>> que;
  que.push(make_pair(sx, sy));
  rep(loop, K) {
    queue<pair<int, int>> nque;
    while (!que.empty()) {
      auto p = que.front(); que.pop();
      int x = p.first, y = p.second;
      rep(i, 4) {
          int nx = x + dx[i], ny = y + dy[i];
          if (!(0 <= nx && nx < X && 0 <= ny && ny < Y)) continue;
          if (A[ny][nx] == '#') continue;
          if (A[ny][nx] == 'S') continue;
          A[ny][nx] = 'S';
          nque.push(make_pair(nx, ny));
      }
    }
    que = nque;
  }
 

  int ans = 10000;
  rep(y, Y) rep(x, X) {
    if (A[y][x] == 'S') ans = min(ans, (min(min(x, X - x - 1), min(y, Y - y - 1)) + K - 1)/K + 1);
  }
  
  cout << ans << endl;

  return 0;
}
