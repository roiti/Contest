#include <iostream>
using namespace std;

int dp[1 << 16];

int main(void){
    int N, a;
    cin >> N;
    dp[0] = 1;
    for (int i = 0; i < N; i++) {
        cin >> a;
        for (int j = 0; j < (1 << 16); j++) {
            if (dp[j]) dp[j ^ a] = 1;
        }
    }

    int ans = 0;
    for (int i = 0; i < (1 << 16); i++) ans += dp[i];
    cout << ans << endl;
    
    return 0;
}
