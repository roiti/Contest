#include <iostream>
using namespace std;
typedef long long ll;

const int MAX = 100005;
ll h[MAX], p[MAX];

int main(void) {
    int n, m;
    cin >> n >> m;
    for (int i = 0; i < n; i++) cin >> h[i];
    for (int i = 0; i < m; i++) cin >> p[i];

    ll l = 0, r = 1000000000000001;
    ll ans = r;
    int loop = 51;

    while (loop--) {
        ll t = (l + r) / 2;

        int j = 0;
        for (int i = 0; i < n; i++) {
            if (p[j] < h[i]) {
                ll dl = h[i] - p[j];
                if (dl > t) break;
                while (j <= m - 1) {
                    if (p[j] <= h[i]) j++;
                    else {
                        ll dr = p[j] - h[i];
                        if (p[j] <= h[i] + t - dl - min(dl, dr)) j++;
                        else break;
                    }
                }
            } else {
                while (j <= m - 1 and p[j] <= h[i] + t) j++;
            }

            if (j == m) break;
        }

        if (j == m) {
            ans = min(ans, t);
            r = t;
        } else {
            l = t;
        }
    }

    cout << ans << endl;

    return 0;
}
