#include <iostream>
#include <algorithm>
#define FOR(i,a,b) for(int i=(a); i<(b); i++)
#define REP(i,a) FOR(i,0,a)
using namespace std;
 
int main(void){
  int N,M,D;
  cin >> N >> M >> D;
  int A[M],S[N],L[N];
  REP(i,M) cin >> A[i];
    
  REP(i,N) S[i] = i, L[i] = i;
 
  int tmp = 0;
  for (int i=M-1; i > -1; i--){
    tmp = S[A[i]]; S[A[i]] = S[A[i]-1]; S[A[i]-1] = tmp;
  }
 
  int t = 0;
  while (D > (1<<t)) t += 1;
 
  int JUMP[t+1][N];
  REP(i,N) JUMP[0][i] = S[i];
  FOR(j,1,t+1){
    REP(i,N)
      JUMP[j][i] = JUMP[j-1][JUMP[j-1][i]];
  }
    
  int j = 0;
  while (D > 0){
    if (D&1)
      REP(i,N) L[i] = JUMP[j][L[i]];
    D >>= 1;
    j += 1;
  }
  REP(i,N) cout << L[i]+1 << endl;
    
  return 0;
}
