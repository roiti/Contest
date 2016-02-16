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
int b[100005];
ll a[100005];

vector<pair<ll, int>> yes, no;

void solve() {
  cin >> n >> m;
  int ycnt = 1, ncnt = 1;
  rep(i, m) {
    cin >> a[i] >> b[i];
    if (b[i]) yes.push_back(make_pair(a[i], ycnt++));
    else      no.push_back(make_pair(a[i], i));
  }

  sort(yes.begin(), yes.end());
  sort(no.begin(), no.end());

  int i = no.size() - 1;
  map<int, pair<int, int>> ok;
 // for (auto j: ok) cout << j << endl;
  for (int j = yes.size() - 1; j >= 1; j--) {
    int capa = j;
    if (i < 0) break;
    while (yes[j].first <= no[i].first && i >= 0 && capa > 0) {
      ok[no[i].second] = make_pair(yes[j].second + 1, yes[capa - 1].second + 1);
      i--;
      capa--;
    }
  }
  //cout << i << endl;
  if (i > -1) {
    cout << -1 << endl;
    return;
  };

  int j = 0;
  rep(i, m) {
    if (b[i]) {
      cout << 1 << " " << yes[j].second + 1 << endl;
      j++;
    } else {
      auto p = ok[i];
      cout << p.first << " " << p.second << endl;
    }
  }
  return;
}

int main(void) {
  solve();
  return 0;
}
