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

int N;
vector<int> a[100010];
bitset<200020> bs;
bitset<200020> ts;

int main(void) {
  cin.tie(0);
  ios::sync_with_stdio(false);

  cin >> N;
  int ai, bi;
  rep(i, N) cin >> ai, a[ai].push_back(i);
  rep(i, N) cin >> bi, bs[i] = bi;

  rep(i, 100010) if (a[i].size()) {
    bitset<200020> t;
    for (auto v: a[i]) t |= bs << v;
    ts ^= t;
  }

  rep(i, 2*N - 1) printf("%s\n", ts[i] ? "ODD":"EVEN");
  return 0;
}
