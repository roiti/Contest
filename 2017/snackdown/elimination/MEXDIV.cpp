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

int n, k;
int A[500005];
ll dp[500005];
map<int, int> cnt;
set<int> s;

ll pow_mod(int a, int p, ll mod) {
  ll res = 1;
  while (p) {
    if (p&1) res = res*a % mod;
    a = a*a % mod;
    p /= 2;
  }
  return res;
}

int main(void) {
  cin.tie(0);
  ios::sync_with_stdio(false);

  cin >> n >> k;
  rep(i, n) cin >> A[i];

  int i = 0;
  dp[0] = 1;
  if (A[0] <= k) {
      cnt[A[0]]++;
      s.insert(A[0]);
  }

  REP(j, 1, n) {
    dp[j] = dp[j - 1]*2 % mod;
    if (A[j] <= k) {
        cnt[A[j]]++;
        s.insert(A[j]);
    }
    if (s.size() == k + 1) {
      ll tmp = 0;
      while (1) {
        tmp = (tmp + (i - 1 >= 0 ? dp[i - 1]:1)) % mod;
        if (A[i] <= k) {
          cnt[A[i]]--;
          if (cnt[A[i]] == 0) {
            s.erase(A[i]);
            i++;
            break;
          }
        }
        i++;
      }
      dp[j] = (dp[j] - tmp + mod) % mod; 
    }
  }

  cout << dp[n - 1] << endl;
  
  return 0;
}
