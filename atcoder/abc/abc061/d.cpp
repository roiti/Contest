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

const ll inf = (ll)1e15;

int N, M;
int a[1005], b[1005];
ll c[1005], G[1005][1005];

int main(void) {
  cin.tie(0);
  ios::sync_with_stdio(false);

  cin >> N >> M;
  rep(i, M) {
    cin >> a[i] >> b[i] >> c[i];
    a[i]--;
    b[i]--;
  }

  rep(i, N) rep(j, N) G[i][j] = i == j ? 0:-inf;
  rep(i, N) G[a[i]][b[i]] = c[i];

  rep(k, N) rep(i, N) rep(j, N) G[i][j] = max(G[i][j], G[i][k] + G[k][j]);

  ll val = G[0][N - 1];
  rep(k, N) rep(i, N) rep(j, N) G[i][j] = max(G[i][j], G[i][k] + G[k][j]);

  if (val == G[0][N - 1])
    cout << G[0][N - 1] << endl;
  else
    cout << "inf" << endl;

  return 0;
}
