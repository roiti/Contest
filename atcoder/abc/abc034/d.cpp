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

int N, K;
ll w[1005], p[1005];
bool used[1005];

int main(void) {
  cin.tie(0);
  ios::sync_with_stdio(false);
  
  cin >> N >> K;
  rep(i, N) cin >> w[i] >> p[i];

  double ok = 0, ng = 100;
  rep(loop, 100) {
    double md = (ok + ng)/2.0;

    vector<double> box;
    rep(i, N) box.push_back(-w[i]*(p[i]/100.0 - md));
    sort(box.begin(), box.end());

    double s = 0;
    rep(i, K) s += -box[i];
    if (s < 0) ng = md;
    else ok = md;
  }

  printf("%.10f\n", ok*100);

  return 0;
}
