#include <iostream>

using namespace std;
typedef long long ll;
const ll INF = (1LL << 58);
ll G[101][101];

int main(void) {
    int V, E;
    cin >> V >> E;
    for (int i = 0; i < V; i++) {
        for (int j = 0; j < V; j++) {
            if (i == j) continue;
            G[i][j] = INF;
        }
    }

    for (int i = 0; i < E; i++) {
        int s, t, d;
        cin >> s >> t >> d;
        G[s][t] = d;
    }

    for (int k = 0; k < V; k++)
        for (int i = 0; i < V; i++)
            for (int j = 0; j < V; j++)
                G[i][j] = min(G[i][j], G[i][k] + G[k][j]);

    for (int i = 0; i < V; i++) {
        if (G[i][i] < 0) {
            cout << "NEGATIVE CYCLE" << endl;
            return 0;
        }
    }

    for (int i = 0; i < V; i++) {
        for (int j = 0; j < V; j++) {
            if (G[i][j] < (1LL << 40)) cout << G[i][j];
            else cout << "INF";
            if (j < V - 1) cout << " ";
            else cout << endl;
        }
    }

    return 0;
}
