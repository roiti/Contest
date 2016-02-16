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

int X, Y, x, y;
string s;
int ans[100005];
bool used[505][505];

int main(void) {
  cin >> X >> Y >> x >> y;
  cin >> s;
  int n = s.size();
  used[y][x] = true;
  ans[0] = 1;
  rep(i, n) {
    if (s[i] == 'U') if (x > 1) x--;
    if (s[i] == 'D') if (x < X) x++;
    if (s[i] == 'L') if (y > 1) y--;
    if (s[i] == 'R') if (y < Y) y++;

    if (!used[y][x]) ans[i + 1] = 1;
    else ans[i + 1] = 0;

    used[y][x] = true;
  }

  REP(i, 1, Y + 1)
    REP(j, 1, X + 1)
      if (!used[i][j]) ans[n]++;

  rep(i, n + 1) cout << ans[i] << (i == n ? "\n":" ");

  return 0;
}
