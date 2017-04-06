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
int A[100005];
string S[100005];

int main(void) {
  cin.tie(0);
  ios::sync_with_stdio(false);

  cin >> N >> K;
  rep(i, K) cin >> A[i], A[i] -= 1;
  rep(i, N) cin >> S[i];

  if (N == K) {
    cout << endl;
    return 0;
  }

  int mn = 1e7;
  for (auto i: A) {
    mn = min(mn, (int)S[i].size());
  }

  string query = "";
  bool flag = true;
  rep(i, mn) {
    char c = S[A[0]][i];
    REP(j, 1, K) {
      if (S[A[j]][i] != c) {
        flag = false;
        break;
      }
    } 
    if (!flag) break;
    else query += c;
  }

  set<int> B;
  rep(i, N) B.insert(i);
  rep(i, K) B.erase(A[i]);
  int mx = 0;
  for (auto i: B) {
    flag = true;
    rep(j, min(S[i].size(), query.size())) {
      if (S[i][j] != query[j]) {
        mx = max(mx, j);
        flag = false;
        break;
      }
    }
    if (flag) mx = max(mx, (int)S[i].size());
  }

  if (mx < query.size()) cout << query.substr(0, mx + 1) << endl;
  else cout << -1 << endl;

  return 0;
}
