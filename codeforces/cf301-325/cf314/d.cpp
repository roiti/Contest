#include <bits/stdc++.h>
using namespace std;
typedef long long ll;

#define REP(i, a, b) for (int i = (int)(a); i < (int)(b); i++)
#define rep(i, a) REP(i, 0, a)
#define EACH(i, a) for (auto i: a)
#define ITR(x, a) for (__typeof(a.begin()) x = a.begin(); x != a.end(); x++)
#define ALL(a) (a.begin()), (a.end())

int n, k, a, m;
int x[200005], y[200005];
bool hit[200005];

int main(void) {
  cin >> n >> k >> a;
  cin >> m;
  rep(i, m) cin >> x[i], y[i] = x[i];

  y[m] = 0;
  y[m + 1] = n + 1;
  sort(y, y + m + 2);
  map<int, pair<int, int>> ref;
  ref[0] = make_pair(0, y[1]);
  REP(i, 1, m + 1) ref[y[i]] = make_pair(y[i - 1], y[i + 1]);
  ref[n + 1] = make_pair(y[m], n + 1);
  
//  rep(i, m + 1) cout << ref[y[i]].first << " " << y[i] << " " << ref[y[i]].second << " " << (ref[y[i]].second - y[i] - 1) / a << endl;

  ll exist = 0; 
  rep(i, m + 1) exist += (ref[y[i]].second - y[i]) / (a + 1);
  
  if (exist >= k) {
    cout << -1 << endl;
    return 0;
  }

  for (int i = m - 1; i > -1; i--) {
    int l, r;
    l = ref[x[i]].first;
    r = ref[x[i]].second;
    int bef = (x[i] - l) / (a + 1) + (r - x[i]) / (a + 1);
    int aft = (r - l) / (a + 1);
    ref[l].second = r;
    ref[r].first  = l;
    exist += aft - bef;
    if (exist >= k) {
      cout << i + 1 << endl;
      break;
    }
  }

  return 0;
}
