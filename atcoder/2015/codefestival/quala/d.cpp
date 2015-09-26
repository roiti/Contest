#include <bits/stdc++.h>
using namespace std;
typedef long long ll;

#define REP(i, a, b) for (int i = (int)(a); i < (int)(b); i++)
#define rep(i, a) REP(i, 0, a)
#define EACH(i, a) for (auto i: a)
#define ITR(x, a) for (__typeof(a.begin()) x = a.begin(); x != a.end(); x++)
#define ALL(a) (a.begin()), (a.end())

int N, M;
ll X[100005];

bool ok(ll t) {
    ll x = 0;
    rep(i, M) {
        ll d = max(0, X[i] - (x + 1));
        if (d > t) break;
        x = X[i] + max(t - 2 * d, (t - d) / 2);
        if (x >= N) return true;
    }
    return x >= N;
}

int main(void) {
    cin >> N >> M;
    rep(i, M) scanf("%d", &X[i]);

    ll l = -1, r = 1.5 * N;
    while (r - l > 1) {
        ll t = (r + l) / 2;
        if (ok(t)) r = t;
        else l = t;
    }

    cout << r << endl;

    return 0;
}
