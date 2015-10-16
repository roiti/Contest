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

int n, w;
int cnt[1100005];

int main(void) {
  cin >> n;
  rep(i, n) {
    scanf("%d", &w);
    cnt[w]++;
  }

  int ans = 0;
  rep(i, 1100002) {
    cnt[i + 1] += cnt[i] / 2;
    ans += cnt[i] % 2;
  }

  cout << ans << endl;

  return 0;
}
