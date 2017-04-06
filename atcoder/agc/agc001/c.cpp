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

int N, K;
int A[2016], B[2016];
bool used[2016];
vector<int> G[2016];

pair<int, int> solve(int i, int d) {
  if (d > K) return {0, 0};
  // res = self + child num
  int res = 1;
  int mx = 0;
  for (auto j: G[i]) {
    if (!used[j]) {
      used[j] = true;
      auto p = solve(j, d + 1); 
      used[j] = false;
      int n = p.first, r = p.second;
      if (r == -1 || r + mx > K) {
        return {-1, -1};
      }
      mx = max(mx, r);
      res += n;
    }
  }
  return {res, mx + 1};
}

int main(void) {
  cin.tie(0);
  ios::sync_with_stdio(false);

  cin >> N >> K;
  rep(i, N - 1) {
    cin >> A[i] >> B[i]; 
    G[A[i] - 1].push_back(B[i] - 1);
    G[B[i] - 1].push_back(A[i] - 1);
  }

  int ans = N;
  rep(i, N) {
    used[i] = true;
    for (auto j: G[i]) {
      used[j] = true;
      auto p = solve(j, 1);
      used[j] = false;
      if (p.second == -1) continue;
      //if (ans > N - p.first - 1) cout << i << " " << j << endl;
      ans = min(ans, N - p.first - 1);
    }
    used[i] = false;
  } 

  cout << ans << endl;

  return 0;
}
