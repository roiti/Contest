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
int h[100005], w[100005];
int wrap[100005];

template<class T> struct SegmentTree {
  const T MIN = 0; 
  vector<T> dat;
  int n;
  SegmentTree(int N) {
    n = 1;
    while (n < N) n *= 2;
    dat.resize(2 * n - 1, MIN);
  };
  void update(int k, T x) {
    k += n - 1;
    dat[k] = x;
    while (k > 0) {
      k = (k - 1) / 2;
      dat[k] = max(dat[2 * k + 1], dat[2 * k + 2]);
    }
  }
  // get max val [a, b)
  T query(int a, int b) {
    return query(a, b, 0, 0, n);
  }
  T query(int a, int b, int k, int l, int r) {
    if (r <= a || b <= l) return MIN;
    if (a <= l && r <= b) return dat[k];
    T vl = query(a, b, 2 * k + 1, l, (l + r) / 2);
    T vr = query(a, b, 2 * k + 2, (l + r) / 2, r);
    return max(vl, vr);
  }
};

int main(void) {
  cin.tie(0);
  ios::sync_with_stdio(false);

  cin >> N;
  rep(i, N) cin >> w[i] >> h[i];
  SegmentTree<int> seg(100005);

  vector<pair<int, int>> box;
  rep(i, N) box.push_back({w[i], h[i]});
  sort(box.begin(), box.end());
  rep(i, N) w[i] = box[i].first, h[i] = box[i].second;

  int i = 0;
  while (i < N) {
    int j = i;
    while (j < N && w[j] == w[i]) {
      wrap[j] = seg.query(0, h[j]) + 1;
      j += 1;
    }
    REP(k, i, j) seg.update(h[k], wrap[k]);
    //cout << w[i] << " " << h[i] << " " << wrap[i] << endl;
    i = j;
  }

  int ans = 0;
  rep(i, N) ans = max(ans, wrap[i]);

  cout << ans << endl;

  return 0;
}
