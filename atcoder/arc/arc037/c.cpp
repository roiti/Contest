#include <iostream>
#include <algorithm>
#define REP(i,a,b) for (int i = (a); i < (int)(b); i++)
#define rep(i,a) REP(i,0,a)
using namespace std;
 
int N, K;
long long a[30010], b[30010];
 
int main(void){
  cin >> N >> K;
  rep(i, N) cin >> a[i];
  rep(i, N) cin >> b[i];
 
  sort(a, a + N);
  sort(b, b + N);
    
  long long low = 0, high = (1LL << 61);
  long long mid = (low + high) / 2;
  long long ans = (1LL << 61);
  while (low <= high) {
    int k = 0;
    long long tmp = 0;
    rep(i, N) {
      int pos = upper_bound(a, a + N, mid / b[i]) - a;
      k += pos;
      if (pos > 0) tmp = max(tmp, a[pos - 1] * b[i]);
    }
        
    if (k >= K) ans  = min(ans, tmp);
    if (k >= K) high = mid - 1;
    if (k <  K) low  = mid + 1;
 
    mid = (low + high) / 2;
  }
    
  cout << ans << endl;
  return 0;
}
