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

int main(void) {
  cin.tie(0);
  ios::sync_with_stdio(false);

  ll n;
  cin >> n;
  ll k;
  for (k = 1; (k + 1)*(k + 2)/2 < n; k++);
  cout << n - k*(k + 1)/2 << endl;

  return 0;
}
