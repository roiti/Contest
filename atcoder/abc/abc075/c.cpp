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

const int inf = (int)1e8;

int N, M;
int a[55], b[55];
int G[55][55], X[55][55];

int main(void) {
  cin.tie(0);
  ios::sync_with_stdio(false);
  
  cin >> N >> M;
  rep(i, N) rep(j, N) G[i][j] = (i == j ? 0:inf);

  rep(i, M) {
    cin >> a[i] >> b[i];
    a[i]--; b[i]--;
    G[a[i]][b[i]] = 1;
    G[b[i]][a[i]] = 1;
  }

  int ans = 0;
  rep(z, M) {
    rep(i, N) rep(j, N) X[i][j] = G[i][j]; 
    X[a[z]][b[z]] = X[b[z]][a[z]] = inf;

    rep(k, N) rep(i, N) rep(j, N) X[i][j] = min(X[i][j], X[i][k] + X[k][j]);

    bool flag = true;
    rep(i, N) {
      rep(j, N) {
        if (X[i][j] == inf) {
          ans++;
          flag = false;
          break;
        }
      }
      if (!flag) break;
    }
  }

  cout << ans << endl;

  return 0;
}
