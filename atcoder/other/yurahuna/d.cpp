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

string S1, S2, S3;
int C1[26], C2[26], C3[26];

int main(void) {
  cin.tie(0);
  ios::sync_with_stdio(false);

  cin >> S1;
  cin >> S2;
  cin >> S3;

  rep(i, S1.size()) C1[S1[i] - 'A']++;
  rep(i, S2.size()) C2[S2[i] - 'A']++;
  rep(i, S3.size()) C3[S3[i] - 'A']++;

  rep(i, 26) {
    C1[i] = min(C1[i], C3[i]);
    C2[i] = min(C2[i], C3[i]);
  }

  int r1 = S1.size()/2, r2 = S2.size()/2;
  rep(i, 26) {
    if (C3[i] > C1[i] + C2[i]) {
      cout << "NO" << endl;
      return 0;
    } else if (C3[i] == C1[i] + C2[i]) {
      r1 -= C1[i];
      r2 -= C2[i];
    } else if (C1[i] == 0 && C3[i] <= C2[i]) {
      r2 -= C3[i];
    } else if (C2[i] == 0 && C3[i] <= C1[i]) {
      r1 -= C3[i];
    }
  }

  if (accumulate(C1, C1 + 26, 0) >= r1 && r1 >= 0 && accumulate(C2, C2 + 26, 0) >= r2 && r2 >= 0) {
    cout << "YES" << endl;
  } else {
    cout << "NO" << endl;
  }

  return 0;
}
