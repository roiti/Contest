#include <bits/stdc++.h>
using namespace std;
typedef long long ll;

#define REP(i, a, b) for (int i = (int)(a); i < (int)(b); i++)
#define rep(i, a) REP(i, 0, a)
#define EACH(i, a) for (auto i: a)
#define ITR(x, a) for (__typeof(a.begin()) x = a.begin(); x != a.end(); x++)
#define ALL(a) (a.begin()), (a.end())

string a, b;

string rec(string &a, int i, int n) {
  if (n % 2 == 1) return a.substr(i, n);
  string l = rec(a, i, n / 2);
  string r = rec(a, i + n / 2, n / 2);
  return min(l + r, r + l);
}

int main(void) {
  cin >> a;
  cin >> b;
  int n = a.size();
  cout << (rec(a, 0, n) == rec(b, 0, n) ? "YES":"NO") << endl;
  return 0;
}
