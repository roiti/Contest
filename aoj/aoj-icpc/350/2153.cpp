#include <iostream>
#include <deque>
#define rep(i,a) for (int i = 0; i < (a); i++)
using namespace std;

int W, H, wl, hl, wr, hr, dw, dh;
int nwl, nhl, nwr, nhr, wlg, hlg, wrg, hrg;
int dws[] = {1,0,-1,0}, dhs[] = {0,1,0,-1};
char dummy, A[51][51], B[51][51];
bool visited[51][51][51][51];

struct Array {
    int wl, hl, wr, hr;
    Array(int wl0, int hl0, int wr0, int hr0) {
        wl = wl0, hl = hl0;
        wr = wr0, hr = hr0;
    }
};
        

int main(void){
    while (cin >> W >> H, W) {
        rep(h, H) {
            rep(w, W) cin >> A[h][w];
            rep(w, W) cin >> B[h][w];
        }
        rep(h, H) {
            rep(w, W) {
                if (A[h][w] == 'L') wl  = w, hl  = h;
                if (B[h][w] == 'R') wr  = w, hr  = h;
                if (A[h][w] == '%') wlg = w, hlg = h;
                if (B[h][w] == '%') wrg = w, hrg = h;
            }
        }

        rep(i, H) rep(j, W) rep(k, H) rep(l, W) visited[i][j][k][l] = false;
        visited[hl][wl][hr][wr] = true;
        bool flag = false;
        deque<Array> que;
        que.push_back(Array(wl,hl,wr,hr));
        while (!que.empty()) {
            Array tmp = que.front(); que.pop_front();
            wl = tmp.wl, hl = tmp.hl;
            wr = tmp.wr, hr = tmp.hr;
            if (wl == wlg && hl == hlg && wr == wrg && hr == hrg) {
                cout << "Yes" << endl;
                flag = true;
                break;
            }
            
            rep(i, 4) {
                dw = dws[i], dh = dhs[i];
                nwl = min(W-1,max(0,wl+dw)), nhl = min(H-1,max(0,hl+dh));
                if (A[nhl][nwl] == '#') nwl = wl, nhl = hl;
                nwr = min(W-1,max(0,wr-dw)), nhr = min(H-1,max(0,hr+dh));
                if (B[nhr][nwr] == '#') nwr = wr, nhr = hr;
                
                if (!visited[nhl][nwl][nhr][nwr]) {
                    if ((nwl == wlg && nhl == hlg) ^ (nwr == wrg && nhr == hrg)) continue;
                    visited[nhl][nwl][nhr][nwr] = true;
                    que.push_back(Array(nwl,nhl,nwr,nhr));
                }
            }
        }
        if (!flag) cout << "No" << endl;
    }
    return 0;
}

