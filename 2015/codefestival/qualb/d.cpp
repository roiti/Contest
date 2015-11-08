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
ll S, C;
set<ll> start, ed;
vector<ll> ans;

int main(void) {
  start.insert((ll)1e18);
  ed.insert((ll)1e18);

  cin >> N;
  while (N--) {
    cin >> S >> C;
    auto it1 = start.upper_bound(S);
    auto it2 = ed.lower_bound(S);
    if (*it2 < *it1) S = *it2 + 1;
    bool flag = HAS(ed, S - 1);
    if (flag) ed.erase(S - 1);

    ll i = S;
    while (1) {
      it1 = start.upper_bound(i);
      it2 = ed.upper_bound(i);
      ll s = *it1;
      ll e = *it2;
//    cout << i << " " << s << " " << e << " " << endl;
      if (C < s - i) {
        if (!flag) start.insert(S);
        ed.insert(i + C - 1);
        ans.push_back(i + C - 1);
        break;
      }
      else if (C == s - i) {
        if (!flag) start.insert(S);
        start.erase(s);
        ans.push_back(i + C - 1);
        break;
      }
      else {
        C -= s - i;
        i = e + 1;
        start.erase(s);
        ed.erase(e);
      }
    }
  }

  EACH(i, ans) printf("%lld\n", i);

  return 0;
}
