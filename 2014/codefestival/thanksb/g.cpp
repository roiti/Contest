#include <iostream>
#define FOR(i,a,b) for(int i=(a); i<(b); i++)
#define REP(i,a) FOR(i,0,a)
using namespace std;
 
const int MAX = 505;
int dp[MAX][MAX];
 
int solve(int n, int p)
{
  if (dp[n][p] != -1) return dp[n][p];
  dp[n][p] = 0;
  FOR(i,1,p+1){
    if (i > n) break;
    if (!solve(n-i,i+1)){
      dp[n][p] = 1;
      break;
    }
  }
  return dp[n][p];
}
 
int main(void)
{
  int N,P;
  cin >> N >> P;
  REP(i,MAX) REP(j,MAX) dp[i][j] = -1;
 
  cout << (solve(N,P) ? "first":"second") << endl;
 
  return 0;
}
