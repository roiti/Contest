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

int T;
int N, K, M;

int solve() {
  vector<pair<int, int>> V, H;
  cin >> N >> K >> M;
  int D = (N - K)/2;

  rep(i, M) {
    int hx, hy, tx, ty;
    cin >> hx >> hy >> tx >> ty;
    hx--; hy--; tx--; ty--;

    // vertical side wall
    if (hx < D && tx < D || hx >= N - D && tx >= N - D) {
      if (hy > ty) swap(hy, ty);
      if (ty < D || hy >= N - D) continue;
      hy = max(hy, D);
      ty = min(ty, N - D - 1);
      V.push_back(make_pair(hy, ty));
    }

    // horizontal side wall
    if (hy < D && ty < D || hy >= N - D && ty >= N - D) {
      if (hx > tx) swap(hx, tx);
      if (tx < D || hx >= N - D) continue;
      hx = max(hx, D);
      tx = min(tx, N - D - 1);
      H.push_back(make_pair(hx, tx));
    }
  }
  
  sort(V.begin(), V.end());
  sort(H.begin(), H.end());

  int ans = 0;
  // Vertical
  int i = 0, t = D - 1;
  while (i < V.size() && t < N - D - 1) {
    int nt = t;
    ans++;
    bool flag = false;
    while (i < V.size()) {
      auto p = V[i];
      if (p.first <= t + 1) {
          nt = max(p.second, nt);
          flag = true;
          i++;
      } else {
          break;
      }
    }
    if (!flag) break;
    t = nt;
  }
 
  if (t < N - D - 1) return -1;

  // Horizontal
  i = 0; t = D - 1;
  while (i < H.size() && t < N - D - 1) {
    int nt = t;
    ans++;
    bool flag = false;
    while (i < H.size()) {
      auto p = H[i];
      if (p.first <= t + 1) {
          nt = max(p.second, nt);
          flag = true;
          i++;
      } else {
          break;
      }
    }
    if (!flag) break;
    t = nt;
  }

  if (t < N - D - 1) return -1;

  return ans;
}

int main(void) {
  cin.tie(0);
  ios::sync_with_stdio(false);

  cin >> T;

  while (T--) {
    cout << solve() << endl;
  }

  return 0;
}
