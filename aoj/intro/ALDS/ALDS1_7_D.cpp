#include <iostream>
#include <algorithm>
using namespace std;

int n, pos;
vector<int> pre, in, post;

void rec(int l, int r) {
    if (l >= r) return;
    int root = pre[pos++];
    int m = distance(in.begin(), find(in.begin(), in.end(), root));
    rec(l, m);
    rec(m + 1, r);
    post.push_back(root);
}

void solve() {
    rec(0, n);
    for (int i = 0; i < n; i++) {
        if (i) cout << " ";
        cout << post[i];
    }
    cout << endl;
}

int main(void) {
    int k;
    cin >> n;
    for (int i = 0; i < n; i++) {
        cin >> k;
        pre.push_back(k);
    }
    for (int i = 0; i < n; i++) {
        cin >> k;
        in.push_back(k);
    }

    solve();

    return 0;
}
