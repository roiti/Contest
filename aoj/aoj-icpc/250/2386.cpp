#include <iostream>
#include <algorithm>
using namespace std;
int main(void){
    int N;
    long long ans = 0;
    cin >> N;
    int C[N][N];
    for (int i = 0; i < N; i++) for (int j = 0; j < N; j++) cin >> C[i][j];
    for (int i = 0; i < N; i++) for (int j = i+1; j < N; j++) ans += min(C[i][j],C[j][i]);
    cout << ans << endl;
    return 0;
}


