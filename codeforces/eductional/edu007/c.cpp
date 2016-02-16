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

int n, m;
int a[100005];

int main(void) {
  cin.tie(0);
  ios::sync_with_stdio(false);

  cin >> n >> m;
  rep(i, n) cin >> a[i];

  while (m--) {
    int l, r, x;
    cin >> l >> r >> x;
    l--; r--;
    auto iter = lower_bound(a + l, a + r + 1, x);
    if (a[l] != *iter) {
      cout << iter - a + 1 << endl;
    } else {
      cout << -1 << endl;
    }
  }
  return 0;
}
