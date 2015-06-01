#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#define REP(i,a,b) for(int i = (a); i < (b); i++)
#define rep(i,a) REP(i,0,a)
using namespace std;
typedef vector<int> vec;
typedef vector<vec> mat;

int N, M, A, B, C, T;

void init(mat &D) {
        D[N-1][N-2]           = A;
        D[0][0] = D[N-1][N-1] = B;
        D[0][1]               = C;
        REP(i,1,N-1) {
            D[i][i-1] = A;
            D[i][i]   = B;
            D[i][i+1] = C;
    }
}

mat mul(mat &A, mat&B) {
    mat C(A.size(), vec(B[0].size()));
    rep(i, A.size()) {
        rep(k, B.size()) {
            rep(j, B[0].size()) {
                C[i][j] = (C[i][j] + A[i][k] * B[k][j]) % M;
            }
        }
    }
    return C;
}

mat pow(mat A, int n) {
    mat B(A.size(), vec(A.size()));
    rep(i, A.size()) {
        B[i][i] = 1;
    }
    while (n > 0) {
        if (n & 1) B = mul(B, A);
        A = mul(A, A);
        n >>= 1;
    }
    return B;
}

int main(void){
    while (cin >> N >> M >> A >> B >> C >> T, N) {
        mat S(N, vec(1));
        rep(i, N) cin >> S[i][0];
        mat D(N, vec(N,0));
        init(D);
        D = pow(D, T);
        S = mul(D, S);
        rep(i, N) cout << (i ? " ":"") << S[i][0];
        cout << endl;
    }
    return 0;    
}

