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

int T, N;
ll A[10005];
ll B[10005];

int main(void) {
  cin.tie(0);
  ios::sync_with_stdio(false);

  cin >> T;
  while (T--) {
    cin >> N;
    rep(i, N) cin >> A[i + 1];
    rep(i, N) cin >> B[i + 1];

    int ans = 0;
    REP(i, 1, N + 1) {
      if (A[i] - A[i - 1] >= B[i]) ans++;
    }
    
    cout << ans << endl;
  }

  return 0;
}
