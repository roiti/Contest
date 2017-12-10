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

int N, K;
int x[55], y[55];

int main(void) {
  cin.tie(0);
  ios::sync_with_stdio(false);

  cin >> N >> K;
  rep(i, N) cin >> x[i] >> y[i];

  ll ans = (ll)4e18;

  rep(i, N) {
    int lx = x[i];
    rep(j, N) {
      int rx = x[j];
      if (lx >= rx) continue;
      rep(k, N) {
        int uy = y[k];
        rep(l, N) {
          int dy = y[l];
          if (dy >= uy) continue;
          int cnt = 0;
          rep(m, N) {
            if (lx <= x[m] && x[m] <= rx && dy <= y[m] && y[m] <= uy) cnt++;
          }
          if (cnt >= K) {
            ans = min(ans, (ll)(rx - lx)*(uy - dy));
          }
        }
      }
    }
  }

  cout << ans << endl;

  return 0;
}
