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
ll a[100005];

int main(void) {
  cin.tie(0);
  ios::sync_with_stdio(false);

  cin >> N >> K;
  rep(i, N) cin >> a[i];

  ll ans = 0;
  rep(i, N) {
    ans += min(i + 1, min(K, min(N - K + 1, N - i)))*a[i];
  }

  cout << ans << endl;

  return 0;
}
