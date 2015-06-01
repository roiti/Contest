#include <iostream>
using namespace std;
typedef long long ll;

const ll mod = 1000000007;
ll fib[100010];

int main(void) {
    fib[1] = 1;
    for (int i = 2; i < 100010; i++) {
        fib[i] = (fib[i - 1] + fib[i - 2]) % mod;
    }

    int T;
    cin >> T;
    while (T--) {
        int N;
        cin >> N;
        ll ans = 0;
        for (int i = 0; i + 2 <= N; i++) {
            ans = (ans + fib[i + 1] * fib[N - i - 1]) % mod;
        }
        cout << ans % mod << endl;
    }
    return 0;
}
