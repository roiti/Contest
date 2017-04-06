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

ll mod_pow(ll a, ll p, ll mod) {
    ll res = 1;
    while (p) {
        if (p&1) res = res*a%mod;
        p /= 2;
        a = a*a%mod;
    }
    return res;
}

ll p(ll n, ll k, ll mod) {
    ll res = 1;
    for (int i = n; i > n - k; i--) res = res*i%mod;
    return res;
}

ll mod = 1e9 + 7;
int N, M;
ll ans[305];

ll solve() {
    ans[2] = 1;
    if (N > M) return 0;

    REP(i, 3, N + 1) ans[i] = ans[i - 1]*(i - 1)%mod; 
    REP(i, 2, N) ans[i] = 0;

    REP(i, N + 1, M + 1) {
        ans[i] = (N - 1)*ans[i - 1] + N*ans[i - 2] + (i - 1)*(N - 2)*ans[i - 1];
        ans[i] %= mod;
    }

    cout << ans[M] << endl;
    REP(i, N + 1, M + 1) ans[M] = (ans[M] + ans[i - 1]*p(M - 1, M - i + 1, mod))%mod;
    return ans[M];
}

int main(void) {
  cin.tie(0);
  ios::sync_with_stdio(false);

  cin >> N >> M;

  cout << solve() << endl;

  return 0;
}
