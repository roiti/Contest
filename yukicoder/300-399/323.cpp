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
int w[3005];

int main(void) {
  cin >> n >> m;
  rep(i, n) cin >> w[i];
  int rem = n;
  int cur = 0;
  rep(i, n) cur += w[i];

  queue<pair<int, vector<bool>>> que;
  que.push(make_pair(cur, vector<bool>(n, false)));

  while (rem-- > m) {
    queue<pair<int, vector<bool>>> nque;
    int mx = -1e8;
    while (que.size()) {
      auto ele = que.front(); que.pop();
      int cur = ele.first;
      auto removed = ele.second;
      vector<int> pos;
      int decrease = 1e8;

      rep(i, n) {
        if (removed[i]) continue;
        int l = (i - 1 + n) % n, r = (i + 1) % n;
        int tmp = 0;
        if (!removed[l]) tmp += w[l];
        if (!removed[r]) tmp += w[i];
        if (tmp < decrease) {
          pos.clear();
          pos.push_back(i);
          decrease = tmp;
        }
        else if (tmp == decrease) {
          pos.push_back(i);
        }
      }
      for (auto i: pos) {
        mx = max(mx, cur - decrease);
        auto nremoved = removed;
        nremoved[i] = true;
        nque.push(make_pair(cur - decrease, nremoved));
      }
    }
    queue<pair<int, vector<bool>>> nnque;
    while (nque.size()) {
      auto ele = nque.front(); nque.pop();
      if (ele.first < mx) continue;
      nnque.push(ele);
    }
    que = nnque;
  }

  int ans = que.front().first;
  cout << ans << endl;

  return 0;
}
