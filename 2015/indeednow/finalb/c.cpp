#include <iostream>
#include <string>
#define REP(i,a,b) for(int i = (a); i < (b); i++)
#define rep(i,a) REP(i,0,a)
 
using namespace std;
int N, C[5010];
long long dp[5010];
bool ispaindrome[5010][5010];
string S;
 
int main(void){
  cin >> N;
  cin >> S;
    
  rep(i,N) rep(j,N) ispaindrome[i][j] = false;
  rep(i,N) ispaindrome[i][i+1] = true;
    
  rep(i,N-1) {
    rep(j,min(N-i+1,i+1)) {
      if (S[i-j] == S[i+j]) ispaindrome[i-j][i+j+1] = true;
      else break;
    }
        
    if (S[i] != S[i+1]) continue;
    ispaindrome[i][i+2] = true;
    rep(j,min(N-i+1,i+1)) {
      if (S[i-j] == S[i+j+1]) ispaindrome[i-j][i+j+2] = true;
      else break;
    }
        
  }
 
  rep(i,N) cin >> C[i];
 
  rep(i,N+10) dp[i] = 10000000000;
  dp[0] = 0;
  REP(i,1,N+1) {
    for (int j = i-1; j > -1; j--) {
      if (ispaindrome[j][i]) {
	dp[i] = min(dp[i], dp[j]+C[i-j-1]);
      }
    }
  }
  cout << dp[N] << endl;
  return 0;
}
