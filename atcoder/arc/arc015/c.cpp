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

int N;
double G[205][205];
string unit[205];

int main(void) {
  cin >> N;
  map<string, int> idx;
  int cnt = 0;
  rep(i, N) {
    string large, small;
    double m;
    cin >> large >> m >> small;
    if (!HAS(idx, large)) {
      unit[cnt] = large;
      idx[large] = cnt++;
    }
    if (!HAS(idx, small)) {
      unit[cnt] = small;
      idx[small] = cnt++;
    }
    G[idx[large]][idx[small]] = m;
    G[idx[small]][idx[large]] = 1.0 / m;
  }

  rep(k, cnt) rep(i, cnt) rep(j, cnt) {
    if (G[i][j] == 0 && G[i][k] > 0 && G[k][j] > 0) G[i][j] =  G[i][k] * G[k][j];
  }
  int x = -1, y = -1;
  double M = 0;
  rep(i, cnt) rep(j, cnt) if (G[i][j] > M) {
    M = G[i][j];
    x = i;
    y = j;
  }

  printf("1%s=%d%s\n", unit[x].c_str(), (int)(M + 1e-1), unit[y].c_str());

  return 0;
}
