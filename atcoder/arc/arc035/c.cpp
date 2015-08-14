#include <iostream>
#include <algorithm>
using namespace std;
 
const int INF = 1 << 28;
 
int N, M, K, A, B, C;
int G[401][401];
 
int main(void){
  cin >> N >> M;
  for (int i = 0; i < N; i++)
    for (int j = 0; j < N; j++)
      G[i][j] = (i == j ? 0:INF);
            
  while (M--) {
    cin >> A >> B >> C;
    A--; B--;
    G[A][B] = G[B][A] = C;
  }
    
  for (int k = 0; k < N; k++)
    for (int i = 0; i < N; i++)
      for (int j = 0; j < N; j++)
	G[i][j] = min(G[i][j], G[i][k]+G[k][j]);
                
  cin >> K;
  while (K--) {
    cin >> A >> B >> C;
    A--; B--;
    G[A][B] = G[B][A] = min(G[A][B], C);
        
    for (int i = 0; i < N; i++)
      for (int j = 0; j < N; j++) 
	G[i][j] = min({G[i][j], G[i][A]+G[B][j]+C, G[i][B]+G[A][j]+C});
        
    long long ans = 0;
    for (int i = 0; i < N; i++)
      for (int j = i+1; j < N; j++)
	ans += G[i][j];
            
    cout << ans << endl;
  }
  return 0;
}
