#include <bits/stdc++.h>
using namespace std;
typedef long long ll;

#define REP(i, a, b) for (int i = (int)(a); i < (int)(b); i++)
#define rep(i, a) REP(i, 0, a)
#define EACH(i, a) for (auto i: a)
#define ITR(x, a) for (__typeof(a.begin()) x = a.begin(); x != a.end(); x++)
#define ALL(a) (a.begin()), (a.end())
#define ISIN(a, x) (a.find(x) != a.end())

int N, M;
int _s[300005], s[300005], _t[300005], t[300005];

template<class T> class RangeMinQuery {
 public:
    vector<T> dat;
    int n;
    // you may need to change MAX!
    T const MAX = 2147483647; //INT_MAX

    RangeMinQuery() {}
    RangeMinQuery(int N) {
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
  // breath deeply and calm down
  cin >> N >> M;
  rep(i, M) {
    cin >> _s[i] >> _t[i];
    _s[i]--, _t[i]--;
    s[i] = _s[i], t[i] = _t[i];
  }
  sort(s, s + M);
  sort(t, t + M);

  RangeMinQuery<int> rmq(N);
  int cnt = 0;
  int i = 0, j = 0;
  rep(p, N) {
    while (i < M && p == s[i]) {
      i++;
      cnt++;
    }

    rmq.update(p, cnt);

    while (j < M && p == t[j]) {
      j++;
      cnt--;
    }
  }

  vector<int> ans;
  rep(i, M) {
    if (rmq.query(_s[i], _t[i] + 1) > 1) ans.push_back(i + 1);
  }

  cout << ans.size() << endl;
  EACH(i, ans) cout << i << endl;

  return 0;
}
