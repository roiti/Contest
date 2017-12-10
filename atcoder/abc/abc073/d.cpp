#include <iostream>
#include <algorithm>
#define rep(i, x) for(int i = 0; i < (x); i++)
typedef long long ll;
using namespace std;

const int inf = (int)1e8;

int N, M, R;
int r[10];
ll G[205][205];

int main(void) {
    cin >> N >> M >> R;
    rep(i, R) cin >> r[i], r[i]--;
    sort(r, r + R);

    rep(i, N) rep(j, N) G[i][j] = inf;
    rep(i, M) {
        int A, B, C;
        cin >> A >> B >> C;
        A -= 1; B -= 1;
        G[A][B] = C;
        G[B][A] = C;
    }

    rep(k, N) rep(i, N) rep(j, N) 
        G[i][j] = min(G[i][j], G[i][k] + G[k][j]);

    int ans = inf;
    do {
        int tmp = 0;
        rep(i, R - 1) tmp += G[r[i]][r[i + 1]]; 
        ans = min(ans, tmp);
    } while (next_permutation(r, r + R));

    cout << ans << endl;
}
