#include <bits/stdc++.h>
 
#define REP(i,a,b) for(int i = (a); i < (b); i++)
#define rep(i,a) REP(i,0,a)
using namespace std;
 
int main(void){
  double comb[101][101];
  rep(i, 101) {
    comb[i][0] = 1;
    REP(j, 1, i + 1) {
      comb[i][j] = comb[i - 1][j - 1] + comb[i - 1][j];
    }
  }
    
  int N;
  cin >> N;
    
  double P[N + 1];
  rep(i,N+1) P[i] = 0.0;
  REP(n, 2, N + 1) {
    double p_d = 0.0, sum = 0.0;
    rep(a, n + 1) rep(b, n + 1) {
      int c = n - a - b;
      if (c < 0) continue;
            
      double p = comb[n][a] * comb[n-a][b] / pow(3.0, n);
      int cnt[] = {a, b, c};
      sort(cnt, cnt + 3);
      if (cnt[0] == cnt[2] || cnt[1] == 0) {
	p_d += p;
      } else {
	sum += p * (1.0 + P[cnt[cnt[0] == 0]]);
      }
    }
    P[n] = (p_d + sum) / (1.0 - p_d);
  }
  printf("%.10f\n", P[N]);
  return 0;
}
