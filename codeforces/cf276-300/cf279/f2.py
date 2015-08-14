#include <iostream>
#include <algorithm>
#include <cstring>
#define FOR(i,a,b) for(int i=(a);i<(b);i++)
#define REP(i,a) FOR(i,0,a)
using namespace std;

int n;  //max 6000
int pop[6000];
int fst[6000];
int nxt[12000];
int fm[12000];
int to[12000];
int dp[12000];

int go(int at, int prev, int last){
    int res = pop[at] > last? 1:0;
    for (int x=fst[at]; x!=-1; x=nxt[x]){
        if (to[x]==prev) continue;
        {
            int cur = go(to[x],at,last);
            res = max(res,cur);
        }
        if (pop[at] > last){
            if(dp[x] == -1) dp[x] = 1+go(to[x],at,pop[at]);
            res = max(res,dp[x]);
        }
    }
    return res;
}

void solve(){
    memset(fst,-1,sizeof(fst));
    cin >> n;
    REP(i,n) cin >> pop[i];
    REP(i,n-1){
        int a,b;
        cin >> a >> b; a--, b--;
        nxt[2*i+0]=fst[a]; fst[a]=2*i+0; fm[2*i+0]=a; to[2*i+0]=b;
        nxt[2*i+1]=fst[b]; fst[b]=2*i+1; fm[2*i+1]=b; to[2*i+1]=a;
    }
    
    memset(dp,-1,sizeof(dp));
    int ans = 0;
    REP(i,2*(n-1)){
        if (dp[i] == -1) dp[i] = 1+go(to[i],fm[i],pop[fm[i]]);
        ans = max(ans,dp[i]);
    }
    cout << ans << endl;
}

int main(void){
    solve();
    return 0;
}
