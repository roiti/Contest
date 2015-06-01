#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#define REP(i,a,b) for (int i = (a); i < (int)(b); i++)
#define rep(i,a) REP(i,0,a)

using namespace std;

vector<string> ans;

void search(string s, char c) {
    if (c == 'a') {
        ans.push_back(s);
        return;
    }
    
    rep(i, s.size()) {
        if (s[i] == c) return;
        
        if (s[i] == c-1) {
            string t(s);
            t[i] = c;
            
            search(t, c-1);
        }
    }
    search(s, c-1);
}

int main(void){
    while (1) {
        string S;
        cin >> S;
        if (S == "#") break;
        
        ans.clear();
        search(S,'z');
        
        sort(ans.begin(), ans.end());
        ans.erase(unique(ans.begin(), ans.end()), ans.end());
        
        cout << ans.size() << endl;
        if (ans.size() <= 10) {
            rep(i, ans.size()) cout << ans[i] << endl;
        }
        else {
            rep(i, 5) cout << ans[i] << endl;
            rep(i, 5) cout << ans[ans.size()-5+i] << endl;
        }
    }
    
    return 0;
}


