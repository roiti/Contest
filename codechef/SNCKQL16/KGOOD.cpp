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

int T, K;

int main(void) {
  cin.tie(0);
  ios::sync_with_stdio(false);

  cin >> T;
  while (T--) {
    vector<int> alpha(26);
    string w;
    cin >> w >> K;

    rep(i, w.size()) alpha[w[i] - 'a']++;

    int ans = w.size();
    rep(i, 26) {
      if (alpha[i] == 0) continue;
      // alpha[i] is min
      int tmp = 0;
      rep(j, 26) {
        if (j == i) continue;
        if (alpha[j] < alpha[i]) tmp += alpha[j];
        if (alpha[j] > alpha[i] + K) tmp += alpha[j] - (alpha[i] + K);
      } 
      ans = min(ans, tmp);
    }
    cout << ans << endl;
  }

  return 0;
}
