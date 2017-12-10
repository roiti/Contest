#include <bits/stdc++.h>
#include <message.h>
#include <stdio.h>
#include "todd_and_steven.h"
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
const ll mod = 1000000007LL; //10**9 + 7
const ll inf = 10000000000000LL; //10**13

int main() {
  ll todd_L = GetToddLength();
  ll stev_L = GetStevenLength();

  ll nodes = NumberOfNodes(); // small:10, large:100
  ll unit = 10000000LL; // 10**7
  ll my_id = MyNodeId();

  if (my_id == MASTER_NODE) {
    ll ans = 0;
    ll t_i = 0, s_i = 0;
    ll b_t = GetToddValue(0);
    ll b_s = GetStevenValue(0);
    for (ll t_j = min(N - 1, unit); t_j < N; t_ += unit) {
      ll t = GetToddValue(t_);
      ll lo = b_s, hi = N - 1;
      while (hi - lo > 1) {
        ll mi = (hi + lo)/2;
        s = GetStevenValue(mi);
        if (s >= t) hi = mi - 1;
      }
    
      while (t_i < todd_L || s_i < stev_L) {
      if (t < s) {
        ans = (ans + t^(t_i + s_i)) % mod;
        t_i++;
        if (t_i == todd_L) t = inf;
        else t = GetToddValue(t_i);
      } else {
        ans = (ans + s^(t_i + s_i)) % mod;
        s_i++;
        if (s_i == stev_L) s = inf;
        else s = GetStevenValue(s_i);
      }
    }

    printf("%lld\n", ans);
  }

    while (t_i < todd_L || s_i < stev_L) {
      if (t < s) {
        ans = (ans + t^(t_i + s_i)) % mod;
        t_i++;
        if (t_i == todd_L) t = inf;
        else t = GetToddValue(t_i);
      } else {
        ans = (ans + s^(t_i + s_i)) % mod;
        s_i++;
        if (s_i == stev_L) s = inf;
        else s = GetStevenValue(s_i);
      }
  // master process (summing)
  if (my_id == MASTER_NODE) {
    ll ans = 0;
    for (int node = 0; node < nodes; node++) {
      Receive(node);
      ans = (ans + GetLL(node)) % mod;
    }
    printf("%lld\n", ans);
  }

  return 0;
}
