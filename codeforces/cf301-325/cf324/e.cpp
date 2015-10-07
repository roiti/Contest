#include <bits/stdc++.h>
using namespace std;
typedef long long ll;

#define REP(i, a, b) for (int i = (int)(a); i < (int)(b); i++)
#define rep(i, a) REP(i, 0, a)
#define EACH(i, a) for (auto i: a)
#define ITR(x, a) for (__typeof(a.begin()) x = a.begin(); x != a.end(); x++)
#define ALL(a) (a.begin()), (a.end())


int n;
int p[2005], s[2005], pos[2005];
ll ans;
vector<pair<int, int>> swaps;

void dodo() {
  rep(i, n) REP(j, i + 1, n) {
    if ((pos[p[i]] >= j && j > i) && (pos[p[j]] <= i && i < j)) {
    swaps.push_back(make_pair(i + 1, j + 1));
    ans += j - i;
    swap(p[i], p[j]);
    }
  }
}


void rev_do() {
  for(int i = n - 1; i > -1; i--) for (int j = i - 1; j > -1; j--) {
    if ((pos[p[j]] >= i && i > j) && (pos[p[i]] <= j && j < i)) {
    swaps.push_back(make_pair(i + 1, j + 1));
    ans += i - j;
    swap(p[i], p[j]);
    }
  }
}

bool isSame(int p[], int s[]) {
    rep(i, n) if (p[i] != s[i]) return false;
    return true;
}

int main(void) {
  // breath deeply and calm down
  cin >> n;
  rep(i, n) cin >> p[i];
  rep(i, n) cin >> s[i];
  rep(i, n) pos[s[i]] = i;

  while (!isSame(p, s)) {
    dodo();
    rev_do();
  }

  cout << ans << endl;
  cout << swaps.size() << endl;
  for (auto ele: swaps) {
    cout << ele.first << " " << ele.second << endl;
  }

  return 0;
}
