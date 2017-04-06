#ifndef KOMAKI_LOCAL
#define NDEBUG
#endif
 
#include <bits/stdc++.h>
#include <sys/time.h>
#include <unistd.h>
using namespace std;
#define i64         int64_t
#define rep(i, n)   for(i64 i = 0; i < ((i64)(n)); ++i)
#define sz(v)       ((i64)((v).size()))
#define bit(n)      (((i64)1)<<((i64)(n)))
#define all(v)      (v).begin(), (v).end()
 
std::string dbgDelim(int &i){ return (i++ == 0 ? "" : ", "); }
#define dbgEmbrace(exp) { int i = 0; os << "{"; { exp; } os << "}"; return os; }
template <class T> std::ostream& operator<<(std::ostream &os, std::vector<T> v);
template <class T> std::ostream& operator<<(std::ostream &os, std::set<T> v);
template <class T> std::ostream& operator<<(std::ostream &os, std::queue<T> q);
template <class T> std::ostream& operator<<(std::ostream &os, std::priority_queue<T> q);
template <class T, class K> std::ostream& operator<<(std::ostream &os, std::pair<T, K> p);
template <class T, class K> std::ostream& operator<<(std::ostream &os, std::map<T, K> mp);
template <class T, class K> std::ostream& operator<<(std::ostream &os, std::unordered_map<T, K> mp);
template <int INDEX, class TUPLE> void dbgDeploy(std::ostream &os, TUPLE tuple){}
template <int INDEX, class TUPLE, class H, class ...Ts> void dbgDeploy(std::ostream &os, TUPLE t)
{ os << (INDEX == 0 ? "" : ", ") << get<INDEX>(t); dbgDeploy<INDEX + 1, TUPLE, Ts...>(os, t); }
template <class T, class K> void dbgDeploy(std::ostream &os, std::pair<T, K> p, std::string delim)
{ os << "(" << p.first << delim << p.second << ")"; }
template <class ...Ts> std::ostream& operator<<(std::ostream &os, std::tuple<Ts...> t)
{ os << "("; dbgDeploy<0, std::tuple<Ts...>, Ts...>(os, t); os << ")"; return os; }
template <class T, class K> std::ostream& operator<<(std::ostream &os, std::pair<T, K> p)
{ dbgDeploy(os, p, ", "); return os; }
template <class T> std::ostream& operator<<(std::ostream &os, std::vector<T> v)
{ dbgEmbrace( for(T t: v){ os << dbgDelim(i) << t; }); }
template <class T> std::ostream& operator<<(std::ostream &os, std::set<T> s)
{ dbgEmbrace( for(T t: s){ os << dbgDelim(i) << t; }); }
template <class T> std::ostream& operator<<(std::ostream &os, std::queue<T> q)
{ dbgEmbrace( for(; q.size(); q.pop()){ os << dbgDelim(i) << q.front(); }); }
template <class T> std::ostream& operator<<(std::ostream &os, std::priority_queue<T> q)
{ dbgEmbrace( for(; q.size(); q.pop()){ os << dbgDelim(i) << q.top();   }); }
template <class T, class K> std::ostream& operator<<(std::ostream &os, std::map<T, K> mp)
{ dbgEmbrace( for(auto p: mp){ os << dbgDelim(i); dbgDeploy(os, p, "->"); }); }
template <class T, class K> std::ostream& operator<<(std::ostream &os, std::unordered_map<T, K> mp)
{ dbgEmbrace( for(auto p: mp){ os << dbgDelim(i); dbgDeploy(os, p, "->"); }); }
#define DBG_OUT std::cerr
#define DBG_OVERLOAD(_1, _2, _3, _4, _5, _6, macro_name, ...) macro_name
#define DBG_LINE() { char s[99]; sprintf(s, "line:%3d | ", __LINE__); DBG_OUT << s; }
#define DBG_OUTPUT(v) { DBG_OUT << (#v) << "=" << (v); }
#define DBG1(v, ...) { DBG_OUTPUT(v); }
#define DBG2(v, ...) { DBG_OUTPUT(v); DBG_OUT << ", "; DBG1(__VA_ARGS__); }
#define DBG3(v, ...) { DBG_OUTPUT(v); DBG_OUT << ", "; DBG2(__VA_ARGS__); }
#define DBG4(v, ...) { DBG_OUTPUT(v); DBG_OUT << ", "; DBG3(__VA_ARGS__); }
#define DBG5(v, ...) { DBG_OUTPUT(v); DBG_OUT << ", "; DBG4(__VA_ARGS__); }
#define DBG6(v, ...) { DBG_OUTPUT(v); DBG_OUT << ", "; DBG5(__VA_ARGS__); }
 
#define DEBUG0() { DBG_LINE(); DBG_OUT << std::endl; }
#define DEBUG(...)                                                        {                                                                         DBG_LINE();                                                             DBG_OVERLOAD(__VA_ARGS__, DBG6, DBG5, DBG4, DBG3, DBG2, DBG1)(__VA_ARGS__);     DBG_OUT << std::endl;                                                 }
 
 
 
 
 
 
class Timer
{
public:
  void restart();
  double getElapsed();
 
  Timer();
private:
  static double rdtsc_per_sec_inv;
 
  double getTimeOfDay();
  unsigned long long int getCycle();
 
  double start_time;
  unsigned long long int start_clock;
};
double Timer::rdtsc_per_sec_inv = -1;
 
 
inline double Timer::getElapsed()
{
  if(rdtsc_per_sec_inv != -1) return (double)(getCycle() - start_clock) * rdtsc_per_sec_inv;
 
  const double RDTSC_MEASUREMENT_INTERVAL = 0.1;
  double res = getTimeOfDay() - start_time;
  if(res <= RDTSC_MEASUREMENT_INTERVAL) return res;
 
  rdtsc_per_sec_inv = 1.0 / (getCycle() - start_clock);
  rdtsc_per_sec_inv *= getTimeOfDay() - start_time;
  return getElapsed();
}
 
inline void Timer::restart()
{
  start_time = getTimeOfDay();
  start_clock = getCycle();
}
 
Timer::Timer()
{
  restart();
}
 
inline double Timer::getTimeOfDay()
{
  timeval tv;
  gettimeofday(&tv,0);
  return tv.tv_sec + tv.tv_usec * 0.000001;
}
 
inline unsigned long long int Timer::getCycle()
{
  unsigned int low, high;
  __asm__ volatile ("rdtsc" : "=a" (low), "=d" (high));
  return ((unsigned long long int)low) | ((unsigned long long int)high << 32);
}
 
 
 
class XorShift{
public:
  static int rand();
private:
  static unsigned int x;
  static unsigned int y;
  static unsigned int z;
  static unsigned int w;
  static unsigned int t;
};
unsigned int XorShift::x = 123456789;
unsigned int XorShift::y = 362436069;
unsigned int XorShift::z = 521288629;
unsigned int XorShift::w = 88675123;
unsigned int XorShift::t = 1;
 
int XorShift::rand()
{
  t = x ^ (x << 11);
  x = y;
  y = z;
  z = w;
  w = (w ^ (w >> 19)) ^ (t ^ (t >> 8));
  return w & 0x7fffffff;
}
 
 
 
 
 
const i64 L = 30;
const i64 K = 450;
const i64 T = 10000;
class A
{
public:
  i64 cur_x;
  i64 cur_y;
  i64 final_dest_x;
  i64 final_dest_y;
  i64 first_dest_x;
  i64 first_dest_y;
 
  double scores[5];
};
A as[K];
A inputs[K];
i64 tmp[L][L];
 
i64 dxs[] = {1, 0, -1, 0, 0};
i64 dys[] = {0, 1, 0, -1, 0};
string directions = "DRUL-";
 
vector<string> solve(double weight0, double weight1)
{
  vector<string> moves;
  memset(tmp, 0, sizeof(tmp));
  rep(i, K) tmp[as[i].final_dest_x][as[i].final_dest_y] = 1;
  rep(i, K){
    i64 cnt = 0;
    rep(y, as[i].final_dest_y)if(tmp[as[i].final_dest_x][y]) cnt += 1;
    as[i].first_dest_x = as[i].final_dest_x;
    as[i].first_dest_y = cnt;
  }
 
  rep(target_y, L){
    DEBUG(target_y, sz(moves));
    i64 used[L][L];
    i64 target_used[L][L];
    while(true){
      if(5000 < sz(moves)) return vector<string>();
 
      // finished?
      {
        bool ok = true;
        rep(i, K)if(as[i].first_dest_y == target_y) {
            if (as[i].cur_x != as[i].first_dest_x || as[i].cur_y != as[i].first_dest_y) ok = false;
          }
        if(ok) break;
      }
      rep(i, K)rep(j, 5) as[i].scores[j] = j == 4 ? 0.2 : 1.0;
      memset(used, false, sizeof(used));
 
      rep(i, K) used[as[i].cur_x][as[i].cur_y] = true;
      rep(i, K){
        if(as[i].first_dest_y < target_y){
          as[i].scores[4] += 1000000000.0;
        }else if(as[i].first_dest_y == target_y){
          if(as[i].cur_y == as[i].first_dest_y && as[i].cur_x == as[i].first_dest_x){
            as[i].scores[4] += 1000.0;
          }else{
            if(as[i].first_dest_y < as[i].cur_y) as[i].scores[3] += weight0;
            if(as[i].first_dest_x < as[i].cur_x) as[i].scores[2] += weight1;
            if(as[i].first_dest_x > as[i].cur_x) as[i].scores[0] += weight1;
          }
        }else{
          if(as[i].first_dest_y > as[i].cur_y * 1.5 - 3) as[i].scores[1] += 3.0;
          if(as[i].first_dest_y > as[i].cur_y * 1.5 + 3) as[i].scores[3] += 3.0;
          if(as[i].first_dest_x < as[i].cur_x) as[i].scores[2] += 1.5;
          if(as[i].first_dest_x > as[i].cur_x) as[i].scores[0] += 1.5;
          rep(dir, 5){
            double penalty = 0.0;
            i64 r = 1;
            for(int dx = -r; dx <= r; ++dx){
              for(i64 dy = -r; dy <= r; ++dy){
                i64 x = dx + as[i].cur_x + dxs[dir];
                i64 y = dy + as[i].cur_y + dys[dir];
                if(x < 0 || L <= x) continue;
                if(y < 0 || L <= y) continue;
                if(used[x][y]) penalty += 1;
              }
            }
            penalty = penalty / ((r * 2 + 1) * (r * 2 + 1));
            //DEBUG(as[i].scores[dir]);
            as[i].scores[dir] *= (1 + penalty * 0.005);
            if(as[i].scores[dir] < 0){
              DEBUG(as[i].scores[dir], penalty);
            }
            //DEBUG(as[i].scores[dir]);
          }
        }
      }
 
      vector<pair<double, i64>> weights;
      rep(i, K){
        double weight = 0.0;
        rep(j, 5) weight += as[i].scores[j];
        weights.push_back(make_pair(weight, i));
      }
      sort(all(weights));
      reverse(all(weights));
 
      string move(K, '-');
      rep(i, K){
        i64 index = weights[i].second;
        A &a = as[index];
 
        rep(step, 5){
          bool finish = false;
          const i64 MOD = 100000000;
          double r = XorShift::rand() % MOD / double(MOD) * weights[i].first;
          rep(dir, 5){
            if(r < a.scores[dir]){
              i64 next_x = a.cur_x + dxs[dir];
              i64 next_y = a.cur_y + dys[dir];
              if(next_x < 0 || L <= next_x) break;
              if(next_y < 0 || L <= next_y) break;
              if(used[next_x][next_y]) break;
              used[next_x][next_y] = true;
              move[index] = directions[dir];
              a.cur_x = next_x;
              a.cur_y = next_y;
              finish = true;
              break;
            }
            r -= a.scores[dir];
          }
          if(finish) break;;
        }
      }
      moves.push_back(move);
    }
  }
 
 
  i64 used[L][L];
  while(true){
    memset(used, false, sizeof(used));
    rep(i, K) used[as[i].cur_x][as[i].cur_y] = 1;
 
    bool finish = true;
    string move(K, '-');
    rep(i, K){
      if(as[i].cur_y == as[i].final_dest_y) continue;
      if(used[as[i].cur_x][as[i].cur_y + 1]) continue;
      move[i] = 'R';
      as[i].cur_y += 1;
      used[as[i].cur_x][as[i].cur_y] = 1;
      finish = false;
    }
    if(finish) break;
    moves.push_back(move);
  }
 
  return moves;
}
 
 
void rotate(i64 &cur_x, i64 &cur_y)
{
  i64 x = L - 1 - cur_y;
  i64 y = cur_x;
  cur_x = x;
  cur_y = y;
}
 
vector<string> solve_rotate()
{
  vector<string> best;
  double weights0[] = {5.0, 10.0};
  double weights1[] = {5.0};
  for(double weight0: weights0){
    for(double weight1: weights1){
      rep(rot, 4){
        rep(i, K) as[i] = inputs[i];
        rep(i, K){
          rep(rot_i, rot) {
            rotate(as[i].cur_x, as[i].cur_y);
            rotate(as[i].final_dest_x, as[i].final_dest_y);
          }
        }
        vector<string> moves = solve(weight0, weight1);
        rep(rot_i, rot){
          rep(i, sz(moves))rep(j, sz(moves[i])){
              switch(moves[i][j]){
                case '_':
                  moves[i][j] = '-';
                  break;
                case 'U':
                  moves[i][j] = 'R';
                  break;
                case 'R':
                  moves[i][j] = 'D';
                  break;
                case 'L':
                  moves[i][j] = 'U';
                  break;
                case 'D':
                  moves[i][j] = 'L';
                  break;
              }
            }
        }
        DEBUG(rot, sz(moves));
        if(sz(best) == 0) best = moves;
        if(0 < sz(moves) && sz(moves) < sz(best)) best = moves;
      }
    }
  }
 
  DEBUG(sz(best));
  return best;
}
 
 
int main()
{
  i64 dummy;
  cin >> dummy >> dummy >> dummy >> dummy;
  rep(i, K) cin >> inputs[i].cur_x >> inputs[i].cur_y >> inputs[i].final_dest_x >> inputs[i].final_dest_y;
  rep(i, K) --inputs[i].cur_x;
  rep(i, K) --inputs[i].cur_y;
  rep(i, K) --inputs[i].final_dest_x;
  rep(i, K) --inputs[i].final_dest_y;
  vector<string> moves = solve_rotate();
  cout << sz(moves) << endl;
  for(string &move: moves) cout << move << endl;
}

