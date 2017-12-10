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

int H, W, d;
int G[505][505];
char C[4] = {'R', 'G', 'B', 'Y'};

bool is_in(int h, int w) {
    return 0 <= h && h < H && 0 <= w && w < W;
}

bool can(int y, int x, int n) {
    if (is_in(y - d, x) && G[y - d][x] == n) return false;
    if (is_in(y + d, x) && G[y + d][x] == n) return false;
    if (is_in(y, x - d) && G[y][x - d] == n) return false;
    if (is_in(y, x + d) && G[y][x + d] == n) return false;
    for (int w = x - d, h = y; w != x; w += 1, h += 1)
        if (is_in(h, w) && G[h][w] == n) return false;
    for (int w = x - d, h = y; w != x; w += 1, h -= 1)
        if (is_in(h, w) && G[h][w] == n) return false;
    for (int w = x + d, h = y; w != x; w -= 1, h += 1)
        if (is_in(h, w) && G[h][w] == n) return false;
    for (int w = x + d, h = y; w != x; w -= 1, h -= 1)
        if (is_in(h, w) && G[h][w] == n) return false;
    return true;
}

int main(void) {
  cin.tie(0);
  ios::sync_with_stdio(false);

  cin >> H >> W >> d;
  rep(i, H) rep(j, W) G[i][j] = -1;

  rep(h, H) rep(w, W) {
    if (G[h][w] == -1) {
        rep(i, 4) {
            if (can(h, w, i)) {
                G[h][w] = i;
                break;
            }
        }
    }
  }

  rep(h, H) {
      rep(w, W) cout << C[G[h][w]];
      cout << endl;
  }

  return 0;
}
