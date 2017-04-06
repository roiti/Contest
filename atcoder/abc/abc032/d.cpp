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

int N, W;
ll v[205], w[205];
ll dp[200010];

void solve1() {
  vector<pair<ll, ll>> s1, s2;
  int L = min(N, 15);
  rep(mask, 1 << L) {
    ll tv = 0, tw = 0;
    rep(i, L) if (mask&(1 << i)) tv += v[i], tw += w[i];
    if (tw <= W) s1.push_back({tw, tv});
  }

  L = max(0, N - 15);
  rep(mask, 1 << L) {
    ll tv = 0, tw = 0;
    rep(i, L) if (mask&(1 << i)) tv += v[i + 15], tw += w[i + 15];
    if (tw <= W) s2.push_back({tw, tv});
  }

  sort(ALL(s1));
  sort(ALL(s2));

  rep(i, s1.size() - 1) s1[i + 1].second = max(s1[i].second, s1[i + 1].second);
  rep(i, s2.size() - 1) s2[i + 1].second = max(s2[i].second, s2[i + 1].second);

  ll res = 0;
  int y = s2.size() - 1;
  rep(x, s1.size()) {
    while (y >= 0 && s1[x].first + s2[y].first > W) y--;
    res = max(res, s1[x].second + s2[y].second);
  }

  cout << res << endl;
}

void solve2() {
  rep(i, N) {
    for (int j = 200000 - w[i]; j >= 0; j--) if (dp[j]) dp[j + w[i]] = max(dp[j + w[i]], dp[j] + v[i]);
    dp[w[i]] = max(dp[w[i]], v[i]);
  }

  ll res = *max_element(dp, dp + W + 1);
  
  cout << res << endl;
}

void solve3() {
  fill(dp, dp + 200010, (ll)1e15);
  rep(i, N) {
    for (int j = 200000 - v[i]; j >= 0; j--) dp[j + v[i]] = min(dp[j + v[i]], dp[j] + w[i]);
    dp[v[i]] = min(dp[v[i]], w[i]);
  }

  ll res = 0;
  rep(i, 200010) if (dp[i] <= W) res = i;
  
  cout << res << endl;
}

int main(void) {
  cin >> N >> W;
  rep(i, N) cin >> v[i] >> w[i];

  ll mxv = 0, mxw = 0;
  rep(i, N) mxv = max(mxv, v[i]), mxw = max(mxw, w[i]);

  if (N <= 30) solve1();
  else if (mxw <= 1000) solve2();
  else if (mxv <= 1000) solve3();

  return 0;
}
