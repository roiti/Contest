#include <iostream>
typedef long long ll;
using namespace std;
int main(void){
   ll N, a, n, cnt;
   cnt = 0;
   char c;
   cin >> N;
   while (N--) {
       cin >> a >> c >> n;
       cnt += (c == '(' ? n:-n);
       cout << (cnt == 0 ? "Yes":"No") << endl;
   }
    return 0;
}


