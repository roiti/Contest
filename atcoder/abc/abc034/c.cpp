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
ll H, W;
int k[200005];

ll pow_mod(ll a, ll p, ll mod) {
  ll res = 1;
  while (p) {
    if (p & 1) res = (res * a) % mod;
    a = (a * a) % mod;
    p /= 2;
  }
  return res;
}

void count_factor(int n, int coeff = 1) {
  int i = 2;
  while (i * i<= n) {
    int cnt = 0;
    while (n % i == 0) {
      n /= i;
      k[i] += coeff;
    }
    i++;
  }
  if (n > 1) k[n] += coeff;
}

int main(void) {
  cin.tie(0);
  ios::sync_with_stdio(false);

  cin >> H >> W;
  H--, W--;
  REP(i, W + 1, H + W + 1) count_factor(i); 
  REP(i, 2, H + 1) count_factor(i , -1);

  ll ans = 1;
  rep(i, 200005) {
    ans = ans * pow_mod(i, k[i], mod) % mod;
  }
  cout << ans << endl;

  return 0;
}
