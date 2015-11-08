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

int n, p;
string s, abc, cba;

bool ok(string &s) {
  int n = s.size();
  rep(i, n - 1) if (s[i] == s[i + 1]) return false;
  rep(i, n - 2) if (s[i] == s[i + 2]) return false;
  return true;
}

int main(void) {
  cin >> n >> p;
  cin >> s;
  rep(i, n + 3) {
    abc += 'a' + i % 3;
    cba += 'c' - i % 3;
  }
  for (int i = n - 1; i >= 0; i--) {
    REP(x, 'a', 'z' + 1) if (s[i] < x && x - 'a' < p){
      string t[6];
      rep(j, 3) {
        t[j]     = s.substr(0, i) + (char)x + abc.substr(j, n - (i + 1));
        t[j + 3] = s.substr(0, i) + (char)x + cba.substr(j, n - (i + 1));
      }
      sort(t, t + 6);
      rep(j, 6) if (ok(t[j])) {
        cout << t[j] << endl;
        return 0;
      }
    }
  }

  cout << "NO" << endl;

  return 0;
}
