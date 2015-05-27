#include <iostream>
#define REP(i,a,b) for(int i = (a); i < (b); i++)
#define rep(i,a) REP(i,0,a)
using namespace std;

int A1, A2, A3, B1, B2, B3, C1, C2, C3;
int x1, x2, x3, db, dc, Db, Dc;
int memo[11][101][10001];

int solve(int a1, int a2, int a3) {
    if (memo[a1][a2][a3] >= 0) return memo[a1][a2][a3];
    int res = 0;
    if (1000*a1+100*a2+a3 >= Db) {
        x1 = a1, x2 = a2, x3 = a3, db = Db;
        while (x1 && db >= 1000) db -= 1000, x1 -= 1;
        while (x2 && db >=  100) db -=  100, x2 -= 1;
        while (x3 && db >=    1) db -=    1, x3 -= 1;
        if (db == 0) res = max(res, solve(x1+B1, x2+B2, x3+B3)+1);
    }

    if (1000*a1+100*a2+a3 >= Dc) {
        x1 = a1, x2 = a2, x3 = a3, dc = Dc;
        while (x1 && dc >= 1000) dc -= 1000, x1 -= 1;
        while (x2 && dc >=  100) dc -=  100, x2 -= 1;
        while (x3 && dc >=    1) dc -=    1, x3 -= 1;
        if (dc == 0) res = max(res, solve(x1+C1, x2+C2, x3+C3)+1);
    }
    return memo[a1][a2][a3] = res;
}

int main(void){
    cin >> A1 >> A2 >> A3;
    cin >> Db;
    cin >> B1 >> B2 >> B3;
    cin >> Dc;
    cin >> C1 >> C2 >> C3;
    
    rep(i, 11) rep(j, 101) rep(k, 10001) memo[i][j][k] = -1;
    cout << solve(A1, A2, A3) << endl;
    return 0;
}
