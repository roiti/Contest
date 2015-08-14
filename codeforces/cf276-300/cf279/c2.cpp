#include <iostream>
#include <string>
typedef long long i64;
using namespace std;

int main(void){
    bool flag = false;
    i64 a,b;
    string key;
    cin >> key;
    i64 l = key.size();
    cin >> a >> b;
    i64 ma = 0;
    i64 mb[l];
    mb[l-1] = (key[l-1]-0)%b;
    i64 t = 10;
    for (i64 i = l-2; i > -1; i--){
        mb[i] = (mb[i+1]+(key[i]-0)*t)%b;
        t = t*10%b;
    }
    for (i64 i = 1; i < l; i++){
        ma = (10*ma+(key[i-1]-0))%a;
        if (key[i] != 0 && ma == 0 && mb[i] == 0){
            cout << "YES" << endl;
            for (i64 j = 0; j < i; j++) cout << key[j];
            cout << endl;
            for (i64 j = i; j < l; j++) cout << key[j];
            cout << endl;
            flag = true;
            break;
        }
    }
    if (!flag)
        cout << "NO" << endl;
    return 0;
}
