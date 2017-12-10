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

int R, C, M, N;
int A[51][51];
int r[5001][2];
int c[5001][2];

int main(void) {
  cin.tie(0);
  ios::sync_with_stdio(false);

  cin >> R >> C >> M;
  cin >> N;
  rep(i, N) {
    cin >> r[i][0] >> r[i][1];
    cin >> c[i][0] >> c[i][1];
  }

  vector<int> ans;
  rep(y, R) rep(x, C) A[y][x] = 0; 
  rep(i, N) {
    REP(y, r[i][0] - 1, r[i][1]) {
      REP(x, c[i][0] - 1, c[i][1]) {
        A[y][x] = (A[y][x] + 1) % 4;
      }
    }
  }

  rep(i, N) {
    REP(y, r[i][0] - 1, r[i][1]) {
      REP(x, c[i][0] - 1, c[i][1]) {
        A[y][x] = (A[y][x] - 1 + 4) % 4;
      }
    }    
    int cnt = 0;
    rep(y, R) rep(x, C){
      if (A[y][x] == 0) cnt++;
    }
    if (cnt == M) {
      ans.push_back(i + 1);
    }
    REP(y, r[i][0] - 1, r[i][1]) {
      REP(x, c[i][0] - 1, c[i][1]) {
        A[y][x] = (A[y][x] + 1) % 4;
      }
    }    
  }

  for (auto k: ans) cout << k << endl;

  return 0;
}
