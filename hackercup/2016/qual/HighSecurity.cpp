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

int T, N;
string S[2];

bool needGurad(int row, int col) {
  if (S[row][col] != '.') return false;
  if (S[1 - row][col] == 'G') return false;

  bool res = true;
  int x = col;
  while (x++ < N && S[row][x] != 'X')  if (S[row][x] == 'G') {
    res = false;
    break;
  }

  x = col;
  while (x-- > 0 && S[row][x] != 'X') if (S[row][x] == 'G') {
    res = false;
    break;
  }

  return res;
}

int main(void) {
  cin >> T;
  int ncase = 0;
  while (T--) {
    ncase++;
    cin >> N;
    cin >> S[0];
    cin >> S[1];
    N += 2;
    S[0] = 'X' + S[0] + 'X';
    S[1] = 'X' + S[1] + 'X';

    int ans = 0;
    REP(i, 1, N - 1) {
      if (S[0][i - 1] == 'X' && S[0][i] == '.' &&  S[0][i + 1] == 'X' && S[1][i] == 'X') ans++, S[0][i] = 'G';
      if (S[1][i - 1] == 'X' && S[1][i] == '.' &&  S[1][i + 1] == 'X' && S[0][i] == 'X') ans++, S[1][i] = 'G';
    }

    REP(i, 1, N - 1) {
      if (S[0][i - 1] == 'X' && S[0][i] == '.' &&  S[0][i + 1] == 'X' && S[1][i] == '.') ans++, S[1][i] = 'G';
      if (S[1][i - 1] == 'X' && S[1][i] == '.' &&  S[1][i + 1] == 'X' && S[0][i] == '.') ans++, S[0][i] = 'G';
    }

    REP(i, 1, N - 1) {
      if (needGurad(0, i)) ans++, S[0][i] = 'G';
      if (needGurad(1, i)) ans++, S[1][i] = 'G';
    }

    printf("Case #%d: %d\n", ncase, ans);
    //cout << S[0] << endl;
    //cout << S[1] << endl;
    //cout << endl;
  }
  return 0;
}
