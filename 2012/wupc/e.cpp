#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
template<typename Cost> using Graph = vector<vector<Cost>>;

#define REP(i, a, b) for (int i = (int)(a); i < (int)(b); i++)
#define rep(i, a) REP(i, 0, a)
#define EACH(i, a) for (auto i: a)
#define ICostR(x, a) for (__typeof(a.begin()) x = a.begin(); x != a.end(); x++)
#define ALL(a) (a.begin()), (a.end())
#define HAS(a, x) (a.find(x) != a.end())
#define endl '\n'

template<typename Cost>
struct edge { int to; Cost cost; };
typedef edge<ll> Edge;

const int mod = 28;
const ll inf = (ll)1e9;
int N, M;
ll d[1005][mod];

template<class Cost>
void dijkstra(const Graph<edge<Cost>> &G, int s) {
  typedef pair<Cost, int> Pair;
  typedef edge<Cost> Edge;
  const Cost inf = (Cost)1e9;

  rep(i, N) rep(j, mod) d[i][j] = inf;
  int V = G.size();
  priority_queue<Pair, vector<Pair>, greater<Pair>> que;
  d[s][0] = 0;
  que.push(Pair(0, s));

  while (!que.empty()) {
    Pair p = que.top(); que.pop();
    int v = p.second;
    if (v == V - 1) continue;

    for (int i = 0; i < G[v].size(); i++) {
      edge<Cost> e = G[v][i];
      Cost next_d = p.first + e.cost;
      if (d[e.to][next_d%mod] > d[v][p.first%mod] + e.cost) {
        d[e.to][next_d%mod] = d[v][p.first%mod] + e.cost;
        que.push(Pair(next_d, e.to));
      }
    }
  }
}

int main(void) {
  cin.tie(0);
  ios::sync_with_stdio(false);

  cin >> N >> M;
  Graph<Edge> G(N);

  rep(i, M) {
    int f, t;
    ll c;
    cin >> f >> t >> c;
    G[f].push_back(Edge{t, c});
    G[t].push_back(Edge{f, c});
  }

  dijkstra(G, 0);

  ll ans = inf;
  rep(i, mod) {
    if (i%4 == 0 || i%7 == 0) {
      ans = min(ans, d[N - 1][i]);
    }
  }

  cout << (ans < inf ? ans:-1) << endl;

  return 0;
}
