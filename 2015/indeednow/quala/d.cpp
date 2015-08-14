#include <iostream>
#include <string>
#include <vector>
#include <queue>
#include <tuple>
#include <unordered_set>
#define REP(i,a,b) for(int i = (a); i < (b); i++)
#define rep(i,a) REP(i,0,a)
using namespace std;
typedef vector<int> vi;
typedef vector<vi> vii;
 
 
int dx[] = {1,0,-1,0}, dy[] = {0,1,0,-1};
int N,sx,sy;
int H,W;
string dict = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ";
 
int getlowerbound(vii B) {
  int res = 0;
  rep(h,H) rep(w,W) {
    int tmp = B[h][w];
    int x = (tmp-1)%W;
    int y = (tmp-1)/W;
    res += abs(x-w)+abs(y-h);
  }
  return res;
}
 
bool isgoal(vii B,vii G) {
  rep(h,H) rep(w,W) {
    if (B[h][w] != G[h][w]) return false;
  }
  return true;
}
 
string gethash(vii B) {
  string res = "";
  rep(h,H) rep(w,W) {
    res += dict.at(B[h][w]);
  }
  return res;
}
 
int main(void){
  cin >> H >> W;
  vii _A(H,vi(W));
  rep(h,H) rep(w,W){
    cin >> _A[h][w];
    if (_A[h][w] == 0) {
      sx = w, sy = h;
      _A[h][w] = W*H;
    }
  }
  vii G(H,vi(W));
  rep(h,H) rep(w,W) {
    G[h][w] = (1+w)+h*W;
  }
 
  int lowbound = getlowerbound(_A);
 
  deque< tuple<vii, int, int, int> > que;
  int ans = 24;
 
  que.push_back(make_tuple(_A,0,sx,sy));
  unordered_set<string> used;
  string hash = gethash(_A);
  used.insert(hash);
  while (!que.empty()) {
    tuple<vii,int,int,int> contena;
    contena = que.front(); que.pop_front();
    vii A(H,vi(W));
    int ope, x, y;
    A   = get<0>(contena);
    ope = get<1>(contena);
    x   = get<2>(contena);
    y   = get<3>(contena);
        
    if (ope >= ans || ope == 23) continue;
        
    if (isgoal(A,G)) {
      ans = min(ans,ope);
      continue;
    }
        
    rep(i,4) {
      int nx = x+dx[i], ny = y+dy[i];
      if (0 <= nx && nx < W && 0 <= ny && ny < H) {
	vii NA(H,vi(W));
	rep(h,H) rep(w,W) NA[h][w] = A[h][w];
	int tmp = NA[y][x];
	NA[y][x] = NA[ny][nx];
	NA[ny][nx] = tmp;
	string hash = gethash(NA);
	if (used.find(hash) != used.end()) continue;
	if (getlowerbound(NA)+ope > lowbound+8) continue;
	used.insert(hash);
	que.push_back(make_tuple(NA, ope+1, nx, ny));
      }
    }
  }
  cout << ans << endl;    
  return 0;
}
