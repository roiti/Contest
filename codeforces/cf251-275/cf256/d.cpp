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

ll n, m, k;

ll calc(ll v) {
  ll res = 0;
  REP(i, 1, n + 1) res += min(v/i, m);
  return res;
}

int main(void) {
  cin >> n >> m >> k;
  ll l = 0, r = 1LL << 50;
  while (r > l) {
    ll mid = (l + r)/2;
    if (calc(mid) >= k) r = mid;
    else l = mid + 1;
  }

  cout << l << endl;

  return 0;
}
