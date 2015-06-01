#include <iostream>
#include <algorithm>
#include <map>
#include <vector>
#include <string>
#include <set>
#define REP(i,a,b) for (int i = (a); i < (int)(b); i++)
#define rep(i,a) REP(i,0,a)

using namespace std;

char field[51][51];
map<char, vector<int>> corner;
vector<char> chars;
set<char> schars;
int H, W;

bool judge(char (*field)[51], char c) {
    REP(y, corner[c][2], corner[c][3]+1)
        REP(x, corner[c][0], corner[c][1]+1) {
            if (field[y][x] != c && field[y][x] != '*')  return false;
            field[y][x] = '*';
        }
    return true;
}

string solve(vector<char> chars) {
    do {
        char cp[51][51];
        rep(y, H) rep(x, W) cp[y][x] = field[y][x];
        
        bool flag = true;
        for(char c: chars) 
            if (!judge(cp, c)) {
                flag = false;
                break;
            }
        if (flag) return "SAFE";
    } while (next_permutation(chars.begin(), chars.end()));

    return "SUSPICIOUS";
}

int main(void){
    int N;
    cin >> N;
    while (N--) {
        cin >> H >> W;
        rep(y, H) rep(x, W) cin >> field[y][x];
        chars.clear(); schars.clear(); corner.clear();
        
        rep(y, H) rep(x, W) {
            char c = field[y][x];
            if (c == '.') continue;
            
            schars.insert(c);
            if (corner.find(c) == corner.end()) {
                vector<int> vec(4);
                vec = {x, x, y, y};
                corner[c] = vec;
            }
            else {
                corner[c][0] = min(corner[c][0], x);
                corner[c][1] = max(corner[c][1], x);
                corner[c][2] = min(corner[c][2], y);
                corner[c][3] = max(corner[c][3], y);
            }
        }
        
        for (char c: schars) chars.push_back(c);
        sort(chars.begin(), chars.end());
        cout << solve(chars) << endl;
    }
    return 0;
}

