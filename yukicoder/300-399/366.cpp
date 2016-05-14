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
int a[1005];

int main(void) {
  cin.tie(0);
  ios::sync_with_stdio(false);

  cin >> N >> K;
  rep(i, N) cin >> a[i];

  int i = 0, ans = 0;
  while (i < N - K) {
    if (a[i] > a[i + K]) {
      swap(a[i], a[i + K]);
      ans++;
      i = 0;
    } else {
      i++;
    }
  }

  int mn = 1e9;
  rep(i, N - 1) mn = min(mn, a[i + 1] - a[i]);

  if (mn >= 1) {
    cout << ans << endl;
  } else {
    cout << -1 << endl; 
  }
  return 0;
}
