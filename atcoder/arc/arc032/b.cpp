#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;
const int MAX = 100000;
 
int N,M;
int visited[MAX];
vector<int> G[MAX];
 
void dfs(int i){
  visited[i] = true;
  for (vector<int>::iterator it = G[i].begin(); it < G[i].end(); it++){
    if (not visited[*it])
      dfs(*it);
  }
}
 
int main(void){
  // initilization
  for (int i = 0; i < MAX; i++) visited[i] = false;
 
  cin >> N >> M;
  for (int i = 0; i < M; i++){
    int a,b;
    cin >> a >> b;
    a--, b--;
    G[a].push_back(b);
    G[b].push_back(a);
  }
    
  int cnt = 0;
  for (int i = 0; i < N; i++){
    if (visited[i]) continue;
    dfs(i), cnt++;
  }
 
  cout << cnt-1 << endl;
 
  return 0;
}
