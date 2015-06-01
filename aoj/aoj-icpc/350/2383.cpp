#include <iostream>
#include <algorithm>
#define REP(i,a,b) for(int i = (a); i < (b); i++)
#define rep(i,a) REP(i,0,a)
using namespace std;

const int mod = 1000000007;
int N, T;
int D[100001];

int main(){
    cin >> N >> T;
    rep(i,N) cin >> D[i];
    sort(D, D+N);
    long long ans = 1;
    rep(i,N) ans = ans * (lower_bound(D,D+i,D[i]+1) - lower_bound(D,D+i,D[i]-T) + 1) % mod;
    cout << ans << endl;
    return 0;
}

