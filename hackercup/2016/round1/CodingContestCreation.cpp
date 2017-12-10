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
int D[100005];

int main(void) {
  cin >> T;
  int testcase = 0;
  while (testcase++ < T) {
    cin >> N;
    rep(i, N) cin >> D[i];

    int ans = 0;
    int four = 1;
    int cur = D[0];
    int i = 1;

    while (i < N) {
      //cout << cur << " ";
      if (four == 4) {
        cur = D[i];
        four = 1;
        i++;
        continue;
      }

      if (0 < D[i] - cur && D[i] - cur <= 10) {
        four += 1;
        cur = D[i];
        i++;
      } else if (D[i] - cur <= 0) {
        four += 1;
        ans++;
        cur = cur + 1;
      } else { // D[i] - cur > 10;
        four += 1;
        ans++;
        cur = cur + 10;
        while (cur >= D[i]) cur--;
      }
    }
    ans += 4 - four;

    assert((N + ans) % 4 == 0);
    printf("Case #%d: %d\n", testcase, ans);
  }

  return 0;
}
