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

string S;
int M;

int main(void) {
  cin.tie(0);
  ios::sync_with_stdio(false);

  cin >> S;
  int N = S.size();
  map<string, int> mp; 
  rep(i, N) {
    string t;
    REP(j, i, min(i + 10, N)) {
      t += S[j];
      mp[t]++;
    }
  }

  ll ans = 0;
  cin >> M;
  rep(loop, M) {
    string C;
    cin >> C;
    ans += mp[C];
  }
  cout << ans << endl;

  return 0;
}
