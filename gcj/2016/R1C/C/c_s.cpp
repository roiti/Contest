#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
template<typename T> using Graph = vector<vector<T>>;

#define REP(i, a, b) for (int i = (int)(a); i < (int)(b); i++)
#define rep(i, a) REP(i, 0, a)
#define EACH(i, a) for (auto i: a)
#define ITR(x, a) for (__typeof(a.begin()) x = a.begin(); x != a.end(); x++)
#define ALL(a) (a.begin()), (a.end())
#define HAS(a, x) (a.find(x) != a.end())
#define endl '\n'

int T;
int J, P, S, K;
int cjp[11][11], cjs[11][11], cps[11][11];

int main(void) {
  cin.tie(0);
  ios::sync_with_stdio(false);

  cin >> T;
  REP(test, 1, T + 1) {
    cin >> J >> P >> S >> K;
    vector<tuple<int,int,int>> comb;
    REP(j, 1, J + 1) REP(p, 1, P + 1) REP(s, 1, S + 1) comb.push_back(make_tuple(j, p, s));

    while (true) {
      int idx = 0;
      int mn = 0;
      int summing = 0;
      rep(x, comb.size()) {
        int jp = 0, js = 0, ps = 0;
        int jx = get<0>(comb[x]);
        int px = get<1>(comb[x]);
        int sx = get<2>(comb[x]);
        rep(y, comb.size()) {
          if (x == y) continue;
          int jy = get<0>(comb[y]);
          int py = get<1>(comb[y]);
          int sy = get<2>(comb[y]);
          if (jx == jy && px == py) jp++;
          if (jx == jy && sx == sy) js++;
          if (px == py && sx == sy) ps++;
        }
        if (max(jp, max(js, ps)) > mn) {
          mn = max(jp, max(js, ps));
          summing = jp + js + ps;
          idx = x;
        }
        if (max(jp, max(js, ps)) == mn) {
          if (jp + js + ps > summing) {
            mn = max(jp, max(js, ps));
            summing = jp + js + ps;
            idx = x;
          }
        }
      }
      
      rep(j, J + 1) rep(p, P + 1) rep(s, S + 1) cjp[j][p] = 0, cjs[j][s] = 0, cps[p][s] = 0;
      rep(x, comb.size()) {
        int j = get<0>(comb[x]);
        int p = get<1>(comb[x]);
        int s = get<2>(comb[x]);
        cjp[j][p] += 1;
        cjs[j][s] += 1;
        cps[p][s] += 1;
      }

      int k = 0;
      rep(j, J + 1) rep(p, P + 1) rep(s, S + 1) k = max(k, max(cjp[j][p], max(cjs[j][s], cps[p][s])));
      if (k <= K) { 
        printf("Case #%d: %d\n", test, (int)comb.size());
        for (auto ele: comb) {
          printf("%d %d %d\n", get<0>(ele), get<1>(ele), get<2>(ele)); 
        }
        break;
      }
      comb.erase(comb.begin() + idx);
    }
  }
  
  return 0;
}
