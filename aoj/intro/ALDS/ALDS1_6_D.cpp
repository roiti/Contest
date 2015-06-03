#include <iostream>
#include <algorithm>
using namespace std;

const int MAX = 1000, VMAX = 100001;
int n, mn, A[MAX], B[MAX], T[VMAX];
bool V[MAX];

int solve() {
    int res = 0;

    for (int i = 0; i < n; i++) {
        B[i] = A[i];
        V[i] = false;
    }

    sort(B, B + n);

    for (int i = 0; i < n; i++) T[B[i]] = i;
    for (int i = 0; i < n; i++) {
        if (V[i]) continue;
        int cur = i;
        int S = 0;
        int m = VMAX;
        int an = 0;
        while (1) {
            V[cur] = true;
            an++;
            int v = A[cur];
            m = min(m, v);
            S += v;
            cur = T[v];
            if (V[cur]) break;
        }
        res += min(S + (an - 2) * m, m + S + (an + 1) * mn);
    }
    return res;
}

int main(void) {
    mn = VMAX;
    cin >> n;
    for (int i = 0; i < n; i++) {
        cin >> A[i];
        mn = min(mn, A[i]);
    }

    cout << solve() << endl;

    return 0;
}
