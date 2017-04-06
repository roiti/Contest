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

bool startswith(string a, string b) {
  if (a.size() < b.size()) return false;
  rep(i, b.size()) {
    if (a[i] != b[i]) return false;
  }
  return true;
}

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

  vector<string> X;
  set<int> SA;
  set<string> Y;
  for (auto i: A) X.push_back(S[i]);
  for (auto i: A) SA.insert(i);
  rep(i, N) if (!HAS(SA, i)) Y.insert(S[i]);

  int mn = 1e7;
  for (auto x: X) mn = min(mn, (int)x.size());

  string query = "";
  bool flag = true;
  rep(i, mn) {
    char c = X[0][i];
    REP(j, 1, K) {
      if (X[j][i] != c) {
        flag = false;
        break;
      }
    } 
    if (!flag) break;
    else {
      query += c;
      vector<string> delist;
      for (auto y: Y) {
        if (startswith(y, query)) break;
        else delist.push_back(y);
      }
      for (auto y: delist) Y.erase(y);
      if (Y.size() == 0) {
        cout << query << endl;
        return 0;
      }
    }
  }

  if (Y.size()) cout << -1 << endl;
  else cout << query << endl;

  return 0;
}
