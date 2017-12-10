#include <bits/stdc++.h>
using namespace std;
typedef long long ll;

#define REP(i, a, b) for (int i = (int)(a); i < (int)(b); i++)
#define rep(i, a) REP(i, 0, a)
#define EACH(i, a) for (auto i: a)
#define ITR(x, a) for (__typeof(a.begin()) x = a.begin(); x != a.end(); x++)
#define ALL(a) (a.begin()), (a.end())
#define HAS(a, x) (a.find(x) != a.end())
#define endl '\n'

int T, L, N;
ll M, D;

int main(void) {
  cin >> T;
  int testcase = 0;
  
  while (testcase++ < T) {
    cin >> L >> N >> M >> D;
    queue<int> W;
    rep(i, N) {
      int Wi;
      cin >> Wi; 
      W.push(Wi);
    }

    int washed = 0;
    int notdry = 0;
    int usedDryer = 0;
    int dryed = 0;
    ll cur = 0;
    // plan = {time, wash or dry, value(Wi or D)}
    priority_queue<tuple<ll, int, ll>> plan;

    while (washed < L) {
      if (!plan.empty()) {
        do {
          auto work = plan.top(); plan.pop();
          cur = -get<0>(work);
          if (get<1>(work) == 0) {
            // washed a load
            washed++;
            notdry++;
            W.push(get<2>(work));
          } else {
            // dryed a load
            usedDryer--;
            dryed++;
          }
        } while (!plan.empty() && cur == -get<0>(plan.top()));
      }
      
      while (!W.empty()) {
        auto Wi = W.front(); W.pop();
        plan.push(make_tuple(-(cur + Wi), 0, Wi));
      }

      while (notdry > 0 && usedDryer < M) {
        plan.push(make_tuple(-(cur + D), 1, D));
        usedDryer++;
        notdry--;
      }
    }

    while (!plan.empty()) {
      while (notdry > 0 && usedDryer < M) {
        plan.push(make_tuple(-(cur + D), 1, D));
        usedDryer++;
        notdry--;
      }

      auto work = plan.top(); plan.pop();
      if (get<1>(work) == 1) {
        usedDryer--;
        if (dryed < L) {
          cur = -get<0>(work);
          dryed++;
        } else {
          break;
        } 
      }
    }

    ll ans = cur;
    assert(washed >= L);
    assert(dryed >= L);
    printf("Case #%d: %lld\n", testcase, ans);
  }

  return 0;
}
