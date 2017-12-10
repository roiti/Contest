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
int A[100005], B[100005];
vector<int> G[100005];
int D[100005];
bool loop;

void dfs(int u) {
  for (auto v: G[u]) {
    if (D[v] == -1) {
      D[v] = 1 - D[u];
      dfs(v);
    } else if (D[v] == 1 - D[u]) {
      continue;
    } else {
      loop = true;
    }
  }
}

int main(void) {
  cin.tie(0);
  ios::sync_with_stdio(false);

  cin >> N >> M;
  rep(i, M) {
    cin >> A[i] >> B[i];
    A[i]--; B[i]--;
    G[A[i]].push_back(B[i]);
    G[B[i]].push_back(A[i]);
  }

  rep(i, N) D[i] = -1;
  D[0] = 0;
  loop = false;
  dfs(0);

  if (loop) {
    cout << (ll)N*(N - 1)/2 - M << endl;
  } else {
    int z = 0;
    rep(i, N) if (D[i] == 0) z++;
    cout << (ll)z*(N - z) - M << endl;
  }
  return 0;
}
