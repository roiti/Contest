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

int n;
int a[100005];

int main(void) {
  cin >> n;
  rep(i, n) cin >> a[i];

  int ans = 0;
  int mx = a[0], mn = a[0];
  int nmx = 1,  nmn = 1;
  queue<int> que;
  que.push(a[0]);
  REP(i, 1, n) {
    if (mx == mn) {
      if (a[i] > mx) {
        mn = mx;
        mx = a[i];
        nmn = nmx;
        nmx = 1;
      }
      else if (mn > a[i]) {
        mx = mn;
        mn = a[i];
        nmx = nmn;
        nmn = 1;
      }
      else {
        nmx++;
        nmn++;
      }
    }
    else {
      if (a[i] > mx) {
        while (nmn > 0) {
          if (que.front() == mn) nmn--;
          else if (que.front() == mx) nmx--;
          que.pop();
        }
        mn = mx;
        mx = a[i];
        nmn = max(1, nmx);
        nmx = 1;
      }
      else if (mn > a[i]) {
        while (nmx > 0) {
          if (que.front() == mn) nmn--;
          else if (que.front() == mx) nmx--;
          que.pop();
        }
        mx = mn;
        mn = a[i];
        nmx = max(1, nmn);
        nmn = 1;
      }
      else if (mn == a[i]) nmn++;
      else if (mx == a[i]) nmx++;
    }
    que.push(a[i]);
    ans = max(ans, (int)que.size());
  }

  cout << ans << endl;

  return 0;
}
