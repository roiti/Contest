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
#define SUM_NODE_START 1
#define NUM_CHALLENGE 30
#define DONE -1

int main() {
  ll N = GetLength();

  ll nodes = NumberOfNodes(); // small:10, large=100
  const ll SEARCH_NODE_START = (nodes + 1)/2;
  ll unit = 2100000LL; // 2.1*10**6 (*49 > 10**8)
  ll my_id = MyNodeId();

  // distributed search broken i
  if (SEARCH_NODE_START <= my_id && my_id < nodes) {
    ll start = unit*(my_id - SEARCH_NODE_START);
    ll broken_i = -1;
    for (ll i = start; i < min(start + unit, N); i++) {
      int val = GetValue(i);
      for (int loop = 0; loop < NUM_CHALLENGE; loop++) {
        int val2 = GetValue(i);
        if (val2 != val) {
          broken_i = i;
          break;
        }
      }
      if (broken_i != -1) break;
    }
    PutLL(MASTER_NODE, broken_i);
    Send(MASTER_NODE);
  }
  
  // distributed sum
  if (SUM_NODE_START <= my_id && my_id < SEARCH_NODE_START) {
    ll start = unit*(my_id - SUM_NODE_START);
    ll res = 0;
    Receive(MASTER_NODE);
    ll broken_i = GetLL(MASTER_NODE);
    for (ll i = start; i < min(start + unit, N); i++) {
      if (i == broken_i) continue;
      res += GetValue(i);
    }
    PutLL(MASTER_NODE, res);
    Send(MASTER_NODE);
  }

  // master process
  if (my_id == MASTER_NODE) {
    // search broken i
    ll broken_i = -1;
    for (int node = SEARCH_NODE_START; node < nodes; node++) {
      Receive(node);
      ll tmp = GetLL(node);
      if (tmp != -1) {
        broken_i = tmp;
        // Don't broke! There might be a node sending message.
      }
    }

    // summing
    ll ans = 0;
    for (int node = SUM_NODE_START; node < SEARCH_NODE_START; node++) {
      PutLL(node, broken_i);
      Send(node);
    }

    for (int node = SUM_NODE_START; node < SEARCH_NODE_START; node++) {
      Receive(node);
      ans += GetLL(node);
    }

    ans += GetValue(broken_i);

    printf("%lld\n", ans);
  }

  return 0;
}
