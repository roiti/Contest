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
int a[100005];

int main(void) {
  cin.tie(0);
  ios::sync_with_stdio(false);

  cin >> N;
  rep(i, N) cin >> a[i];

  ll ans = N;
  int i = 0, j = 0;
  while (j < N) {
    while (j + 1 < N && a[j] < a[j + 1]) j++;
    ans += (ll)(j - i)*(j - i + 1)/2;
    i = j = j + 1;
  }

  cout << ans << endl;

  return 0;
}
