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

int n, m;
string x, y;

int gcd(int a, int b) {
  while (b) swap(a%b, b);
  return a;
}

int main(void) {
  cin >> n >> m;
  cin >> x >> y;
  if (x.size > y.size()) swap(x, y), swap(n, m);
  int lx = x.size(), ly = y.size();
  int g = gcd(lx, ly);

  ll ans = 0;
  
  return 0;
}
