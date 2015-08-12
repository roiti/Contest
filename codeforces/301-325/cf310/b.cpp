#include <iostream>
#include <vector>
#include <utility>
#include <algorithm>
#include <tuple>
#include <cstrio>
using namespace std;
typedef long long ll;

int n, m;
ll bl, br, l, r;
vector<pair<ll, int>> a[200005];
vector<tuple<ll, ll, int>> b[200005];

int main(void) {
    cin >> n >> m;
    cin >> bl >> br;
    for (int i = 1; i < n; i++) {
        printf("%I64d %I64d", &l, &r);
        b.push_back(make_tuple(r - bl, l - br, i));
    }
    for (int i = 0; i < m; i++) {
        ll tmp;
        printf("%i64d", &tmp);
        a.push_back(make_pair(tmp, i + 1));
    }

    sort(b.begin(), b.end());
    sort(a.begin(), a.end());

    vector<pair<int, int>> ans;

    for (int i = 0; i < n; i++) {
        
