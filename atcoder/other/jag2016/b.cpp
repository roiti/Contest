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

int N, M, T;
int a[105];

int main(void) {
  cin.tie(0);
  ios::sync_with_stdio(false);

  cin >> N >> M >> T;
  rep(i, N) cin >> a[i];

  ll ans = a[0] - M;
  REP(i, 1, N) {
    if (a[i] - a[i - 1] <= 2*M) continue;
    else ans += a[i] - a[i - 1] - 2*M;
  }

  ans += max(0, T - a[N - 1] - M);
  cout << ans << endl;

  return 0;
}
