#include <iostream>
#include <stdio.h>
#define FOR(i,a,b) for(int i=(a); i<(b); i++)
#define RFOR(i,a,b) for(int i=(a); i>(b); i--)
#define REP(i,a) FOR(i,0,a)
using namespace std;
 
int main(void){
  double dp[201][201] = {};
  dp[0][0] = 1.0;
  int N,K;
  cin >> N >> K;
    
  double p;
  REP(i,N){
    cin >> p;
    p *= 0.01;
    RFOR(i,K,-1){
      REP(j,i+1){
	double c = dp[j][i];
	if (i < K){
	  dp[j + 2 - (i == j)][i+1] += c*p;
	  dp[j][i] -= c*p;
	}
	if (i == 0 || 2*i-j+1 < K){
	  dp[j + (i == 0)][i+1] += c*(1.0-p);
	  dp[j][i] -= c*(1.0-p);
	}
      }
    }
  }
  double r = 0.0;
  REP(i,K+1) REP(j,K+1) r += dp[i][j]*(K-j);
  printf("%.8f",r);
  return 0;
}
