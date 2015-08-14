#include <iostream>
using namespace std;
int main(void){
  // Here your code !
  int W,N,K;
  cin >> W;
  cin >> N >> K;
  int A[N];
  int B[N];
  for (int n = 0; n < N; n++){
    cin >> A[n];
    cin >> B[n];
  }
  int dp[K+1][10101];
  for (int k = 0; k < K+1; k++)
    for (int w = 0; w < 10101; w++)
      dp[k][w] = 0;
  for (int n = 0; n < N; n++){
    int a = A[n];
    int b = B[n];
    for (int k = K-1; k > 0; k--){
      for (int w = W-a; w > -1; w--){
	dp[k+1][w+a] = max(dp[k+1][w+a], dp[k][w]+b);
      }
    }
    dp[1][a] = b;
  }
  int ans = 0;
  for (int k = 0; k < K+1; k++)
    for (int w = 0; w < W+1; w++)
      ans = max(ans, dp[k][w]);
  cout << ans << endl;
  return 0;
}
