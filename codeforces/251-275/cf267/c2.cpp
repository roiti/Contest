#define FOR(i,a) for(int i=0;i<(a);i++)
#include <sstream>
#include <iostream>
#include <string>
using namespace std;

int N,M,K;
long long P[5001],S[5005];
long long dp[5005][5005];

void solve() {
    int i,j,k,l,r,x,y;
    string s;
    
    cin>>N>>M>>K;
    FOR(i,N) cin>>P[i];
    FOR(i,N) S[i+1]=S[i]+P[i];
    
    FOR(x,5005) FOR(y,5005) dp[x][y]=-1LL<<50;
    dp[0][K]=0;
    FOR(i,N) FOR(j,K+1) {
        dp[i+1][j]=dp[i][j];
        if(i+1>=M) dp[i+1][j]=max(dp[i+1][j],dp[i+1-M][j+1]+S[i+1]-S[i+1-M]);
    }
    cout <<dp[N][0]<<endl;
}

int main(){
    solve();
    return 0;
}
