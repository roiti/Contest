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

int N, Q;
ll d[1005];
vector<ll> l, g;
vector<pair<ll, ll>> a;

template<typename T> T gcd(T a, T b) {
  while (b) swap(a %= b, b);
  return a;
}

template<typename T> T lcm(T a, T b) {
  return a/gcd(a, b)*b;
}

bool judge(int x) {
  for (auto i = lower_bound(l.begin(), l.end(), x) - l.begin(); i > -1; i--) {
    if (l[i] > x) continue;
    cout << l[i] << " " << g[i] << endl;
    if (x % g[i] == 0) {
      return true; 
    }
  }
  return false;
}

int main(void) {
  cin.tie(0);
  ios::sync_with_stdio(false);

  cin >> N >> Q;
  rep(i, N) cin >> d[i];
  
  rep(i, N) REP(j, i, N) {
    a.push_back({lcm(d[i], d[j]), gcd(d[i], d[j])});
  }

  sort(a.begin(), a.end());

  rep(i, a.size()) {
    l.push_back(a[i].first);
    g.push_back(a[i].second);
  }

  rep(query, Q) {
    int x;
    cin >> x;
    cout << (judge(x) ? "YES":"NO") << endl;
  }
  return 0;
}
