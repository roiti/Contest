#include <bits/stdc++.h>
using namespace std;
typedef long long ll;

#define REP(i, a, b) for (int i = (int)(a); i < (int)(b); i++)
#define rep(i, a) REP(i, 0, a)
#define EACH(i, a) for (auto i: a)
#define ITR(x, a) for (__typeof(a.begin()) x = a.begin(); x != a.end(); x++)
#define ALL(a) (a.begin()), (a.end())

int n;
int x, y;
vector<pair<int, int>> v[1001];

int main(void) {
  // breath deeply and calm down
  scanf("%d", &n);
  int p = -1;
  rep(i, n) {
      scanf("%d %d", &x, &y);
      if (x / 1000 % 2) p = 1;
      else p = -1;
      
      v[x / 1000].push_back(make_pair(p * y, i));
  }

  ll ans = 0;
  rep(i, 1001) {
      sort(ALL(v[i]));
      rep(j, v[i].size())
          printf("%d ", v[i][j].second + 1);
  }
  cout << endl; 
  return 0;
}
