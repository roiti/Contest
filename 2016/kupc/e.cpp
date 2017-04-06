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

int dx[] = {1, 0, -1, 0};
int dy[] = {0, 1, 0, -1};

int H, W;
string S[105];
bool used[105][105];

bool is_surrounded(int x, int y) {
  if (x == 0 || x == W - 1 || y == 0 || y == H - 1) return false;
  used[y][x] = true;
  bool res = true;
  rep(i, 4) {
    int nx = x + dx[i], ny = y + dy[i];
    if (used[ny][nx]) continue;
    if (S[ny][nx] == '.') {
      res &= is_surrounded(nx, ny);
      if (!res) break;
    }
  }
  used[y][x] = false;
  return res;
}

void clear() {
  REP(y, 1, H - 1) REP(x, 1, W - 1) {
    if (S[y][x] == '#') {
      bool rem = true;
      rep(i, 4) {
        int nx = x + dx[i], ny = y + dy[i];
        if (S[ny][nx] == '-' || S[ny][nx] == 'X') rem = false;
      }
      if (rem) S[y][x] = '.';
    }
  }
}

int solve() {
  rep(i, W) if (S[0][i] == 'X' || S[H - 1][i] == 'X') return -1;
  rep(i, H) if (S[i][0] == 'X' || S[i][W - 1] == 'X') return -1;

  rep(y, H - 1) rep(x, W - 1) {
    if (S[y][x] != 'X') continue;
    rep(i, 4) {
      int nx = x + dx[i], ny = y + dy[i];
      if (S[ny][nx] == '.') {
        S[ny][nx] = '#';
      }
    }
  }

  rep(loop, 300) {
    REP(y, 1, H - 1) REP(x, 1, W - 1) {
      if (S[y][x] == '#') {
        int cnt = 0;
        rep(i, 4) {
          int nx = x + dx[i], ny = y + dy[i];
          if (S[ny][nx] == 'X' || S[ny][nx] == '#') cnt++;
        }
        if (cnt == 3) rep(i, 4) {
          int nx = x + dx[i], ny = y + dy[i];
          if (S[ny][nx] == '.') {
            S[ny][nx] = '#';
          }
        }
      }
    }
    REP(y, 1, H - 1) REP(x, 1, W - 1) {
      if (S[y][x] == '.') {
        int cnt = 0;
        rep(i, 4) {
          int nx = x + dx[i], ny = y + dy[i];
          if (S[ny][nx] == 'X' || S[ny][nx] == '#') cnt++;
        }
        if (cnt == 4) {
          S[y][x] = '#';
        }
      }
    }
  }

  REP(y, 1, H - 1) REP(x, 1, W - 1) {
    if (S[y][x] == '#') {
      int cnt = 0;
      rep(i, 4) {
        int nx = x + dx[i], ny = y + dy[i];
        if (S[ny][nx] == 'X' || S[ny][nx] == '#' || S[ny][nx] == '-') cnt++;
      }
      if (cnt == 4) {
        S[y][x] = '-';
      }
    }
  }

  vector<pair<int, int>> q;
  REP(y, 1, H - 1) REP(x, 1, W - 1) {
    if (S[y][x] == '#') {
      if (x + 1 < W - 1 && 0     < y - 1 && S[y - 1][x + 1] == '.') q.push_back({x + 1, y - 1});
      if (x + 1 < W - 1 && y + 1 < H - 1 && S[y + 1][x + 1] == '.') q.push_back({x + 1, y + 1});
    }
  }
  for (auto p: q) {
    int x = p.first, y = p.second;
    S[y][x] = '#';
    if (is_surrounded(x, y)) {
      S[y][x] = '-';
    }
  }
  clear();


  int ans = 0;
  rep(y, H) rep(x, W) if (S[y][x] == '#') ans += 1;
  return ans;
}

int main(void) {
  cin.tie(0);
  ios::sync_with_stdio(false);

  cin >> H >> W;
  rep(i, H) cin >> S[i];

  cout << solve() << endl;
  rep(i, H) cout << S[i] << endl;

  return 0;
}
