#include <iostream>
#include <string>
#include <vector>
#include <cstdio>
#include <random>
#define REP(i,a,b) for(int i = (int)(a); i < (int)(b); i++)
#define rep(i,a) REP(i,0,a)
using namespace std;

int T, K, L, S;
string a, b;

int main(void) {
  cin >> T;
  mt19937 mt;
  random_device rnd;
  mt.seed(rnd());
  
  REP(loop, 1, T + 1) {
    double ans = 0.0;
    cin >> K >> L >> S;
    cin >> a;
    cin >> b;
    rep(rondom, 100000) {
      string tmp = "";
      rep(i, S) {
	tmp += a[mt() % K];
      }
      rep(i, S - L) {
	REP(j, i, S) {
	  if (tmp[j] != b[j - i]) {
	    flag = false;
	    break;
	  }
	}
	if (flag) ans += 1;
      }
    }
    
    printf("Case #%d: %.7f", loop, ans);
  }
  return 0;
}
