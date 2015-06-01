#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <set>
#define REP(i,a,b) for (int i = (a); i < (b); i++)
#define rep(i,a) REP(i,0,a)
using namespace std;

int H, W;
int dw[] = {1,1,0,-1,-1,-1,0,1};
int dh[] = {0,1,1,1,0,-1,-1,-1};

int main(void){
    while (cin >> H >> W && H) {
        vector<string> S(H,"");
        rep(i, H) cin >> S[i];
        string ans = "";
        set<string> appear;
        
        rep(h, H) rep(w, W) rep(i, 8) {
            string s = "";
            s += S[h][w];
            int iw = w, ih = h;
            w = (w+dw[i]+W)%W; h = (h+dh[i]+H)%H;
            while (!(w == iw && h == ih)) {
                s.append(1, S[h][w]);
                if (s.length() >= ans.length() && appear.find(s) != appear.end()) {
                    if (s.length()  > ans.length()) ans = s;
                    if (s.length() == ans.length()) ans = min(ans, s);
                }
                appear.insert(s);
                w = (w+dw[i]+W)%W; h = (h+dh[i]+H)%H;
            }
        }
        cout << (ans.length() > 1 ? ans:"0") << endl;
    }
    return 0;
}


