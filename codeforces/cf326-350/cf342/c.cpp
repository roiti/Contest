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

int n, k;
int A[505][505];

int main(void) {
  cin.tie(0);
  ios::sync_with_stdio(false);

  cin >> n >> k;

  int cur = n*n;
  for (int i = n - 1; i >= 0; i--) {
    for (int j = n - 1; j >= k - 1; j--) {
      A[i][j] = cur;
      cur--;
    }
  }

  for (int i = n - 1; i >= 0; i--) {
    for (int j = n - 1; j >= 0; j--) {
      if (A[i][j] == 0) {
        A[i][j] = cur;
        cur--;
      }
    }
  }

  ll ans = 0;
  rep(i, n) {
    ans += A[i][k - 1];
  }

  cout << ans << endl;
  rep(i, n) {
    rep(j, n) {
      cout << A[i][j] << (j == n - 1 ? "\n":" ");
    }
  }
  return 0;
}
