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

int N;
int x[2005], y[2005];

template<typename T> T gcd(T a, T b) {
  while (b) swap(a %= b, b);
  return a;
}

ll dist2(int i, int j) {
  return (x[i] - x[j])*(x[i] - x[j]) + (y[i] - y[j])*(y[i] - y[j]);
}

int main(void) {
  cin.tie(0);
  ios::sync_with_stdio(false);
  
  cin >> N;
  if (N > 100) return 0;
  rep(i, N) cin >> x[i] >> y[i];

  ll donkaku = 0, sei = 0, eikaku = 0;
  
  vector<ll> dists;
  rep(i, N) {
    REP(j, i + 1, N) dists.push_back(i, j); 
    sort(dists.begin(), dists.end());

    
  }

 

  cout << eikaku << " " << sei << " " << donkaku << endl;

  return 0;
}
