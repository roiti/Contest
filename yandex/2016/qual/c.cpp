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

int N;
double p[11][11];

int main(void) {
  cin.tie(0);
  ios::sync_with_stdio(false);

  cin >> N;
  rep(i, N) rep(j, N) cin >> p[i][j];

  vector<int> perm(N);
  rep(i, N) perm[i] = i;

  double ans = 0.0;
  do {
    double k = 1.0;
    rep(i, N) {
      REP(j, i + 1, N) { 
        k *= 1.0 - p[perm[i]][perm[j]];
      }
    }
    ans += k;
  } while (next_permutation(perm.begin(), perm.end()));

  printf("%.10f\n", ans);

  return 0;
}
