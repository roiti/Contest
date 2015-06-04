#include <iostream>
#include <cstdio>
using namespace std;

const int INF = 100000000;
int n, G[101][101];

int main(void) {
    int u, k, v;
    cin >> n;
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            G[i][j] = INF;
        }
        G[i][i] = 0;
    }

    for (int i = 0; i < n; i++) {
        cin >> u >> k;
        for (int j = 0; j < k; j++) {
            cin >> v;
            G[u - 1][v - 1] = 1;
        }
    }

    for (int k = 0; k < n; k++)
        for (int i = 0; i < n; i++)
            for (int j = 0; j < n; j++)
                G[i][j] = min(G[i][j], G[i][k] + G[k][j]);

    for (int i = 0; i < n; i++)
        printf("%d %d\n", i + 1, (G[0][i] < INF ? G[0][i] : -1));

    return 0;
}
