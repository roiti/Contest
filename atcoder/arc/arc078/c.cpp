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
int a[200005];
int main(void) {
  cin.tie(0);
  ios::sync_with_stdio(false);
  // breath deeply and calm down

  cin >> N;
  rep(i, N) cin >> a[i];

  ll s = 0, t = 0;
  rep(i, N) s += a[i];

  ll ans = (ll)1e15;
  for (int i = 0; i < N - 1; i++) {
    s -= a[i];
    t += a[i];
    ans = min(ans, abs(s - t));
  }

  cout << ans << endl;

  return 0;
}
