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

int N;
int color[100005];
vector<int> tree[100005];
vector<int> path;

bool dfs1(int s, int bef) {
  if (s == N - 1) {
    path.push_back(s);
    return true;
  }

  for (int t: tree[s]) {
    if (t == bef) continue;
    if (dfs1(t, s)) {
      path.push_back(s);
      return true;
    }
  }

  return false;
}

void dfs2(int s, int bef) {
  color[s] = 1;

  for (int t: tree[s]) {
    if (t == bef) continue;
    if (color[t] == -1) continue;
    dfs2(t, s);
  }
}

int main(void) {
  cin.tie(0);
  ios::sync_with_stdio(false);

  cin >> N;
  rep(i, N - 1) {
    int a, b;
    cin >> a >> b;
    a--; b--;
    tree[a].push_back(b);
    tree[b].push_back(a);
  }

  dfs1(0, -1);
  reverse(path.begin(), path.end());

  //rep(i, path.size()) cout << path[i] << " ";
  //cout << endl;

  rep(i, path.size()) {
    if (color[path[i]] == 0) color[path[i]] = 1;
    if (color[path[path.size() - i - 1]] == 0) color[path[path.size() - i - 1]] = -1;
  }

  dfs2(0, -1);

  int cnt = 0;
  rep(i, N) if (color[i] == 1) cnt++;

  //cout << cnt << endl;
  cout << (cnt > N - cnt ? "Fennec":"Snuke") << endl;

  return 0;
}
