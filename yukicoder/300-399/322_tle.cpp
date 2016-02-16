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

int N;
int T[100005], D[100005];

int main(void) {
  cin >> N;
  rep(i, N) cin >> T[i];
  rep(i, N) cin >> D[i];
  
  ll ans = 0, s = 0;
  rep(i, N) {
    ans += D[i]*s + T[i]/2*D[i] + T[i];
    s += T[i];
  }
  cout << ans << endl;
  return 0;
}
