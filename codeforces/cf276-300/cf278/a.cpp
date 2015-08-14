#include <iostream>
#include <algorithm>
#define FOR(i,a,b) for(int i=(a); i < (b); i++)
#define REP(i,a) FOR(i,0,a)
using namespace std;

int H1,A1,D1,H2,D2,A2,h,a,d;

bool judge(int h1, int a1, int d1){
    if (a1-D2 < 1) return false;
    if (a1-D2 > 0 && A2-d1 < 1) return true;
    int t1 = h1/(A2-d1)+(h1%(A2-d1)==0 ? 0:1);
    int t2 = H2/(a1-D2)+(H2%(a1-D2)==0 ? 0:1);
    return t1>t2 ? true:false;
}

int main(void){
    cin >> H1 >> A1 >> D1;
    cin >> H2 >> A2 >> D2;
    cin >> h >> a >> d;
    int ans = (1<<15);
    REP(hi,1000){
        FOR(ai,max(0,D2+1-A1),101-(A1-D2)){
            REP(di,max(0,A2-D1)+1){
                if (judge(H1+hi,A1+ai,D1+di))
                    ans = min(ans,h*hi+a*ai+d*di);
            }
        }
    }
    cout << ans << endl;
    return 0;
}
