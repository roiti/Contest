#include <iostream>
#include <algorithm>
using namespace std;
 
long long salary[110][110][110];
 
int main(void){
  int N,M;
  cin >> N >> M;
  for (int loop = 0; loop < N; loop++) {
    int a,b,c;
    long long w;
    cin >> a >> b >> c >> w;
    for (int i = a; i < 102; i++) {
      for (int j = b; j < 102; j++) {
	for (int k = c; k < 102; k++) {
	  if (salary[i][j][k] >= w) break;
	  salary[i][j][k] = w;
	}
      }
    }
  }
  for (int loop = 0; loop < M; loop++) {
    int a,b,c;
    cin >> a >> b >> c;
    cout << salary[a][b][c] << endl;
  }
  return 0;
}
