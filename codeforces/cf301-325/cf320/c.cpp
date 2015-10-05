#include <iostream>
#include <cstdio>
#include <vector>
#define rep(i, a) for (int i = 0; i < (int)(a); i++)
using namespace std;
typedef long long ll;

int n;
ll a[200005], mx[200005], mn[200005];

int main(void) {
    cin >> n;
    rep(i, n) cin >> a[i];

    rep(i, n) {
        mn[i] = 1L << 60;
        mx[i] = -(1L << 60);
    }

    int i = 0;
    while (i < n) {
        bool cont = false;
        ll tmp = a[i];
        mx[1] = max(mx[1], tmp);
        mn[1] = min(mn[1], tmp);
        rep(j, n) {
            if ((tmp >= 0 && tmp + a[j] < 0) || (tmp <= 0 && tmp + a[j] > 0)) {
                i = j;
                cont = true;
                break;
            }
            tmp += a[j];
            mn[j - i + 1] = min(mn[j - i + 1], tmp);
            mx[j - i + 1] = max(mx[j - i + 1], tmp);
        }
        if (cont) continue;
        break;
    }

    double ans = 1e8
    double l = -10000, r = 10000, x = 0;
    rep(loop, 100) {
        tmp = 1e8
        x = (l + r) / 2.0;
        rep(i, n) {
            tmp = min(tmp, mx[i] + )
        }
    }
}
