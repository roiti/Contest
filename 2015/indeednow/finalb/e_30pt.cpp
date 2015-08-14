#include <iostream>
#include <string>
#define REP(i,a,b) for(int i = (a); i < (b); i++)
#define rep(i,a) REP(i,0,a)
using namespace std;
 
int N;
int H[100010];
 
int main(void) {
  cin >> N;
  rep(i,N) cin >> H[i];
    
  long long ans = 0;
  rep(i,N) {
    REP(j,i+1,N) {
      if (H[i] == H[j]) {
	cout << -1 << endl;
	return 0;
      }
      if (H[i] > H[j]) {
	ans += H[j];
      }
    }
  }
  cout << ans << endl;
  return 0;
}
