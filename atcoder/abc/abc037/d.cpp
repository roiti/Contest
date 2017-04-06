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

const ll mod = (ll)1e9 + 7;
int H, W;
int a[1005][1005];
ll comb[1005][1005];
int dx[] = {1, 0, -1, 0};
int dy[] = {0, 1, 0, -1};

bool is_inside(int x, int y) {
  return (0 <= x && x < W && 0 <= y && y < H);
}

int main(void) {
  cin.tie(0);
  ios::sync_with_stdio(false);

  cin >> H >> W;
  rep(i, H) rep(j, W) cin >> a[i][j];
  rep(i, H) rep(j, W) comb[i][j] = 1;

  priority_queue<pair<int, pair<int, int>>> que;
  rep(i, H) rep(j, W) que.push({-a[i][j], {i, j}});

  while (!que.empty()) {
    auto ele = que.top(); que.pop();
    int aij = -ele.first;
    int y = ele.second.first, x = ele.second.second;

    rep(i, 4) {
      int nx = x + dx[i], ny = y + dy[i]; 
      if (!is_inside(nx, ny)) continue;
      if (a[ny][nx] > a[y][x]) {
        comb[ny][nx] = (comb[ny][nx] + comb[y][x])%mod;
      }
    }
  }
  
  ll ans = 0;
  rep(i, H) rep(j, W) ans = (ans + comb[i][j])%mod;

  cout << ans << endl;

  return 0;
}
