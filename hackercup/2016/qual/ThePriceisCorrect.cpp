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

int T, N;
ll P;
ll B[100005], S[100005];

int main(void) {
  cin >> T;
  int ncase = 0;
  while (T--) {
    ncase++;
    cin >> N >> P;
    rep(i, N) cin >> B[i];
    rep(i, N) S[i + 1] = S[i] + B[i];
    
    ll ans = 0;
    rep(i, N) {
      int lo = i, hi = N;
      while (hi > lo) {
        int mid = (lo + hi)/2;
        if (S[mid] - S[i] > P) {
          hi = mid - 1;
        } else {
          lo = mid + 1;
        }
      }
      while (S[hi] - S[i] > P) hi--;
      //cout << i << " " << hi << endl;
      ans += hi - i;
    }
    printf("Case #%d: %lld\n", ncase, ans);
  }
  return 0;
}
