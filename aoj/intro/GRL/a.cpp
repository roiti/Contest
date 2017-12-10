#include <bits/stdc++.h>
using namespace std;
 
const int MAXN = 100005;
 
int N, Q;
int T[MAXN], L[MAXN], P[MAXN][20];  // direct parent, depth, ancestor
vector<int> adjList[MAXN];
 
void dfs(int node = 0, int depth = 0) {
    L[node] = depth;
    for (int i = 0; i < adjList[node].size(); i++) {
        int child = adjList[node][i];
        dfs(child,depth+1);
    }
}
 
int query(int u, int v) {
    if (L[u] < L[v])
        swap(u,v);
 
    int LOG2;
    for (LOG2 = 1; 1 << LOG2 <= L[u]; LOG2++); LOG2--;
 
    for (int i = LOG2; i >= 0; i--)
        if (L[u] - (1 << i) >= L[v])
            u = P[u][i];
 
    if (u == v)
        return u;
 
    for (int i = LOG2; i >= 0; i--)
        if (P[u][i] != -1 && P[u][i] != P[v][i])
            u = P[u][i], v = P[v][i];
 
    return T[u];
}
 
int main() {
 
    scanf("%d",&N);
    for (int u = 0, M; u < N; u++) {
        scanf("%d",&M);
        for (int i = 0, v; i < M; i++) {
            scanf("%d",&v);
 
            T[v] = u;
            adjList[u].push_back(v);
        }
    }
 
    // rooted at 0
    dfs();
 
    for (int i = 1; i <= N; i++)
        P[i][0] = T[i];
    for (int j = 1; 1 << j < N; j++)
        for (int i = 1; i <= N; i++)
            P[i][j] = P[P[i][j-1]][j-1];
 
    scanf("%d",&Q);
    for (int i = 0, u, v; i < Q; i++) {
        scanf("%d%d",&u,&v);
        printf("%d\n", query(u,v));
    }
 
    return 0;
}
