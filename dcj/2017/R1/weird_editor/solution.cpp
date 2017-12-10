#include <bits/stdc++.h>
#include <message.h>
#include <stdio.h>
#include "weird_editor.h"

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

const ll mod = 1000000007LL;

void PutVLL(int node, vector<ll> vec) {
  for (auto v: vec) PutLL(node, v);
  PutLL(node, DONE);
}

vector<ll> GetVLL(int node) {
  vector<ll> res;
  while (true) {
    ll val = GetLL(node);
    if (val == DONE) break;
    res.push_back(val);
  }
  return res;
}

ll pow_mod(ll a, ll p, ll mod) {
  ll res = 1;
  while (p > 0) {
    if (p & 1) res = res*a % mod;
    a = a*a % mod;
    p /= 2;
  }
  return res;
}

int main() {
  ll N = GetNumberLength();
  ll nodes = NumberOfNodes();

  ll my_id = MyNodeId(); // small:10, large:100
  ll unit = 10000000LL; //10**7
  ll start = unit*my_id;

  // distributed counting
  vector<ll> cnt(10);
  for (ll i = start; i < min(start + unit, N); i++) {
    ll digit = GetDigit(i);

    for (int j = 1; j < digit; j++) {
      cnt[0] += cnt[j];
      cnt[j] = 0;
    }
    cnt[digit] += 1;
  }
  PutVLL(MASTER_NODE, cnt);
  Send(MASTER_NODE);

  // master process (marge and order calc)
  vector<ll> all_cnt(10);
  if (my_id == MASTER_NODE) {
    // marge counting
    for (int node = 0; node < nodes; node++) {
      vector<ll> cnt;
      Receive(node);
      cnt = GetVLL(node);

      for (int i = 9; i >= 0; i--) {
        if (cnt[i] == 0) continue;
        for (int j = 1; j < i; j++) {
          all_cnt[0] += all_cnt[j];
          all_cnt[j] = 0;
        }
        all_cnt[i] += cnt[i];
      }
    }

    // order distributed calc
    for (int i = 9; i >= 0; i--) {
      for (int node = 0; node < nodes; node++) {
        ll num = max(0LL, min(unit, all_cnt[i] - unit*node));
        PutLL(node, i);
        PutLL(node, num);
      }
    }
    for (int node = 0; node < nodes; node++) {
      Send(node);
    }
  }
    
  // distributed calc
  Receive(MASTER_NODE);
  for (int i = 0; i < 10; i++) {
    ll res = 0;
    ll digit = GetLL(MASTER_NODE);
    ll num = GetLL(MASTER_NODE);
    for (ll j = 0; j < num; j++){
        res = (10*res + digit) % mod; 
    }
    PutLL(MASTER_NODE, res);
    Send(MASTER_NODE);
  }

  // master process (summing)
  if (my_id == MASTER_NODE) {
    ll ans = 0;
    for (int i = 9; i >= 0; i--) {
      for (int node = 0; node < nodes; node++) {
        Receive(node);
        ll val = GetLL(node);
        ll num = max(0LL, min(unit, all_cnt[i] - unit*node));
        ans = (ans*pow_mod(10, num, mod) + val) % mod;
      }
    }
    printf("%lld\n", ans);
  }

  return 0;

}
