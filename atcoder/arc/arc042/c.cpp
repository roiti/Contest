#include <iostream>
#include <algorithm>
#include <vector>
#include <utility>
using namespace std;
#define mp(a, b) make_pair(a, b)
 
vector<pair<int, int>> ab;
 
int main(void){
  int N, P;
  cin >> N >> P;
  for (int i = 0; i < N; i++) {
    int a, b;
    cin >> a >> b;
    ab.push_back(mp(a, b));
 
  }
  sort(ab.begin(), ab.end());
 
  pair<int, int> dp[P + 101];
  for (int i = 0; i <= P + 100; i++) dp[i] = mp(999, 0);
 
  for (int i = N - 1; i >= 0; i--) {
    int a = ab[i].first, b = ab[i].second;
    for (int j = P + 100; j >= 0; j--) {
      int m = min(dp[j].first, a);
      if (j + m <= P + 100 && j - m <= P && dp[j + m].second < dp[j].second + b)
	dp[j + m] = mp(m, dp[j].second + b);
    }
    if (b > dp[a].second) dp[a] = mp(a, b);
  }
 
  int ans = 0;
  for (int i = 0; i <= P + 100; i++) {
    if (i - dp[i].first <= P)
      ans = max(ans, dp[i].second);
  }
  cout << ans << endl;
 
  return 0;
 
}
