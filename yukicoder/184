#include <iostream>
using namespace std;

int N;
long long A[100010];

int main(void){
    cin >> N;
    for (int i = 0; i < N; i++) cin >> A[i];
    int rank = 0;
    for (int i = 0; i < 61; i++) {
        int j = rank;
        while (j < N) {
            if ((A[j] >> i) & 1) break;
            j++;
        }
        if (j < N) {
            swap(A[j], A[rank]);
            for (int k = rank + 1; k < N; k++) {
                if ((A[k] >> i) & 1) A[k] ^= A[rank];
            }
            rank++;
        }
    }
    cout << (1LL << rank) << endl;
    
    return 0;
}
