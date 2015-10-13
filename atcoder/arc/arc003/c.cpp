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
int N, M;
string c[501];
double mx[501][501];
double coeff[250005];

int main(void) {
  coeff[0] = 1;
  REP(i, 1, 250005) coeff[i] = coeff[i - 1] * 0.99;

  cin >> N >> M;
  rep(i, N) cin >> c[i];
  int sx, sy, gx, gy;
  rep(y, N) rep(x, M) {
    if (c[y][x] == 's') sx = x, sy = y;
    if (c[y][x] == 'g') gx = x, gy = y;
  }

  deque<tuple<int, int, int, double>> que;
  que.push_back(make_tuple(sx, sy, 0, 10.0));
  while (!que.empty()) {
    auto xytl = que.front(); que.pop_front();
    int x = get<0>(xytl), y = get<1>(xytl), t = get<2>(xytl);
    double l = get<3>(xytl);

    if (mx[y][x] > l) continue;

    rep(i, 4) {
      int nx = x + dx[i], ny = y + dy[i];
      if (!(0 <= nx && nx < M && 0 <= ny && ny < N)) continue;
      if (c[ny][nx] == '#' || c[ny][nx] == 's') continue;
      if (c[ny][nx] == 'g') {
        mx[ny][nx] = max(mx[ny][nx], l);
        continue;
      }
      double nl = min(l, (c[ny][nx] - '0') * coeff[t + 1]);
      if (mx[ny][nx] >= nl) continue;
      mx[ny][nx] = nl;
      que.push_back(make_tuple(nx, ny, t + 1, nl));
    }
  }

  if (mx[gy][gx] > 0)
    printf("%.13f\n", mx[gy][gx]);
  else
    printf("%d", -1);

  return 0;
}
