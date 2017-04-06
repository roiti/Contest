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
#define mp(a, b) make_pair(a, b)

int N;
int R, C;
vector<pair<int, int>> A;
map<pair<int, int>, ll> M;

bool is_inside(int r, int c) {
  return (0 <= r && r < R && 0 <= c && c < C);
}

bool calc_cell(int vr, int vc, int pr, int pc, int r1, int c1, int r2, int c2) {
  pair<int, int> vp = mp(vr, vc), pp = mp(pr, pc), p1 = mp(r1, c1), p2 = mp(r2, c2);
  if (HAS(M, vp)) {
    if (HAS(M, pp) && HAS(M, p1) && HAS(M, p2)) {
      return (M[vp] + M[pp] == M[p1] + M[p2]);
    }
  } else {
    if (HAS(M, pp) && HAS(M, p1) && HAS(M, p2)) {
      ll va = M[p1] + M[p2] - M[pp];
      if (va < 0) return false;
      A.push_back(vp);
      M[vp] = va;
    }
  }
  return true;
}

bool check_cell(int r1, int c1, int r2, int c2, int r3, int c3, int r4, int c4) {
  if (is_inside(r1, c1) && is_inside(r2, c2) && is_inside(r3, c3) && is_inside(r4, c4)) {
    pair<int, int> p1 = mp(r1, c1), p2 = mp(r2, c2), p3 = mp(r3, c3), p4 = mp(r4, c4);
    if (HAS(M, p1) && HAS(M, p2) && HAS(M, p3) && HAS(M, p4)) {
      return (M[p1] - M[p2] == M[p3] - M[p4]);
    }
  }
  return true;
}

bool check_cell2(int r, int c) {
  int r1 = r - 1, c1 = c - 1;
  int r2 = r + 1, c2 = c - 1;
  int r3 = r - 1, c3 = c + 1;
  int r4 = r + 1, c4 = c + 1;
  if (is_inside(r1, c1) && is_inside(r2, c2) && is_inside(r3, c3) && is_inside(r4, c4)) {
    pair<int, int> p1 = mp(r1, c1), p2 = mp(r2, c2), p3 = mp(r3, c3), p4 = mp(r4, c4);
    if (HAS(M, p1) && HAS(M, p2) && HAS(M, p3) && HAS(M, p4)) {
      return (M[p1] - M[p2] == M[p3] - M[p4]) && (M[p1] - M[p3] == M[p2] - M[p4]);
    }
  }
  return true;

}
int main(void) {
  cin.tie(0);
  ios::sync_with_stdio(false);

  cin >> R >> C;
  cin >> N;
  rep(i, N) {
    int r, c, a;
    cin >> r >> c >> a;
    r--; c--;
    A.push_back(make_pair(r, c));
    M[mp(r, c)] = a; 
  }

  bool ok = true;
  for (int i = 0; i < A.size(); i++) {
    int r = A[i].first, c = A[i].second;
    ll a = M[mp(r, c)];

    int r1 = r - 1, c1 = c - 1;
    int r2 = r - 1, c2 = c;
    int r3 = r - 1, c3 = c + 1;
    int r4 = r, c4 = c - 1;
    int r5 = r, c5 = c + 1;
    int r6 = r + 1, c6 = c - 1;
    int r7 = r + 1, c7 = c;
    int r8 = r + 1, c8 = c + 1;

    // up left
    if (is_inside(r1, c1)) {
      ok = calc_cell(r1, c1, r, c, r2, c2, r4, c4) &&
           calc_cell(r2, c2, r4, c4, r1, c1, r, c) &&
           calc_cell(r4, c4, r2, c2, r1, c1, r, c);
      if (!ok) break;
    }
    //cout << "ul" << endl;
  
    // up right
    if (is_inside(r3, c3)) {
      ok = calc_cell(r3, c3, r, c, r2, c2, r5, c5) &&
           calc_cell(r2, c2, r5, c5, r, c, r3, c3) &&
           calc_cell(r5, c5, r2, c2, r, c, r3, c3);
      if (!ok) break;
    }
    //cout << "ur" << endl;
  
    // down left 
    if (is_inside(r6, c6)) {
      ok = calc_cell(r6, c6, r, c, r4, c4, r7, c7) &&
           calc_cell(r4, c4, r7, c7, r, c, r6, c6) &&
           calc_cell(r7, c7, r4, c4, r, c, r6, c6);
      if (!ok) break;
    }
    //cout << "dl" << endl;
  
    // down right
    if (is_inside(r8, c8)) {
      ok = calc_cell(r8, c8, r, c, r5, c5, r7, c7) &&
           calc_cell(r5, c5, r7, c7, r, c, r8, c8) &&
           calc_cell(r7, c7, r5, c5, r, c, r8, c8);
      if (!ok) break;
    }
    //cout << "dr" << endl;
    
    ok = check_cell(r, c, r4, c4, r + 2, c, r + 2, c - 1) &&
         check_cell(r, c, r4, c4, r - 2, c, r - 2, c - 1) &&
         check_cell(r, c, r5, c5, r + 2, c, r + 2, c + 1) &&
         check_cell(r, c, r5, c5, r - 2, c, r - 2, c + 1) &&
         check_cell(r, c, r2, c2, r, c + 2, r + 1, c + 2) &&
         check_cell(r, c, r2, c2, r, c - 2, r + 1, c - 2) &&
         check_cell(r, c, r7, c7, r, c + 2, r - 1, c + 2) &&
         check_cell(r, c, r7, c7, r, c - 2, r - 1, c - 2);
    if (!ok) break;

    ok = check_cell2(r, c);
    if (!ok) break;
  }

  cout << (ok ? "Yes":"No") << endl;
}
