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
ll A, B;
ll h[100005];

int main(void) {
  cin.tie(0);
  ios::sync_with_stdio(false);

  cin >> N >> A >> B;
  rep(i, N) cin >> h[i];

  ll D = A - B;

  ll lo = 0, hi = 1000000000;
  while (hi - lo > 0) {
    ll mi = (hi + lo)/2;
    ll cnt = 0;
    rep(i, N) {
      ll r = h[i] - mi*B;
      if (r > 0) cnt += (r + D - 1)/D;
    }          

    if (cnt <= mi) {
        hi = mi;
    } else {
        lo = mi + 1;
    }
  }

  cout << hi << endl;

  return 0;
}
