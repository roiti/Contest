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

int w, h, n;
set<int> X, Y;
map<int, int> W, H;

int main(void) {
  cin >> w >> h >> n;
  X.insert(0); X.insert(w);
  Y.insert(0); Y.insert(h);
  W[w] = 1;
  H[h] = 1;

  while(n--) {
    char c;
    int v;
    scanf("%s %d", &c, &v);
    if (c == 'V') {
      auto it = X.lower_bound(v);
      int xr = *it;
      it--;
      int xl = *it;
      if (W[xr - xl] == 1) W.erase(W.find(xr - xl));
      else W[xr - xl]--;
      W[xr - v]++;
      W[v - xl]++;
      X.insert(v);
    } else {
      auto it = Y.lower_bound(v);
      int yr = *it;
      it--;
      int yl = *it;
      if (H[yr - yl] == 1) H.erase(H.find(yr - yl));
      else H[yr - yl]--;
      H[yr - v]++;
      H[v - yl]++;
      Y.insert(v);
    }
    auto a = W.rbegin();
    auto b = H.rbegin();
    cout << (ll)(*a).first * (*b).first << endl;
  }

  return 0;
}
