#include <iostream>
#define FOR(i,a,b) for(int i=(a); i<b; i++)
#define REP(i,a) FOR(i,0,a)
using namespace std;
 
int R,C,M,N;
int A[50][50]={0} ; // 0,1,2,3 : S,W,N,E
 
int main(void){
  cin >> R >> C >> M >> N;
  int ra[N],rb[N],ca[N],cb[N];
  REP(i,N)
    cin >> ra[i] >> rb[i] >> ca[i] >> cb[i];
  REP(i,N) {
    FOR(y,ra[i]-1,rb[i]) {
      FOR(x,ca[i]-1,cb[i]) {
	A[y][x] = (A[y][x]+1)%4;
      }
    }
  }
  int south = 0;
  REP(y,R) REP(x,C) south += (A[y][x] == 0 ? 1:0);
  REP(i,N){
    int tmp = south;
    FOR(y,ra[i]-1,rb[i]){
      FOR(x,ca[i]-1,cb[i]){
	if (A[y][x] == 0) tmp -= 1;
	if (A[y][x] == 1) tmp += 1;
      }
    }
    if (tmp == M) cout << i+1 << endl;
  }
  return 0;
}
