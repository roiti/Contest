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
deque<ll> A;

int main(void) {
  cin >> N;
  rep(i, N) {
    int t;
    cin >> t;
    A.push_back(t);
  };

  ll ans = 0;
  while (N > 1) {
    ll x0 = A[0], x1 = A[1];
    ll y0 = A[N - 1], y1 = A[N - 2];
    N -= 2;
    if (2*x0 + x1 + 1 <= 2*y0 + y1 + 1) {
      ans += 2*x0 + x1 + 1;
      A.pop_front();A.pop_front();
      A[0] += x0 + x1 + 2;
    }
    else {
      ans += 2*y0 + y1 + 1;
      A.pop_back();A.pop_back();
      A[N - 1] += y0 + y1 + 2;
    }
  }
  cout << ans << endl;
  return 0;
}
