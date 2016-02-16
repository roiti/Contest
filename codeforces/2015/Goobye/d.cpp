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

const ll mod = (ll)1e9 + 7;
int n;
ll memo[5005][5005];
string s;

bool comp(int i, int j, int size) {
  rep(k, size) {
    if (s[i + k] > s[j + k]) return true;
    if (s[i + k] < s[j + k]) return false;
  }
  return false;
}

ll dfs(int k, int size) {
  if (k == n) return 1;
  if (memo[k][size]) return memo[k][size];
  if (s[k] == '0') return 0;
  ll res = 0;
  REP(i, k + size, n + 1) {
    if (i - k == size && comp(k, k - size, size)) res = (res + dfs(i, i - k)) % mod;
    else if (i - k > size) res = (res + dfs(i, i - k)) % mod;
  }
  memo[k][size] = res;
  return res;
}

int main(void) {
  cin >> n;
  cin >> s;

  cout << dfs(0, 0) << endl;
  return 0;
}
