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

ll A, B, N;
ll L, T, M;

bool ok(ll R) {
  ll mx = A + (R - 1) * B;
  ll mn = A + (L - 1) * B;
  ll D = R - L;

  if (mx > T) return false;
  return (mn * (D + 1) + B * D * (D + 1) / 2) <= T * M;
}

int main(void) {
  cin >> A >> B >> N;
  while (N--) {
    cin >> L >> T >> M;
    ll R = L;
    ll mn = A + (L - 1) * B;
    if (mn > T) {
      R = -1;
    } else {
      ll XR = 1LL << 22;
      while (XR > R) {
        ll m = (R + XR) / 2;
        if (!ok(m)) XR = m;
        else R = m + 1;
      }
      R -= 1;
    }
    cout << R << endl;
  }

  return 0;
}
