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

int N, T;
int l, r;
int imos[100005];

int main(void) {
  cin.tie(0);
  ios::sync_with_stdio(false);

  cin >> N >> T;
  rep(loop, N) {
    cin >> l >> r;
    imos[l]++;
    imos[r]--;
  }

  REP(i, 1, T + 1) imos[i] += imos[i - 1];

  int ans = 0;
  rep(i, T + 1) ans = max(ans, imos[i]);

  cout << ans << endl;


  return 0;
}
