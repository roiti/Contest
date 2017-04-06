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

int n;
int a[200005];
bool used[200005];


int main(void) {
  cin.tie(0);
  ios::sync_with_stdio(false);

  cin >> n;
  rep(i, n) cin >> a[i];
  sort(a, a + n);

  ll ans = 0;
  ll s = 0;
  rep(i, n) s += a[i];
  rep(i, n) {
    if (s <= ans) break;
    if (used[a[i]]) continue;
    ll tmp = 0;
    REP(j, i, n) {
      if (a[j]%a[i] == 0) used[a[j]] = true;
      tmp += a[j]/a[i]*a[i];
    }
    ans = max(ans, tmp);
    s -= a[i];
  }

  cout << ans << endl;

  return 0;
}
