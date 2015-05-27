#include <iostream>
#include <vector>
#include <queue>
#define REP(i,a,b) for(int i = (a); i < (b); i++)
#define rep(i,a) REP(i,0,a)
using namespace std;

int n, indiv;
int a[200010];
vector<queue<int>> shake(200010);

void fail() {
    cout << "Impossible" << endl;
}

int main(void){
    cin >> n;
    rep(i, n) cin >> a[i];
    rep(i, n) shake[a[i]].push(i+1);
    
    vector<int> ans;

    int indiv = 0;
    while (n) {
        if (indiv >= 3 && shake[indiv].empty()) {
            while (indiv >= 3 && shake[indiv].empty()) {
                indiv -= 3;
            }
        }
        else if (!shake[indiv].empty()) {
            ans.push_back(shake[indiv].front());
            shake[indiv].pop();
            indiv++;
            n--;
        }
        else {
            fail();
            return 0;
        }
    }
    
    cout << "Possible" << endl;
    for (auto i: ans) cout << i << " ";
    cout << endl;
    return 0;
}
