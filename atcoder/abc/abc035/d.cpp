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

struct edge { int to; int cost; };
int N, M, T;
ll A[100005];

// dijkstra not work for Graph has negative edge
// O(|E|log(|V|))

vector<ll> dijkstra(vector<vector<edge>> &G, int s) {
  const ll inf = (ll)1e11;
  typedef pair<ll, int> P;
  priority_queue<P, vector<P>, greater<P>> que;
  vector<ll> d(N, inf);
  d[s] = 0;
  que.push(P(0LL, s));

  while (!que.empty()) {
    P p = que.top(); que.pop();
    int v = p.second;
    if (d[v] < p.first) continue;
    for (int i = 0; i < G[v].size(); i++) {
      edge e = G[v][i];
      if (d[e.to] > d[v] + e.cost) {
        d[e.to] = d[v] + e.cost;
        que.push(P(d[e.to], e.to));
      }
    }
  }
  return d;
}

int main(void) {
  cin.tie(0);
  ios::sync_with_stdio(false);

  cin >> N >> M >> T;
  rep(i, N) cin >> A[i];

  vector<vector<edge>> G(N), rG(N);
  rep(i, M) {
    int a, b, c;
    cin >> a >> b >> c;
    a--, b--;
    G[a].push_back(edge{b, c});
    rG[b].push_back(edge{a, c});
     
  } 
  vector<ll> go = dijkstra(G, 0); 
  vector<ll> back = dijkstra(rG, 0);

  ll ans = 0;
  rep(i, N) ans = max(ans, A[i]*max(0LL, T - go[i] - back[i])); 
  
  cout << ans << endl;

  return 0;
}
