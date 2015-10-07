#include <bits/stdc++.h>
using namespace std;
typedef long long ll;

#define REP(i, a, b) for (int i = (int)(a); i < (int)(b); i++)
#define rep(i, a) REP(i, 0, a)
#define EACH(i, a) for (auto i: a)
#define ITR(x, a) for (__typeof(a.begin()) x = a.begin(); x != a.end(); x++)
#define ALL(a) (a.begin()), (a.end())

int n, m;
int a[100005];
bool used[100005];
vector<vector<int>> edge(100005);

int solve(int i, int c) {
    used[i] = true;
    if (a[i]) c++;
    else c = 0;

    if (c > m) return 0;
    int res = 0;
    bool leaf = true;
    EACH(j, edge[i]) {
        if (used[j]) continue;
        res += solve(j, c);
        leaf = false;
    }
    if (leaf) return 1;
    return res;
}

int main(void) {
  // breath deeply and calm down
  cin >> n >> m;
  rep(i, n) cin >> a[i];
  rep(i, n - 1) {
      int x, y;
      cin >> x >> y;
      x--; y--;
      edge[x].push_back(y);
      edge[y].push_back(x);
  }

  rep(i, n) used[i] = false;
  cout << solve(0, 0) << endl;

  return 0;
}
