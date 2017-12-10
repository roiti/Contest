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
int A[40005], B[40005], C[40005];

pair<long double, long double> intersect(int a1, int b1, int c1, int a2, int b2, int c2) {
  long double x = ((long double)b1*c2 - b2*c1)/(a1*b2 - a2*b1);
  long double y = ((long double)a2*c1 - a1*c2)/(a1*b2 - a2*b1);
  return {x, y};
}

int main(void) {
  cin.tie(0);
  ios::sync_with_stdio(false);

  cin >> N;
  rep(i, N) cin >> A[i] >> B[i] >> C[i];

  int NN = N*(N - 1)/2;
  long double x = 0, y = 0;
  rep(i, N) REP(j, i + 1, N) {
    auto p = intersect(A[i], B[i], -C[i], A[j], B[j], -C[j]);  
    cout << p.first << "," << p.second << endl;
    x += p.first/NN;
    y += p.second/NN;
  }

  printf("%.18Lf %.18Lf\n", x, y);

  return 0;
}
