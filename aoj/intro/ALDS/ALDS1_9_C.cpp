#include <iostream>
#include <vector>
using namespace std;

int n;
vector<int> A;

void maxHeapify(vector<int>& A, int i) {
    int l = 2 * i + 1;
    int r = 2 * i + 2;

    int largest = i;
    if (l < n && A[l] > A[largest]) largest = l;
    if (r < n && A[r] > A[largest]) largest = r;

    if (largest != i){
        swap(A[i], A[largest]);
        maxHeapify(A, largest);
    }
}

void maxHeap(vector<int>& A) {
    for (int i = (n - 1)/ 2; i >= 0; i--)
        maxHeapify(A, i);
}

int main(void) {
    cin >> n;
    string comm;
    int k;
    cin >> comm;
    if (comm == "insert") {
    for (int i = 0; i < n; i++) {
        cin >> k;
        A.push_back(k);
    }

    maxHeap(A);

    for (int i = 0; i < n; i++) cout << " " << A[i];
    cout << endl;

    return 0;
}
