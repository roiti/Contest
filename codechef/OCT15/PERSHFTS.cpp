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
  int T;
  cin >> T;
  while (T--) {
    int N, K, NP, NQ;
    cin >> N >> K >> NP >> NQ;
    rep(i, NP) scanf("%d", &P[i]);
    rep(i, NQ) scanf("%d", &Q[i]);

  }

  return 0;
}
