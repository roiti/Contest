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

const ll mod = (ll)1e9 + 7;
ll N;

ll b2n(string b) {
  ll res = 0;
  rep(i, b.size()) {
    res = 2*res + (b[i] - '0'); 
  }
  return res;
}

int main(void) {
  cin.tie(0);
  ios::sync_with_stdio(false);

  cin >> N;

  int k = 0, x = 1;
  while (x < N) x *= 2, k += 1;

  ll ans = 0;
  string b = "1";
  
  while (b2n(b) <= N) {
    rep(a, k - b.size() + 1) {
      
    }
  }
  return 0;
}
