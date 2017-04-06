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

const int eps = 1e-9;
int N;
ll x[100005], y[100005];
int M;
ll K, k;
int a[100005];

bool same(ll x[], ll y[]) {
  rep(i, N) if (x[i] != y[i]) return false;
  return true;
}

int main(void) {
  cin.tie(0);
  ios::sync_with_stdio(false);

  cin >> N;
  rep(i, N) cin >> x[i], y[i] = x[i];
  cin >> M >> K;
  k = K;
  rep(i, M) cin >> a[i], a[i]--;

  int cnt = 0;
  while (k--) {
    rep(i, M) {
      y[a[i]] = y[a[i] - 1] + y[a[i] + 1] - y[a[i]];
    } 
    cnt++;
    if (same(x, y)) break;
  }
  
  if (k > 0) {
    K %= cnt;
    while (K--) {
      rep(i, M) {
        x[a[i]] = x[a[i] - 1] + x[a[i] + 1] - x[a[i]];
      } 
    }
    rep(i, N) printf("%.10f\n", (double)x[i]);
  } else {
    rep(i, N) printf("%.10f\n", (double)y[i]);
  }


  return 0;
}
