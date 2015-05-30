#include <iostream>
#include <vector>
#include <queue>

using namespace std;

int V, E;
vector<int> G[10010];
vector<int> ans;
int indeg[10010];
bool used[10010];

void bfs(int s) {
    queue<int> que;
    que.push(s);
    used[s] = true;
    while (!que.empty()) {
        int u = que.front(); que.pop();
        ans.push_back(u);
        for (auto v: G[u]) {
            indeg[v]--;
            if (indeg[v] == 0 && !used[v]) {
                used[v] = true;
                que.push(v);
            }
        }
    }
}

void tsort() {
    for (int u = 0; u < V; u++) {
        used[u] = false;
        indeg[u] = 0;
    }

    for (int u = 0; u < V; u++)
        for (auto v: G[u]) indeg[v]++;

    for (int u = 0; u < V; u++)
        if (indeg[u] == 0 && !used[u]) bfs(u);
}


int main(void) {
    cin >> V >> E;
    for (int i = 0; i < E; i++) {
        int s, t;
        cin >> s >> t;
        G[s].push_back(t);
    }

    tsort();
    for (auto i: ans) cout << i << endl;

    return 0;
}
