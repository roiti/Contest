#include <iostream>
using namespace std;
typedef long long ll;

const ll mod = (ll)1e9 + 7;
int N;
ll dp[1000005][3];

int main() {
  cin >> N;
  dp[0][1] = 1;
  for (int i = 1; i < N; i++) {
    dp[i][0] = (dp[i - 1][1] + dp[i - 2][1]) % mod;
    dp[i][1] = dp[i - 1][0];
    dp[i][2] = dp[i - 1][1];
  }

  ll ans = (dp[N - 1][0] + dp[N - 1][1] + dp[N - 1][2]) % mod;
  cout << ans << endl;

  return 0;
}
