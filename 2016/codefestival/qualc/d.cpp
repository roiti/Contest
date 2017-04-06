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

int H, W;
char c[305][305] ;
int cost[305];
int rem[305];

void print_c() {
  rep(h, H) {
    rep(w, W) cout << c[h][w];
    cout << endl;
  }
}

void print_cost() {
  rep(w, W) cout << cost[w] << endl;;
}

int main(void) {
  cin.tie(0);
  ios::sync_with_stdio(false);

  cin >> H >> W;
  rep(h, H) rep(w, W) cin >> c[H - h - 1][w];
  rep(w, W) c[H][w] = '-';

  rep(w, W) {
    int cur = 0, nxt = 0;
    if (w > 0) {
      int tmp = 0;
      rep(h, H) if (c[h][w] != '-' && c[h][w] == c[h][w - 1]) cur++;
      rep(h, H) if (c[h + 1][w] != '-' && c[h + 1][w] == c[h][w - 1]) nxt++;
    }
    if (w < W - 1) {
      int tmp = 0;
      rep(h, H) if (c[h][w] != '-' && c[h][w] == c[h][w + 1]) cur++;
      rep(h, H) if (c[h + 1][w] != '-' && c[h + 1][w] == c[h][w + 1]) nxt++;
    }
    cost[w] = nxt;
  }

  ll ans = 0;
  rep(loop, H*W) {
    int mx = 1e5;
    int idx = 0;
    rep(w, W) if (c[0][w] != '-' && cost[w] <= mx) mx = cost[w], idx = w;

    print_c();
    cout << endl;
    //rep(w, W) cout << cost[w] << " "; cout << endl;

    if (idx > 0)     rep(h, H) if (c[h][idx] != '-' && c[h][idx] == c[h][idx - 1]) ans++;
    if (idx < W - 1) rep(h, H) if (c[h][idx] != '-' && c[h][idx] == c[h][idx + 1]) ans++;
    
    //cout << loop << " " << ans << " " << mx << " " << idx << endl;
    rep(i, H) c[i][idx] = c[i + 1][idx];

    REP(w, idx - 1, idx + 2) {
      int cur = 0, nxt = 0;
      if (w < 0 || w > W - 1) continue;
      if (w > 0) {
        rep(h, H) if (c[h][w] != '-' && c[h][w] == c[h][w - 1]) cur++;
        rep(h, H) if (c[h + 1][w] != '-' && c[h + 1][w] == c[h][w - 1]) nxt++;
      }
      if (w < W - 1) {
        rep(h, H) if (c[h][w] != '-' && c[h][w] == c[h][w + 1]) cur++;
        rep(h, H) if (c[h + 1][w] != '-' && c[h + 1][w] == c[h][w + 1]) nxt++;
      }
      cost[w] = nxt;
    }
  }

  cout << ans << endl;

  return 0;
}
