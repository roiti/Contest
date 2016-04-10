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

int N, M, K;
int D[16];
int v[105][105];
int mn[1 << 17];
int idx[105];

int main(void) {
  cin.tie(0);
  ios::sync_with_stdio(false);

  cin >> N >> M >> K;
  rep(i, M) cin >> D[i];
  rep(i, N + 1) idx[i] = -1;
  rep(i, M) idx[D[i]] = i;
  rep(i, N) rep(j, K) cin >> v[i][j];

  rep(i, 1 << M + 1) mn[i] = inf; 

  queue<int> que;
  que.push((1 << M) - 1);
  mn[(1 << M) - 1] = 0;
  while (!que.empty()) {
    int mask = que.front(); que.pop();

    for (int i = 0; i < K; i++) {
      int next_mask = 0; 
      for (int j = 0; j < M; j++) {
        if (!(mask & (1 << j))) continue;
        if (idx[v[D[j] - 1][i]] > -1) {
          next_mask |= 1 << idx[v[D[j] - 1][i]];
        }
      }
      if (mn[mask] + 1 < mn[next_mask]) {
        mn[next_mask] = mn[mask] + 1;
        que.push(next_mask);
        if (next_mask == 0) {
          cout << mn[0] << endl;
          return 0;
        }
      }
    }
  }
}
