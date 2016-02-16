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
#define mp make_pair

int W, H, N;
int B[1005];
set<int> used;
set<pair<int, int>> X;
const int inf = (int)1e8;
int dx[] = {1, 0, -1, 0}, dy[] = {0, 1, 0, -1};

int main(void) {
  cin >> W >> H >> N;
  rep(i, N) {
    int M;
    cin >> M;
    rep(j, M + 1) cin >> B[j];
    rep(j, M) {
      if (abs(B[j] - B[j + 1])%W == 0 && B[j] > B[j + 1]) {
        for (int k = B[j + 1]; k < B[j]; k += W) X.insert(mp(k, k + W)), X.insert(mp(k + W, k));
      }
      else if (abs(B[j] - B[j + 1])%W == 0 && B[j] < B[j + 1]) {
        for (int k = B[j]; k < B[j + 1]; k += W) X.insert(mp(k, k + W)), X.insert(mp(k + W, k));
      }
      else if (B[j] > B[j + 1]) {
        for (int k = B[j + 1]; k < B[j]; k += 1) X.insert(mp(k, k + 1)), X.insert(mp(k + 1, k));
      }
      else if (B[j] < B[j + 1]) {
        for (int k = B[j]; k < B[j + 1]; k += 1) X.insert(mp(k, k + 1)), X.insert(mp(k + 1, k));
      }
    }
  }

  int ans = inf;
  priority_queue<pair<int, int>> que;
  que.push(mp(0, 0));
  while (!que.empty()) {
    auto ele = que.top(); que.pop();
    int cost = ele.first;
    if (ele.second == W*H - 1) {
      ans = cost;
      break;
    }
    int x = ele.second%W, y = ele.second/H;
    if (HAS(used, H*y + x)) continue;
    used.insert(H*y + x);

    rep(i, 4) {
      int nx = x + dx[i], ny = y + dy[i];
      if (!(0 <= nx && nx < W && 0 <= ny && ny < H)) continue;
      if (HAS(X, mp(H*y + x, H*ny + nx)) && !HAS(used, H*ny + nx)) {
        que.push(mp(cost + 1, H*ny + nx));
      }
    }
  }
  
  if (ans < inf) {
    cout << ans << endl;
  } else {
    cout << "Odekakedekinai.." << endl;
  }

  return 0;
}
