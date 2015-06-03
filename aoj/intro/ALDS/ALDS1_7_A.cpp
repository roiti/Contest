#include <iostream>
using namespace std;

const int nil = -1;

struct Node {int p, l, r;};
Node T[100000];
int n, D[100000];

void print(int u) {
    cout << "node " << u << ": ";
    cout << "parent = " << T[u].p << ", ";
    cout << "depth = " << D[u] << ", ";

    if (T[u].p == nil) cout << "root, ";
    else if (T[u].l == nil) cout << "leaf, ";
    else cout << "internal node, ";

    cout << "[";

    for (int i = 0, c = T[u].l; c != nil; i++, c = T[c].r) {
        if (i) cout << ", ";
        cout << c;
    }
    cout << "]" << endl;
}

void rec(int u, int p) {
    D[u] = p;
    if (T[u].r != nil) rec(T[u].r, p);
    if (T[u].l != nil) rec(T[u].l, p + 1);
}

int main(void) {
    int v, d, c, l, r;
    cin >> n;
    for (int i = 0; i < n; i++) T[i].p = T[i].l = T[i].r = nil;

    for (int i = 0; i < n; i++) {
        cin >> v >> d;
        for (int j = 0; j < d; j++) {
            cin >> c;
            if (j == 0) T[v].l = c;
            else T[l].r = c;
            l = c;
            T[c].p = v;
        }
    }

    for (int i = 0; i < n; i++) {
        if (T[i].p == nil) r = i;
    }

    rec(r, 0);

    for (int i = 0; i < n; i++) print(i);

    return 0;
}
