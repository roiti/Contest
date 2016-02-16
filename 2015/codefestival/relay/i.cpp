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
int k[205], d[205];

int main(void) {
  cin >> N;
  rep(i, N) cin >> k[i] >> d[i];

  set<pair<int, int>> exist;
  exist.insert(make_pair(0, 0));
  rep(i, N) {
    set<pair<int, int>> nexist;
    ITR(x, exist) {
      nexist.insert(make_pair((*x).first + k[i], (*x).second + d[i]));
      nexist.insert(make_pair((*x).first - d[i], (*x).second - k[i]));
    }
    exist = nexist;
  }

  cout << (HAS(exist, make_pair(0, 0)) ? "valid":"invalid") << endl;
  return 0;
}
