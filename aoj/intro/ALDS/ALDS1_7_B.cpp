#include <iostream>
using namespace std;

const int nil = -1;

struct Node {int p, l, r;};
Node T[10000];
int n, d[10000], sib[10000], deg[10000], h[10000];

void print(int u) {
    cout << "node " << u << ": ";
    cout << "parent = " << T[u].p << ", ";
    cout << "sibling = " << sib[u] << ", ";
    cout << "degree = " << deg[u] << ", ";
    cout << "depth = " << d[u] << ", ";
    cout << "height = " << h[u] <<  ", ";


    if (T[u].p == nil) cout << "root";
    else if (T[u].l != nil || T[u].r != nil) cout << "internal node";
    else cout << "leaf";
    cout << endl;
}

void rec_depth(int u, int p) {
    d[u] = p;
    if (T[u].r != nil) rec_depth(T[u].r, p + 1);
    if (T[u].l != nil) rec_depth(T[u].l, p + 1);
}

void rec_height(int u, int k) {
    h[u] = max(h[u], k);
    if (T[u].p != nil) rec_height(T[u].p, k + 1);
}

int main(void) {
    int p, l, r;
    cin >> n;
    for (int i = 0; i < n; i++) T[i].p = T[i].l = T[i].r = sib[i] = nil;

    for (int i = 0; i < n; i++) {
        cin >> p >> l >> r;
        T[p].l = l;
        T[p].r = r;
        T[l].p = T[r].p = p;
        sib[r] = l;
        sib[l] = r;
        deg[p] = min(1, l + 1) + min(1, r + 1);
    }

    for (int i = 0; i < n; i++) {
        if (T[i].p == nil) rec_depth(i, 0);
        if (T[i].l == nil && T[i].r == nil) rec_height(i, 0);
    }

    for (int i = 0; i < n; i++) print(i);

    return 0;
}
