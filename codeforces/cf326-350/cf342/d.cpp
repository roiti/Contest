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

string n;

int main(void) {
  cin.tie(0);
  ios::sync_with_stdio(false);

  cin >> n;
  int k = n.size();

  // n < 10
  if (k == 1) {
    if ((n[0] - '0') % 2 == 0) cout << (n[0] - '0')/2 << endl;
    else cout << 0 << endl;
    return 0;
  }

  string a(m, '0');

  // kuriagari
  int k;
  if (a[0] == 1 || a[0] - a[m - 1] == 1) {
    k = true;
  } else if (a[0] - a[m - 1] == 0) {
    k = false;
  } else {
    // no solution
    cout << 0 << endl;
    return 0;
  }

  rep(i, m/2) {
    if (n[i] != n[m - i - 1]) {
      cout << 0 << endl;
      return 0;
    }
    a[i] = '0' + (n[i] - '0' + 1)/2;
    a[n - i - 1] = '0' + (n[i] - '0')/2;
  }
  cout << a << endl;

  return 0;
}
