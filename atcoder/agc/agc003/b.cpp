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
int A[100005];

int main(void) {
  cin.tie(0);
  ios::sync_with_stdio(false);

  cin >> N;
  ll ans = 0;
  rep(i, N) cin >> A[i];

  rep(i, N) {
    if (A[i]%2 && A[i + 1] > 0) {
      ans += 1;
      A[i] -= 1; 
      A[i + 1] -= 1;
    }
  }
  rep(i, N) {
    ans += A[i]/2;
    A[i] %= 2;
  }
  rep(i, N) {
    ll mn = min(A[i], A[i + 1]);
    ans += mn;
    A[i] -= mn;
    A[i + 1] -= mn;
  }

  cout << ans << endl;

  return 0;
}
