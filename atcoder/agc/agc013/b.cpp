#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
template<typename T> using Graph = vector<vector<T>>;

#define REP(i, a, b) for (int i = (int)(a); i < (int)(b); i++)
#define rep(i, a) REP(i, 0, a)
#define EACH(i, a) for (auto i: a)
#define ITR(x, a) for (__typeof(a.begin()) x = a.begin(); x != a.end(); x++)
#define ALL(a) (a.begin()), (a.end())
#define HAS(a, x) (a.find(x) != a.end())
#define endl '\n'

int N, M;
vector<int> G[100005];
bool used[100005];

vector<int> used(int v) {
  used[v] = true;
  for (auto u: G[v]) {
    if (used[u]) continue;
    
  }
}

int main(void) {
  cin.tie(0);
  ios::sync_with_stdio(false);

  cin >> N >> M;
  rep(i, M) {
    int a, b;
    cin >> a >> b;
    a--; b--;
    G[a].push_back(b);
    G[b].push_back(a);
  }

  vector<int> one;
  rep(i, N) {
    if (G[i].size() == 1) {
        one.push_back(i);
    }
  }

  vector<int> ans;
  if (one.size() == 0) {
    ans = dfs(0);
  } else if (one.size() == 1) {

  } else {

  }

  cout << ans.size() << endl;
  for (auto i: ans) cout << i + 1 << endl;

  return 0;
}
