#include <iostream>
#include <vector>
using namespace std;

const int MAX = 500000, SENTINEL = 2100000000;
int L[MAX / 2 + 2], R[MAX / 2 + 2];
int cnt;

void merge(int A[], int n, int left, int mid, int right) {
    int n1 = mid - left;
    int n2 = right - mid;
    for (int i = 0; i < n1; i++) L[i] = A[left + i];
    for (int i = 0; i < n2; i++) R[i] = A[mid + i];
    L[n1] = R[n2] = SENTINEL;
    int i = 0, j = 0;
    for (int k = left; k < right; k++) {
        cnt++;
        if (L[i] <= R[j]) {
            A[k] = L[i++];
        } else {
            A[k] = R[j++];
        }
    }
}

void msort(int A[], int n, int left, int right) {
    if (left + 1 < right) {
        int mid = (left + right) / 2;
        msort(A, n, left, mid);
        msort(A, n, mid, right);
        merge(A, n, left, mid, right);
    }
}


int main(void) {
    int n, A[MAX];
    cnt = 0;

    cin >> n;
    for (int i = 0; i < n; i++) cin >> A[i];

    msort(A, n, 0, n);

    for (int i = 0; i < n; i++) {
        if (i) cout << " ";
        cout << A[i];
    }
    cout << endl;
    cout << cnt << endl;

    return 0;
}
