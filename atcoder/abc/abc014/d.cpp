#include <iostream>
#include <vector>
#define FOR(i,a,b) for(int i=(a); i<(b); i++)
#define REP(i,a) FOR(i,0,a)
using namespace std;
 
const int MAXN = 1000001;
const int MAXM = 20; //2**20 = 1048576 > MAXN = 1000001
 
int N,Q,x,y,a,b;
int fs[MAXM][MAXN]; // fs[i][j]はノードjの2**i上のparentを格納する
vector<int> d(MAXN,-2); //各ノードの深さを格納。-2で初期化し未格納を表す。
vector<int> G[MAXN];  //ノードの連結を格納
 
// 全ノードのdepthと1つ上のparentについてdとfsに格納する。
void dfs(int index, int parent, int depth){
  d[index] = depth;
  fs[0][index] = parent;
 
  REP(i,G[index].size())
    if (d[G[index][i]] == -2)
      dfs(G[index][i],index,depth+1);
}
 
// 2ノードの共通祖先のうち最も近いもののノード番号を返す。
int lca(int aa, int bb){
  int a = aa; int b = bb;
  // 2ノードの深さを合わせる
  if (d[a] != d[b]){
    bool ab = d[a]<d[b];
    int len = ab ? d[b]-d[a]:d[a]-d[b];
    int c = ab? b:a;
    // fsのparent情報を利用して、効率的に根方向にたどっていく。
    REP(i,MAXM) if ((len>>i)&1) c = fs[i][c];
    a = ab ? a:c;
    b = ab ? c:b;
  }
 
  if (a == b) return a;
    
  // 2ノードが衝突する直前まで根の方向にたどる。
  // i = MAXM-1から調べることで処理が早くなる。
  for (int i = MAXM-2; i > -1; i--)
    if (fs[i][a] != fs[i][b]){
      a = fs[i][a];
      b = fs[i][b];
    }
        
  return fs[0][a];
}
 
int main(void){
  cin >> N;
  REP(i,N-1){
    cin >> x >> y;
    x--;y--;
    // 各ノード間のつながりを格納していく
    G[x].push_back(y);
    G[y].push_back(x);
  } 
    
  // ノード0を根として、各ノードのdepthと1つ上のparentを求める
  dfs(0,-1,0);
 
  // 各ノードの2**(i+1)上のparentのノード番号を格納していく。
  // fs[i][fs[i][j]] はノードjの2**i上のparentのさらに2**i上のparent
  // つまり2**(i+1)上のparentを指す。根をより上の場合は-1。
  REP(i,MAXM-1)
    REP(j,N)
    fs[i+1][j] = (fs[i][j] == -1 ? -1:fs[i][fs[i][j]]);
            
  cin >> Q;
  REP(i,Q){
    cin >> a >> b;
    a--; b--;
    cout << d[a]+d[b]-2*d[lca(a,b)]+1 << endl;
  }
  return 0;
}
