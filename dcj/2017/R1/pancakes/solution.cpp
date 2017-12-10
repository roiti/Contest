#include <bits/stdc++.h>
#include <stdio.h>
#include <message.h>
#include "pancakes.h"

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
#define DONE -1

int main() {
  ll N = GetStackSize();
  ll D = GetNumDiners();
  ll nodes = NumberOfNodes(); // small:10, large=100
  ll unit = 10000000LL; // 10**7
  ll my_id = MyNodeId();
  ll start = my_id*unit;

  if (start <= N) {
    ll res = 0;
    ll cur = GetStackItem(start);
    ll first = cur;
    for (ll i = start + 1; i < min(start + unit, N); i++) {
      ll nxt = GetStackItem(i);
      if (cur > nxt) res++;
      cur = nxt;
    }
    ll last = cur;

    PutLL(MASTER_NODE, res);
    PutLL(MASTER_NODE, first);
    PutLL(MASTER_NODE, last);
  } else {
    PutLL(MASTER_NODE, 0);
    PutLL(MASTER_NODE, 10000000000LL);
    PutLL(MASTER_NODE, -1);
  }
  Send(MASTER_NODE);

  if (my_id == MASTER_NODE) {
    ll ans = 1;
    ll first = -1, last = -1;
    for (int node = 0; node < nodes; node++) {
      Receive(node);
      ll cnt = GetLL(node);
      first  = GetLL(node);
      last   = GetLL(node);

      ans += cnt;
      if (last > first) ans++;
    }
    printf("%lld\n", ans);
  }
  return 0;
}
