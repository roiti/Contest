#include <iostream>
#include <algorithm>
#define FOR(i,a,b) for(int i=(a); i<(b); i++)
#define REP(i,a) FOR(i,0,a)

using namespace std;
int main(void){
    int n,m;
    cin >> n >> m;
    int score[n][n];
    REP(i,n) REP(j,n) score[i][j] = 0;
    int a,b,c;
    REP(i,m){
        cin >> a >> b >> c;
        score[a][b] = c;
    }
    int item[n];
    REP(i,n) item[i] = i;
    int ans = 0;
    do{
        int tmp = 0;
        REP(i,n-1){
            FOR(j,i+1,n){
                tmp += score[item[i]][item[j]];
            }
        }
        ans = max(ans,tmp);
    }while(next_permutation(item,item+n));
    cout << ans << endl;
}