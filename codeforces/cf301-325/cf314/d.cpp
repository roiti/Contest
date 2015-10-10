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

int main(void) {
  cin >> n >> k >> a;
  cin >> m;
  rep(i, m) cin >> x[i], y[i] = x[i];

  //番兵
  y[m] = 0;
  y[m + 1] = n + 1;
  sort(y, y + m + 2);
  map<int, pair<int, int>> lr;
  lr[0] = make_pair(0, y[1]);
  REP(i, 1, m + 1) lr[y[i]] = make_pair(y[i - 1], y[i + 1]);
  lr[n + 1] = make_pair(y[m], n + 1);
  
  ll ship = 0; 
  rep(i, m + 1) ship += (lr[y[i]].second - y[i]) / (a + 1);
  
  if (ship >= k) {
    cout << -1 << endl;
    return 0;
  }

  for (int i = m - 1; i > -1; i--) {
    int l, r;
    l = lr[x[i]].first;
    r = lr[x[i]].second;
    int bef = (x[i] - l) / (a + 1) + (r - x[i]) / (a + 1);
    int aft = (r - l) / (a + 1);
    lr[l].second = r;
    lr[r].first  = l;
    ship += aft - bef;
    if (ship >= k) {
      cout << i + 1 << endl;
      break;
    }
  }

  return 0;
}

