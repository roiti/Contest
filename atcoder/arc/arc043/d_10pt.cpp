#include <bits/stdc++.h>
using namespace std;
typedef long long ll;

#define REP(i, a, b) for (int i = (int)(a); i < (int)(b); i++)
#define rep(i, a) REP(i, 0, a)
#define EACH(i, a) for (auto i: a)
#define ITR(x, a) for (__typeof(a.begin()) x = a.begin(); x != a.end(); x++)
#define ALL(a) (a.begin()), (a.end())

int main(void) {
  // breath deeply and calm down
  int N, M;
  cin >> N >> M;
  vector<int> P(M);
  rep(i, M) cin >> P[i];
  
  vector<int> pos(N, 0);
  rep(i, N) pos[i] = i;

  ll ans = 0;
  do {
    ll tmp = 0;
    rep(i, M) {
      REP(j, i + 1, M) {
	tmp += abs(pos[j] - pos[i]) * P[i] * P[j];
      }
    }
    ans = max(ans, tmp);
  } while (next_permutation(ALL(pos)));

  cout << ans << endl;
  
  return 0;
}
