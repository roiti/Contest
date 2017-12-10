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

int N;
set<int> cand;
int x[100005], y[100005];

int main(void) {
  cin.tie(0);
  ios::sync_with_stdio(false);

  cin >> N;

  int root = 0;
  int edge = 0;

  rep(i, N - 1) {
      cin >> x[i] >> y[i];
      x[i]--; y[i]--;
      if (x[i] > y[i]) swap(x[i], y[i]);
      if (x[i] == 0) {
          root += 1;
          cand.insert(y[i]);
      } 
  }

  rep(i, N) {
    if (HAS(cand, x[i])) {
        edge += 1;
        root -= 1;
        cand.erase(x[i]);
    }
    if (HAS(cand, y[i])) {
        edge += 1;
        root -= 1;
        cand.erase(y[i]);
    }
  }

  int hand = 0;
  while (true) {
    if (edge == 0) {
        root -= 1;
    }
    else {
        if (root%2 == 1) {
            edge -= 1;
        } else {
            root -= 1;
        }
    }
    if (root == 0) {
      cout << (hand == 1 ? "Bob":"Alice") << endl;
      break;
    }

    hand = (hand + 1)%2;
  }
  return 0;
}
