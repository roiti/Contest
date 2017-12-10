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

const int inf = 1e8;
int N, S;
int a[100005];

int main(void) {
  cin.tie(0);
  ios::sync_with_stdio(false);

  cin >> N >> S;
  rep(i, N) cin >> a[i];

  int t = 0;
  int i = 0;
  int ans = inf;
  for (int j = 0; j < N; j++) {
    t += a[j];
    while (t >= S) {
      ans = min(ans, j - i + 1);
      t -= a[i];
      i += 1;
    } 
  }

  cout << (ans < inf ? ans:0) << endl;

  return 0;
}
