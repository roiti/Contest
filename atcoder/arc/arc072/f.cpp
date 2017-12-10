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
#define mp(a, b) make_pair((a), (b))

int N, L;
int t[100005], v[100005];

int main(void) {
  cin >> N >> L;
  rep(i, N) cin >> t[i] >> v[i];

  priority_queue<pair<int, int>> que;

  double tv = 0.0;
  ll V = 0;
  rep(i, N) {
    V += v[i];
    tv += 1.0*t[i]*v[i];
    que.push(mp(-t[i], v[i]));
    while (true) {
      auto p = que.top();
      if (V - p.second <= L) {
          int d = V - L;
          V = L;
          tv -= -1.0*p.first*d;
          que.pop();
          que.push(mp(p.first, p.second - d));
          break;
      } else {
          V -= p.second;
          tv -= -1.0*p.first*p.second;
          que.pop();
      }
    }
    printf("%.10f\n", tv/L);
  }

  return 0;

}
