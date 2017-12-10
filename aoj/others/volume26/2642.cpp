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

ll N, P, Q;
ll A[500005];
ll sum;

int main(void) {
  cin.tie(0);
  ios::sync_with_stdio(false);

  cin >> N >> P >> Q;
  rep(i, N) {
    ll C;
    cin >> C;
    sum += C;
    A[i] = C - (Q - i)*P;
  };

  sort(A, A + N);
  ll ans = sum;
  rep(i, N) {
    sum += 2*P*i - A[i];
    ans = max(ans, sum);
  }
  
  cout << ans << endl;

  return 0;
}
