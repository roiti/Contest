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
long a[100005], x;

long query(long x) {
  long s = 0;
  long res = 0;
  int i = 0;
  for (int j = 0; j < N; j++) {
    s += a[j];
    while (s > x) {
      res += (j - i);
      s -= a[i];
      i++;
    }
  }

  while (i < N) {
    res += (N - i);
    i++;
  }

  return res;
}

int main(void) {
  cin.tie(0);
  ios::sync_with_stdio(false);

  cin >> N >> Q;
  rep(i, N) cin >> a[i];
  rep(loop, Q) {
    cin >> x;
    cout << query(x) << endl;
  }
  return 0;
}
