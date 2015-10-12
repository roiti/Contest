#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
typedef pair<int, int> pi;
typedef map<pi, pair<int, ll>> MAP;

#define REP(i, a, b) for (int i = (int)(a); i < (int)(b); i++)
#define rep(i, a) REP(i, 0, a)
#define EACH(i, a) for (auto i: a)
#define ITR(x, a) for (__typeof(a.begin()) x = a.begin(); x != a.end(); x++)
#define ALL(a) (a.begin()), (a.end())
#define HAS(a, x) (a.find(x) != a.end())
#define endl '\n'

const int INF = (int)1e9;
int N;
int l[30], m[30], w[30];

void dfs(MAP &comb, int i, int n, int x, int y, int z, ll s) {
  if (i == n) {
    pi ofs = make_pair(x - y, x - z);
    if (HAS(comb, ofs)) comb[ofs] = max(comb[ofs], make_pair(x, s));
    else comb[ofs] = make_pair(x, s);
    return;
  }
  dfs(comb, i + 1, n, x, y + m[i], z + w[i], 3 * s);
  dfs(comb, i + 1, n, x + l[i], y, z + w[i], 3 * s + 1);
  dfs(comb, i + 1, n, x + l[i], y + m[i], z, 3 * s + 2);
}

int main(void) {
  cin >> N;
  rep(i, N) cin >> l[i] >> m[i] >> w[i];

  MAP comb1, comb2;
  dfs(comb1, 0, N / 2, 0, 0, 0, 0);
  dfs(comb2, N / 2, N, 0, 0, 0, 0);

  string ans[25];
  const string C[] = {"MW", "LW", "LM"};
  int mx = -INF;
  ITR(it, comb1) {
    pi ofs = (*it).first;
    int x1 = comb1[ofs].first;
    ll  s1 = comb1[ofs].second;
    pi rofs = make_pair(-ofs.first, -ofs.second);
    if (HAS(comb2, rofs)) {
      int x2 = comb2[rofs].first;
      ll  s2 = comb2[rofs].second;
      if (x1 + x2 < mx) continue;
      mx = x1 + x2;
      REP(i, 0, N / 2) {
        ans[i] = C[s1 % 3];
        s1 /= 3;
      }
      reverse(ans, ans + (N / 2));
      REP(i, N / 2, N) {
        ans[i] = C[s2 % 3];
        s2 /= 3;
      }
      reverse(ans + (N / 2), ans + N);
    }
  }

  if (mx > -INF) {
    rep(i, N) cout << ans[i] << endl;
  } else {
    cout << "Impossible" << endl;
  }

  return 0;
}
