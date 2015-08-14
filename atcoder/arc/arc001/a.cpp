#include <iostream>
#include <algorithm>
#include <vector>
#include <string>
using namespace std;
int main(void){
    int N;
    cin >> N;
    string c;
    cin >> c;
    vector<int> score(4, 0);
    for (int i = 0; i < c.size(); i++) score[c[i] - '1']++;
    cout << *max_element(score.begin(), score.end()) <<   << *min_element(score.begin(), score.end()) << endl;
    return 0;
}

