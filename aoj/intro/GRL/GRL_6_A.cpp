#include <iostream>
#include <vector>
#include <numeric>
#include <queue>
using namespace std;

template <class T>
class MaxFlowDinic {
 public:
    // you may need to change INF
    static const T INF = 2147483647; //INT_MAX
    int V;
    struct edge {
        int to, rev;
        T cap;
    };
    vector<vector<edge>> G;
    vector<int> level;
    vector<int> iter;

    MaxFlowDinic() {};
    MaxFlowDinic(int v) {
        V = v;
        G.resize(V); level.resize(V); iter.resize(V);
        for (int i = 0; i < V; i++) G[i].clear();
    }

    void add(int from, int to, T cap) {
        G[from].push_back(edge{to, (int)G[to].size(), cap});
        G[to].push_back(edge{from, (int)G[from].size() - 1, 0});
    }

    void add_dual(int from, int to, T cap) {
        G[from].push_back(edge{to, (int)G[to].size(), cap});
        G[to].push_back(edge{from, (int)G[from].size() - 1, cap});
    }

    void bfs(int s) {
        fill(level.begin(), level.end(), -1);
        queue<int> que;
        level[s] = 0;
        que.push(s);
        while (!que.empty()) {
            int v = que.front(); que.pop();
            for (int i = 0; i < G[v].size(); i++) {
                edge &e = G[v][i];
                if (e.cap > 0 && level[e.to] < 0) {
                    level[e.to] = level[v] + 1;
                    que.push(e.to);
                }
            }
        }
    }

    T dfs(int v, int t, T f) {
        if (v == t) return f;
        for (int &i = iter[v]; i < G[v].size(); i++) {
            edge &e = G[v][i];
            if (e.cap > 0 && level[v] < level[e.to]) {
                T d = dfs(e.to, t, min(f, e.cap));
                if (d > 0) {
                    e.cap -= d;
                    G[e.to][e.rev].cap += d;
                    return d;
                }
            }
        }
        return 0;
    }


    T max_flow(int s, int t) {
        T flow = 0;
        while (1) {
            bfs(s);
            if (level[t] < 0) return flow;
            fill(iter.begin(), iter.end(), 0);
            T f;
            while ((f = dfs(s, t, INF)) > 0) {
                flow += f;
            }
        }
    }
};


int main(void) {
    int V, E;
    cin >> V >> E;
    MaxFlowDinic<int> mf(V);
    for (int i = 0; i < E; i++) {
        int u, v, c;
        cin >> u >> v >> c;
        mf.add(u, v, c);
    }
    cout << mf.max_flow(0, V - 1) << endl;

    return 0;
}
