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

int K;
vector<pair<int, int>> ans;

void pb(int a, int b) {
  ans.push_back(make_pair(a, b));
}

int main(void) {
  // breath deeply and calm down
  cin >> K;
  if (K % 2 == 0) {
    cout << "NO" << endl;
    return 0;
  }

  // left group
  REP(i, 1, K) pb(1, i + 1);
  REP(i, 1, K) rep(j, K - 1) pb(i + 1, K + (K - 1) * (i - 1) + j + 1);
  for (int i = K; i < K * (K - 1); i += 2) pb(i + 1, i + 2);
  rep(i, K - 1) rep(j, K - 1) {
    int p = K + 1 + (K - 1) * i + j;
    rep(k, K - 1 - i - 1) {
      pb(p, p + (K - 1) * (k + 1));
    }
  }

  int m = K + (K - 1) * (K - 1);
  // right group
  REP(i, 1, K) pb(1 + m, i + 1 + m);
  REP(i, 1, K) rep(j, K - 1) pb(i + 1 + m, K + (K - 1) * (i - 1) + j + 1 + m);
  for (int i = K; i < K * (K - 1); i += 2) pb(i + 1 + m, i + 2 + m);
  rep(i, K - 1) rep(j, K - 1) {
    int p = K + 1 + (K - 1) * i + j + m;
    rep(k, K - 1 - i - 1) {
      pb(p, p + (K - 1) * (k + 1));
    }
  }

  // briedge
  pb(1, m + 1);

  cout << "YES" << endl;
  cout << 2 * (K + (K - 1) * (K - 1)) << " " << ans.size() << endl;
  EACH(it, ans) {
    printf("%d %d", it.first, it.second);
  }
  return 0;
}
