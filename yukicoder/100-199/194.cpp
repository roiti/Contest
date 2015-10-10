#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
typedef vector<ll> vec;
typedef vector<vec> mat;

#define REP(i, a, b) for (int i = (int)(a); i < (int)(b); i++)
#define rep(i, a) REP(i, 0, a)
#define EACH(i, a) for (auto i: a)
#define ITR(x, a) for (__typeof(a.begin()) x = a.begin(); x != a.end(); x++)
#define ALL(a) (a.begin()), (a.end())
#define HAS(a, x) (a.find(x) != a.end())

ll N, K;
const ll mod = 1000000007;
ll F[1000005];

mat mat_mul(mat &A, mat &B) {
  mat C(A.size(), vec(B[0].size()));
  for (int i = 0; i < A.size(); i++)
    for (int k = 0; k < B.size(); k++)
      for (int j = 0; j < B[0].size(); j++)
        C[i][j] = (C[i][j] + A[i][k] * B[k][j]) % mod;
  return C;
}

mat mat_pow(mat A, ll n) {
  mat B(A.size(), vec(A.size()));
  for (int i = 0; i < A.size(); i++) B[i][i] = 1;
  while (n) {
    if (n & 1) B = mat_mul(B, A);
    A = mat_mul(A, A);
    n >>= 1;
  }
  return B;
}

void solve1() {
  rep(i, N) F[N] = (F[N] + F[i]) % mod;
  REP(i, N + 1, K)
    F[i] = (F[i - 1] + F[i - 1] - F[i - N - 1] + mod) % mod;
  ll S = 0;
  rep(i, K) S = (S + F[i]) % mod;
  cout << F[K - 1] << " " << S << endl;
}


void solve2() {
  mat B(N + 1, vec(1));
  rep(i, N) B[N - i][0] = F[i];
  rep(i, N) B[0][0] += F[i];
  mat A(N + 1, vec(N + 1));
  rep(i, N + 1) A[0][i] = 1;
  rep(i, N) A[1][i + 1] = 1;
  rep(i, N - 1) A[i + 2][i + 1] = 1;
  A = mat_pow(A, K - N);
  B = mat_mul(A, B);
  cout << B[1][0] << " " << B[0][0] << endl;
}

int main(void) {
  cin >> N >> K;
  rep(i, N) cin >> F[i];

  if (N > 30)
    solve1();
  else
    solve2();

  return 0;
}
