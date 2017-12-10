#include <bits/stdc++.h>
#include <stdio.h>
#include <message.h>
#include "query_of_death.h"

using namespace std;
typedef long long ll;
template<typename T> using Graph = vector<vector<T>>;

#define REP(i, a, b) for (int i = (int)(a); i < (int)(b); i++)
#define rep(i, a) REP(i, 0, a)
#define EACH(i, a) for (auto i: a)
#define ITR(x, a) for (__typeof(a.begin()) x = a.begin(); x != a.end(); x++)
#define ALL(a) (a.begin()), (a.end())
#define HAS(a, x) (a.find(x) != a.end())
#define endl '\n'

#define MASTER_NODE 0
#define SLAVE_NODE 1
#define DONE -1

int main() {
  ll N = GetLength();

  ll nodes = NumberOfNodes(); // small:10, large=100
  ll unit = 10000000LL; // 10**7
  ll my_id = MyNodeId();
  ll start = my_id*unit;

  if (my_id == SLAVE_NODE) {
    bool broken = false;
    ll broken_i = 0;
    for (ll i = 0; i < N; i++) {
      int val = GetValue(i);
      for (int loop = 0; loop < 30; loop++) {
        int val2 = GetValue(i);
        if (val2 != val) {
          broken = true;
          broken_i = i;
          break;
        }
      }
      if (broken) break;
    }
    PutLL(MASTER_NODE, broken_i);
    Send(MASTER_NODE);
  }
  
  if (my_id == MASTER_NODE) {
    Receive(SLAVE_NODE);
    ll broken_i = GetLL(SLAVE_NODE);
    ll ans = 0;
    for (ll i = 0; i < N; i++) {
        if (i == broken_i) continue;
        ans += GetValue(i);
    }
    ans += GetValue(broken_i);
    printf("%lld\n", ans);
  }

  return 0;
}
