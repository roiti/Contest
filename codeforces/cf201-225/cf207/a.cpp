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

int n, m;
int l, r, x;
int ans[300005];
set<int> s;

int main(void) {
  cin >> n >> m;
  REP(i, 1, n + 1) s.insert(i);
  s.insert((int)1e8);
  rep(loop, m) {
    cin >> l >> r >> x;
    auto it = s.lower_bound(l);
    while (true) {
      auto it = s.lower_bound(l);
      if (*it > r) break;
      if (*it == x) {
        l = x + 1;
        continue;
      }
      ans[*it - 1] = x;
      s.erase(it);
    }
  }

  rep(i, n) cout << ans[i] << (i == n - 1 ? "\n":" ");

  return 0;
}
