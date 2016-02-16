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

int N, M, K;
int A[60], B[60];

int main(void) {
  cin >> N >> M >> K;
  rep(i, N) cin >> A[i];
  rep(i, M) cin >> B[i];

  ll sa = accumulate(A, A + N);
  ll sb = accumulate(B, B + N);

  while (K) {
    if (K >= 3) {
      
      K -= 3;
    } else if (K == 2) {

      K -= 2
    } else {

      K -= 1;
    }
  }

  ll ans = sa * sb;

  cout << ans << endl;

  return 0;
}
