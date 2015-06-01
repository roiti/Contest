#include <iostream>
#include <algorithm>
using namespace std;
typedef long long ll;

ll gcd(ll a, ll b) {
    while (b) swap(a %= b, b);
    return a;
}

ll extgcd(ll a, ll b, ll& x, ll& y) {
    if (b == 0) {
        x = (a >= 0) ? 1 : -1;
        y = 0;
        return abs(a);
    } else {
        ll res = extgcd(b, a % b, y, x);
        y -= (a / b) * x;
        return res;
    }
}

ll mod_inverse(ll a, ll p) {
    ll x, y;
    extgcd(a, p, x, y);
    return (p + x % p) % p;
}

int main(void) {
    int T;
    cin >> T;
    while (T--) {
        ll a, p, n;
        cin >> a >> p >> n;
        if (gcd(a, p) != 1) {
            cout << -1 << endl;
            continue;
        }
        ll b = mod_inverse(a, p);
        ll ans = (a + b) * (n / 2) + a * (n % 2);
        cout << ans << endl;
    }
    return 0;
}
