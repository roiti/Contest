#include <iostream>
#include <cmath>
#include <cstdio>
using namespace std;

const double th = M_PI * 60 / 180.0;

struct Point {double x, y;};

void print(Point a) {
    printf("%.8f %.8f\n", a.x, a.y);
}

void koch(int n, Point a, Point b) {
    if (n == 0) return;
    Point s, t, u;

    s.x = (2.0 * a.x + 1.0 * b.x) / 3.0;
    s.y = (2.0 * a.y + 1.0 * b.y) / 3.0;
    t.x = (1.0 * a.x + 2.0 * b.x) / 3.0;
    t.y = (1.0 * a.y + 2.0 * b.y) / 3.0;
    u.x = (t.x - s.x) * cos(th) - (t.y - s.y) * sin(th) + s.x;
    u.y = (t.x - s.x) * sin(th) + (t.y - s.y) * cos(th) + s.y;

    koch(n - 1, a, s); print(s);
    koch(n - 1, s, u); print(u);
    koch(n - 1, u, t); print(t);
    koch(n - 1, t, b);
}

int main(void) {
    int n;
    cin >> n;
    Point a = {0, 0};
    Point b = {100, 0};
    print(a);
    koch(n, a, b);
    print(b);
    return 0;
}
