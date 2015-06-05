#include "bits/stdc++.h"
#define REP(i, a, b)  for (int i = (int)(a); i <  (int)(b); i++)
#define rep(i, a)  REP(i, 0, a)
using namespace std;
typedef long long ll;

class RectangleArea {
public:
    int A[51][51];
    void paint(int R, int W) {
        while (1) {
            bool update = false;
            rep(r, R) REP(rr, r + 1, R) rep(w, W) REP(ww, w + 1, W) {
                if (A[r][w] + A[r][ww] + A[rr][w] + A[rr][ww] == 3) {
                    A[r][w] = A[r][ww] = A[rr][w] = A[rr][ww] = 1;
                    update = true;
                }
            }
            if (!update) break;
        }
    }

    int minimumQueries(vector <string> known) {
        int R = known.size(), W = known[0].size();
        rep(r, R) rep(w, W) A[r][w] = (known[r][w] == 'Y' ? 1 : 0);

        int ans = 0;
        paint(R, W);
        rep(r, R) rep(w, W) {
            if (!A[r][w]) {
                A[r][w] = 1;
                paint(R, W);
                ans++;
            }
        }
        return ans;
    }
};
