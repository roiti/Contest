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

int M, N, K;
int E[105][105];

int main(void) {
  cin.tie(0);
  ios::sync_with_stdio(false);

  cin >> M >> N;
  rep(i, N) rep(j, M) cin >> E[i][j];
  
  cin >> K;
  rep(i, K) {
    cin >> u >> v;
  }

  return 0;
}
