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
ll A[100005], imos[100005];

template<class T> struct SegmentTree {
  // you may need to change MAX!
  const T MAX = 2147483647; //INT_MAX
  vector<T> dat;
  int n;
  SegmentTree(int N) {
    n = 1;
    while (n < N) n *= 2;
    dat.resize(2 * n - 1, MAX);
  };
  void update(int k, T x) {
    k += n - 1;
    dat[k] = x;
    while (k > 0) {
      k = (k - 1) / 2;
      dat[k] = min(dat[2 * k + 1], dat[2 * k + 2]);
    }
  }
  // get minimum val [a, b)
  T query(int a, int b) {
    return query(a, b, 0, 0, n);
  }
  T query(int a, int b, int k, int l, int r) {
    if (r <= a || b <= l) return MAX;
    if (a <= l && r <= b) return dat[k];
    T vl = query(a, b, 2 * k + 1, l, (l + r) / 2);
    T vr = query(a, b, 2 * k + 2, (l + r) / 2, r);
    return min(vl, vr);
  }
};

int main(void) {
  cin.tie(0);
  ios::sync_with_stdio(false);

  cin >> T;
  while (T--) {
    cin >> N;
    rep(i, N) cin >> A[i]; 

    imos[0] = A[0];
    REP(i, 1, N) imos[i] = imos[i - 1] + A[i];

    SegmentTree<ll> seg(N);
    rep(i, N) seg.update(i, A[i]);

    ll ans = (ll)-1e10, mn = 0, k = 0;
    rep(i, N) ans = max(ans, A[i]);

    rep(i, N) {
      if (imos[i] < mn) {
        mn = imos[i];
        k = i;
      } 
    
      if (mn < 0 && i != k) {
        ans = max(ans, imos[i] - imos[k] - min(0LL, seg.query(k + 1, i + 1)));
      } else if (i > 0) {
        ans = max(ans, imos[i] - min(0LL, seg.query(0, i + 1)));
      }
    } 

    cout << ans << endl;
  }

  return 0;
}
