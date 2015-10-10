#include <bits/stdc++.h>
using namespace std;
typedef long long ll;

#define REP(i, a, b) for (int i = (int)(a); i < (int)(b); i++)
#define rep(i, a) REP(i, 0, a)
#define EACH(i, a) for (auto i: a)
#define ITR(x, a) for (__typeof(a.begin()) x = a.begin(); x != a.end(); x++)
#define ALL(a) (a.begin()), (a.end())
#define HAS(a, x) (a.find(x) != a.end())

int N, X;
vector<pair<int, int>> edge[100005];
map<int, int> cnt;
bool used[100005];

void dfs(int x, int v) {
  if (HAS(cnt, v)) cnt[v]++;
  else cnt[v] = 1;
  EACH(p, edge[i]) {
    int y = p.first, c = p.second;
    if (used[y]) continue;
    used[y] = true;
    dfs(y, v ^ c);
  }
}

int main(void) {
  cin >> N >> X;
  rep(i, N - 1) {
    int x, y, c;
    cin >> x >> y >> c;
    x--; y--;
    edge[x].push_back(make_pair(y, c));
    edge[y].push_back(make_pair(x, c));
  }

  rep(i, N) used[i] = false;
  used[0] = true;
  dfs(0, 0);
  ll ans = 0;
  if (X == 0) {
    ITR(it, cnt) ans += (ll)(*it).second * ((*it).second - 1) / 2;
  } else {
    ITR(it, cnt) {
      int v = X ^ (*it).first;
      if (HAS(cnt, v)) ans += (ll)cnt[v] * (*it).second;
    }
  }

  cout << ans / (X == 0 ? 1:2) << endl;

  return 0;
}
