include <iostream>
#include <set>
#define int long long
using namespace std;
 
const int MOD = 1000000007;
int N,M;
int f[100010], sum[100010], dp[100010];
 
signed main(void){
  cin >> N >> M;
  for (int i=0; i < N; i++) cin >> f[i];
 
  int l = 0;
  int cur = 0;
  dp[0] = 1;
  set<int> used;
  for (int i=0; i <= N; i++){
    cur += sum[i];
    dp[i] += cur;
    dp[i] %= MOD;
    while (l < N && used.count(f[l]) == false) used.insert(f[l]), l++;
 
    sum[i+1] += dp[i];
    sum[l+1] -= dp[i];
    used.erase(f[i]);
  }
 
  cout << (dp[N]%MOD+MOD)%MOD << endl;
  return 0;
}
