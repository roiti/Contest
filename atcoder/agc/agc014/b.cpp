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

int N, M;
int a[100005], b[100005];
int cnt[100005];

int main(void) {
  cin.tie(0);
  ios::sync_with_stdio(false);
  // breath deeply and calm down

  cin >> N >> M;
  rep(i, M) cin >> a[i] >> b[i];
  rep(i, M) {
    a[i]--, b[i]--;
    if (a[i] > b[i]) swap(a[i], b[i]);
  }

  rep(i, M) {
    cnt[a[i]]++;
    cnt[b[i]]++;
  }

  bool ans = true;
  REP(i, 1, N) ans &= cnt[i]%2 == 0;

  cout << (ans ? "YES":"NO") << endl;
  return 0;
}
