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
const int W = 1005, H = 1005;
int A[W][H];

int main(void) {
  cin.tie(0);
  ios::sync_with_stdio(false);

  cin >> N;
  rep(i, N) {
    int x, y;
    cin >> x >> y;
    A[y][x] = 1;
  }

  ll ans = 0;
  // / direction
  for (int sx = -H; sx < W; sx++) {
    int cnt = 0;
    for (int y = max(0, -sx); y < min(H, W - sx); y++) {
      int x = sx + y;
      if (A[y][x] == 1) cnt++; 
    }
    ans += (ll)cnt*(cnt - 1)/2;
  }

  // \ direction
  for (int sx = 0; sx < W + H; sx++) {
    int cnt = 0;
    for (int y = max(0, sx - W); y < min(H, sx); y++) {
      int x = sx - y;
      if (A[y][x] == 1) cnt++; 
    }
    ans += (ll)cnt*(cnt - 1)/2;
  }

  cout << ans << endl;

  return 0;
}
