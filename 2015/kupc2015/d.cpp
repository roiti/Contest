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
ll A[100005];
ll B[100005];

int main(void) {
  cin >> N;
  rep(i, N) cin >> A[i];
  rep(i, N) cin >> B[i];
  ll money = 0;
  int pos = 0;
  ll mx = B[0];
  ll ans = mx * N;
  REP(day, 1, N + 1) {
    if (money + A[pos] >= 0) {
      money += A[pos];
      pos++;
      mx = max(mx, B[pos]);
      ans = max(ans, money + mx * (N - day));
    }
    else {
      money += mx;
      ans = max(ans, money);
    }
  }
  cout << ans << endl;
  return 0;
}
