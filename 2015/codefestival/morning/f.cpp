#include <bits/stdc++.h>
using namespace std;
typedef long long ll;

#define REP(i, a, b) for (int i = (int)(a); i < (int)(b); i++)
#define rep(i, a) REP(i, 0, a)
#define EACH(i, a) for (auto i: a)
#define ITR(x, a) for (__typeof(a.begin()) x = a.begin(); x != a.end(); x++)
#define ALL(a) (a.begin()), (a.end())
#define HAS(a, x) (a.find(x) != a.end())
#define endl '\n'

ll N, K;
ll A[100005];

int main(void) {
  cin >> N >> K;
  ll S = 0;
  rep(i, N) {
    cin >> A[i];
    S += A[i];
  }

  ll lo = 1, hi = (ll)1e14;
  while (hi - lo > 0) {
    ll mi = (lo + hi)/2;
    ll k = 0;
    rep(i, N) {
      k += max(0LL, A[i] - mi);
    }
    if (k <= K) {
      hi = mi;
    }
    else {
      lo = mi + 1;
    }
  }

  rep(i, N) {
    if (A[i] > hi) {
      K -= A[i] - hi;
      A[i] = hi;
    }
  }

  vector<pair<int,int>> seq;
  int l = 0, sp = 0;
  rep(i, N) {
    if (A[i] == hi) {
      if (l == 0) sp = i;
      l++;
    }
    else {
      if (l > 0) seq.push_back(make_pair(l, sp));
      l = 0;
    }
  }
  
  sort(seq.begin(), seq.end());
  for (auto p: seq) {
    rep(i, min(K, (ll)p.first)) A[i + p.second] -= 1;
    K = max(0LL, K - p.first);
  }

  ll ans = N + A[0] + 3*A[N - 1];
  rep(i, N - 1) {
    ans += abs(A[i] - A[i + 1]) + 2*A[i];
  }

  cout << ans << endl;

  return 0;
}
