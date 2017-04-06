
#define _USE_MATH_DEFINES
#include <cstdio>
#include <iostream>
#include <sstream>
#include <fstream>
#include <iomanip>
#include <algorithm>
#include <cmath>
#include <complex>
#include <string>
#include <vector>
#include <list>
#include <queue>
#include <stack>
#include <set>
#include <map>
#include <bitset>
#include <numeric>
#include <limits>
#include <climits>
#include <cfloat>
#include <functional>
#include <iterator>
using namespace std;
 
#ifdef _WIN32
#include <Windows.h>
#else
#include <sys/time.h>
#endif
 
class TicToc
{
private:
    double getCurrTime(){
    #ifdef _WIN32
        return GetTickCount() * 1e-3;
    #else
        struct timeval tv;
        gettimeofday(&tv, NULL);
        return tv.tv_sec + tv.tv_usec * 1e-6;
    #endif
    }
    double startTime;
public:
    void tic(){
        startTime = getCurrTime();
    }
    double toc(){
        return getCurrTime() - startTime;
    }
};
 
unsigned xor128(){
    static unsigned x=123456789,y=362436069,z=521288629,w=88675123;
    unsigned t;
    t=(x^(x<<11));x=y;y=z;z=w; return( w=(w^(w>>19))^(t^(t>>8)) );
}
 
void shuffle(vector<int>& v)
{
    int n = v.size();
    for(int i=0; i<n; ++i){
        int j = i + xor128() % (n - i);
        swap(v[i], v[j]);
    }
}
 
double getScore(const vector<int>& gy, const vector<int>& gx, const vector<int>& y, const vector<int>& x, int l)
{
    int n = gy.size();
    int pd = 20;
    for(int i=0; i<n; ++i)
        pd += abs(gy[i] - y[i]) + abs(gx[i] - x[i]);
 
    double pt = 10 + l * 0.01;
    double score = 1.0e7 / (pd * pt);
    return score;
}
 
const int dy[] = {-1, 1, 0, 0};
const int dx[] = {0, 0, -1, 1};
const string ds = "UDLR";
 
int main()
{
    int h, w, n, maxTurn;
    cin >> h >> w >> n >> maxTurn;
    maxTurn = min(maxTurn, 1200);
 
    vector<int> sy(n), sx(n), gy(n), gx(n);
    for(int i=0; i<n; ++i){
        cin >> sy[i] >> sx[i] >> gy[i] >> gx[i];
        -- sy[i];
        -- sx[i];
        -- gy[i];
        -- gx[i];
    }
 
    double allBestScore = 0.0;
    vector<string> ans;
    TicToc tictoc;
    tictoc.tic();
    while(tictoc.toc() < 3.5){
        vector<int> y = sy;
        vector<int> x = sx;
        vector<vector<int> > pos(h, vector<int>(w, 0));
        for(int i=0; i<n; ++i)
            pos[sy[i]][sx[i]] = 1;
 
        vector<string> act(maxTurn, string(n, '-'));
        vector<int> index(n);
        vector<int> d(4);
        for(int i=0; i<n; ++i)
            index[i] = i;
        for(int i=0; i<4; ++i)
            d[i] = i;
 
        int bestTurn = 0;
        double bestScore = getScore(gy, gx, y, x, 0);
        string lastAct;
        for(int turn=1; turn<=maxTurn; ++turn){
            shuffle(index);
 
            vector<int> yy = y;
            vector<int> xx = x;
            vector<vector<int> > pos2 = pos;
            string act2(n, '-');
            for(int i : index){
                shuffle(d);
                for(int k : d){
                    int y2 = yy[i] + dy[k];
                    int x2 = xx[i] + dx[k];
                    if(!(0 <= y2 && y2 < h && 0 <= x2 && x2 < w))
                        continue;
                    if(pos2[y2][x2] >= turn)
                        continue;
                    if(abs(gy[i] - y2) + abs(gx[i] - x2) < abs(gy[i] - yy[i]) + abs(gx[i] - xx[i])){
                        act2[i] = ds[k];
                        yy[i] = y2;
                        xx[i] = x2;
                        break;
                    }
                }
                pos2[yy[i]][xx[i]] = turn + 1;
            }
 
            double score = getScore(gy, gx, yy, xx, turn);
            if(bestScore < score){
                bestTurn = turn;
                bestScore = score;
                lastAct = act2;
            }
 
            for(int i : index){
                shuffle(d);
                bool isMove = false;
                for(int k : d){
                    int y2 = y[i] + dy[k];
                    int x2 = x[i] + dx[k];
                    if(!(0 <= y2 && y2 < h && 0 <= x2 && x2 < w))
                        continue;
                    if(pos[y2][x2] >= turn)
                        continue;
                    if(abs(gy[i] - y2) + abs(gx[i] - x2) < abs(gy[i] - y[i]) + abs(gx[i] - x[i])){
                        act[turn-1][i] = ds[k];
                        y[i] = y2;
                        x[i] = x2;
                        isMove = true;
                        break;
                    }
                }
 
                if(!isMove && xor128() % 100 < (100 - turn / 10)){ /*遠ざかる方向にも移動 */
                    shuffle(d);
                    for(int k : d){
                        int y2 = y[i] + dy[k];
                        int x2 = x[i] + dx[k];
                        if(!(0 <= y2 && y2 < h && 0 <= x2 && x2 < w))
                            continue;
                        if(pos[y2][x2] >= turn)
                            continue;
                        act[turn-1][i] = ds[k];
                        y[i] = y2;
                        x[i] = x2;
                        break;
                    }
                }
 
                pos[y[i]][x[i]] = turn + 1;
            }
        }
 
        if(allBestScore < bestScore){
            allBestScore = bestScore;
            act.resize(bestTurn);
            act.back() = lastAct;
            ans.swap(act);
        }
 
        cerr << tictoc.toc() << endl;
    }
 
    cout << ans.size() << endl;
    for(const string& s : ans)
        cout << s << endl;
 
    return 0;
}
