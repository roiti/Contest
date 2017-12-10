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
string s;
vector<string> t;

int main(void) {
  cin.tie(0);
  ios::sync_with_stdio(false);

  cin >> N;
  cin >> s;
  
  string x;
  rep(i, N - 1) {
    if (s[i] == '0' && s[i + 1] == '0' && x.size() >= 3) {
      t.push_back(x); 
      x = "";
    }
    x += s[i];
  }
  if (x.size() >= 2) t.push_back(x + s[N - 1]);

  int ans = 0;
  for (auto u: t) {
    string a = u;
    // left first
    int tmp1 = 0;
    rep(i, a.size() - 3) {
      if (a[i] == '1' && a[i + 1] == '0' && a[i + 2] == '1' && a[i + 3] == '1') {
        a[i] = '0'; a[i + 1] = '1'; a[i + 2] = '0';
        tmp1++;
      }
    }

    for (int i = a.size() - 4; i >= 0; i--) {
      if (a[i] == '1' && a[i + 1] == '1' && a[i + 2] == '0' && a[i + 3] == '1') {
        a[i + 1] = '0'; a[i + 2] = '1'; a[i + 3] = '0';
        tmp1++;
      }
    }

    rep(i, a.size() - 2) {
      if (a[i] == '1' && a[i + 1] == '0' && a[i + 2] == '1') {
        a[i] = '0'; a[i + 1] = '1'; a[i + 2] = '0';
        tmp1++;
      }
    }
    
    a = u;
    // right first
    int tmp2 = 0;
    for (int i = a.size() - 4; i >= 0; i--) {
      if (a[i] == '1' && a[i + 1] == '1' && a[i + 2] == '0' && a[i + 3] == '1') {
        a[i + 1] = '0'; a[i + 2] = '1'; a[i + 3] = '0';
        tmp2++;
      }
    }

    rep(i, a.size() - 3) {
      if (a[i] == '1' && a[i + 1] == '0' && a[i + 2] == '1' && a[i + 3] == '1') {
        a[i] = '0'; a[i + 1] = '1'; a[i + 2] = '0';
        tmp2++;
      }
    }

    rep(i, a.size() - 2) {
      if (a[i] == '1' && a[i + 1] == '0' && a[i + 2] == '1') {
        a[i] = '0'; a[i + 1] = '1'; a[i + 2] = '0';
        tmp2++;
      }
    }  

    ans += max(tmp1, tmp2);
  }

  cout << ans << endl;

  return 0;
}
