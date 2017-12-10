#include <bits/stdc++.h>
using namespace std;
typedef long long ll;

#define REP(i, a, b) for (int i = (int)(a); i < (int)(b); i++)
#define rep(i, a) REP(i, 0, a)
#define EACH(i, a) for (auto i: a)
#define ITR(x, a) for (__typeof(a.begin()) x = a.begin(); x != a.end(); x++)
#define ALL(a) (a.begin()), (a.end())

const int MX = 3005;
bool p[MX];
vector<int> prime;

bool judge(int N) {
  EACH(i, prime) {
    if (i * i > N) return (N > 1 && N % 4 == 1);
    if (N % i == 0 && i % 4 == 1) return true;
    while (N % i == 0) N /= i;
  }
}

int main(void) {
  rep(i, MX) p[i] = true;
  p[0] = p[1] = false;
  for (int i = 2; i * i < MX; i++) {
    if (p[i])
      for (int j = 2 * i; j < MX; j += i) p[j] = false;
  }

  rep(i, MX)
    if (p[i]) prime.push_back(i);

  int T;
  cin >> T;
  while (T--) {
    ll N;
    scanf("%lld", &N);
    printf("%s\n", (judge(N) ? "YES":"NO"));
  }
  return 0;
}
