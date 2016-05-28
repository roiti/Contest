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

int N, Q;
int l[200005], r[200005];
ll c[200005];

int main(void) {
  cin.tie(0);
  ios::sync_with_stdio(false);

  cin >> N >> Q;
  rep(i, Q) {
    cin >> l[i] >> r[i];
    l[i]--;
    r[i]--;
  }

  rep(i, Q) {
    c[l[i]] += 1; 
    c[r[i] + 1] += 1;
  }

  REP(i, 1, N) c[i] += c[i - 1];

  string ans = "";
  rep(i, N) ans += "01"[c[i]%2];
  cout << ans << endl;

  return 0;
}
