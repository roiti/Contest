#include <iostream>
#include <cstdio>
#include <queue>
#include <utility>
#include <vector>
using namespace std;

int n;
double p[1001], q[1001];

int main(void) {
    cin >> n;
    for (int i = 0; i < n; i++) cin >> p[i], p[i] /= 1000.0;
    for (int i = 0; i < n; i++) cin >> q[i], q[i] /= 100.0;
    priority_queue<pair<double, int>> que;
    for (int i = 0; i < n; i++) que.push(make_pair(p[i] * q[i], i));

    double ans = 0.0;
    for (int i = 1;;i++) {
        auto pqj = que.top();
        que.pop();
        double pq = pqj.first;
        int j = pqj.second;
        ans += i * pq;
        if (i * pq < 1e-6) break;
        que.push(make_pair(pq * (1.0 - q[j]), j));
    }

    printf("%.10lf\n", ans);

    return 0;
}
