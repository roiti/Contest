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

typedef pair<int, int> P;
const int INF = 100000000;
int N, M, R, T;
struct edge {int to, cost;};
vector<edge> G[100005];

vector<int> dijkstra(int s) {
  priority_queue<P, vector<P>, greater<P>> que;
  vector<int> cost(N, INF);
  cost[s] = 0;
  que.push(P(0, s));
  while (!que.empty()) {
    P p = que.top(); que.pop();
    int v = p.second;
    if (cost[v] < p.first) continue;
    EACH(e, G[v]){
      if (cost[e.to] > cost[v] + e.cost) {
        cost[e.to] = cost[v] + e.cost;
        que.push(P(cost[e.to], e.to));
      }
    }
  }
  return cost;
}

int main(void) {
  cin >> N >> M >> R >> T;
  rep(i, M) {
    int a, b, c;
    cin >> a >> b >> c;
    a--, b--;
    G[a].push_back(edge{b, c});
    G[b].push_back(edge{a, c});
  }

  ll ans = 0;
  double C = 1.0 * R / T;
  rep(A, N) {
    auto cost = dijkstra(A);
    sort(ALL(cost));
    REP(i, 1, N) {
      ans += (int)(cost.end() - lower_bound(cost.begin(), cost.end(), C * cost[i] + 1e-8));
      if (R < T) ans--;
    }
  }
  cout << ans << endl;

  return 0;
}
