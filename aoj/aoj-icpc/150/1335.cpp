#include <iostream>
using namespace std;

int n,k,s;

int dfs(int i, int k, int s) {
    if (k == 0 && s == 0) return 1;
    if (i > n || k == 0 && s != 0 || s < i*k+k-1) return 0;
    return dfs(i+1,k,s)+dfs(i+1,k-1,s-i);
}

int main(void){
    while (1) {
        cin >> n >> k >> s;
        if (n == 0 && k == 0 && s == 0) break;
        
        cout << dfs(1,k,s) << endl;
    }
    return 0;
}

