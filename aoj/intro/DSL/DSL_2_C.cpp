#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
template<typename T> using Graph = vector<vector<T>>;

#define REP(i, a, b) for (int i = (int)(a); i < (int)(b); i++)
#define rep(i, a) REP(i, 0, a)
#define EACH(i, a) for (auto i: a)
#define ITR(x, a) for (__typeof(a.begin()) x = a.begin(); x != a.end(); x++)
#define ALL(a) (a.begin()), (a.end())
#define HAS(a, x) (a.find(x) != a.end())
#define endl '\n'

struct kdTree2D {
  struct Point{ int x, y; };
  struct Node {
    int k;
    Point p;
    Node *l, *r;
    Node(const int &k, const Point &p)
      :k(k), p(p), l(NULL), r(NULL) {}
  } *root;
  vector<int> label;

  kdTree2D(): root(NULL) {};
   
#define compare(d, p, q) (d ? p.x < q.x : p.y < q.y)
  void insert(const int &k, const Point &p) {
    root = insert(root, 0, k, p);
  }
  Node *insert(Node *t, int d, const int &k, const Point &p) {
    if (t == NULL) return new Node(k, p);
    if (compare(d, p, t->p)) t->l = insert(t->l, !d, k, p);
    else t->r = insert(t->r, !d, k, p);
    return t;
  }
  void search(const Point &ld, const Point &ru) {
    label.clear();
    search(root, 0, ld, ru);
    sort(label.begin(), label.end());
    for(auto i:label) cout << i << endl;
  }
  void search(Node *t, int d, const Point &ld, const Point &ru) {
    if (t == NULL) return;
    const Point p = t->p;
    int res = 0;
    if (ld.x <= p.x && p.x <= ru.x && ld.y <= p.y && p.y <= ru.y) label.push_back(t->k);
    if (!compare(d, p, ld)) search(t->l, !d, ld, ru);
    if (!compare(d, ru, p)) search(t->r, !d, ld, ru);
  }
};

int n, q;

int main(void) {
  cin.tie(0);
  ios::sync_with_stdio(false);

  cin >> n;
  kdTree2D kd;
  rep(i, n) {
    int x, y;
    cin >> x >> y;
    kd.insert(i, {x, y});
  }

  cin >> q;
  rep(i, q) {
    int sx, tx, sy, ty;
    cin >> sx >> tx >> sy >> ty;
    kd.search({sx, sy}, {tx, ty});
    cout << endl;
  }

  return 0;
}
