#include <iostream>
#include <cstdio>
#define REP(i,a,b) for(int i = (a); i < (b); i++)
using namespace std;

double dp[2001][2001];

int main(void){
    int n,t;
    double p;
    cin >> n >> p >> t;
    REP(i,1,t+1) {
        REP(j,1,n+1) {
            dp[i][j] = p * (dp[i-1][j-1]+1) + (1-p) * dp[i-1][j];
        }
    }
    printf("%.7f",dp[t][n]);
    return 0;
}
