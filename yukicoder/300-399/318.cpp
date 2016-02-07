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

int n;
int a[100005];

int main(void) {
  cin >> n;
  rep(i, n) cin >> a[i];
  map<int, vector<int>> m;
  map<int, pair<int, int>> p;

  rep(i, n) m[a[i]].push_back(i);

  ITR(ele, m) {
    int x = (*ele).second[0], y = (*ele).second.back() + 1;
    auto lx = 
  }
  return 0;
}
