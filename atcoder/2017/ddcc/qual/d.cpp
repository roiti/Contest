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

int H, W, A, B;
string G[205];
char X[205][105], Y[105][205];

int main(void) {
  cin.tie(0);
  ios::sync_with_stdio(false);

  cin >> H >> W;
  cin >> A >> B;
  rep(i, H) cin >> G[i];

  // w half
  rep(i, H) rep(j, (W + 1)/2) 
    if (G[i][j] == G[i][W - j - 1] == 's') X[i][j] = 's';
  
  // h half
  rep(i, W) rep(j, (H + 1)/2) 
    if (G[j][i] == G[H - j - 1][i] == 's') Y[j][i] = 's';

  return 0;
}
