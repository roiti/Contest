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

  vector<pair<ll, ll>> s;
  ll cnt = 0;
  for (ll i = start; i < min(start + unit, N); i++) {
    ll digit = GetDigit(i);
    //cout << digit << endl;
    if (digit != 0) {
      while (!s.empty() && s[s.size() - 1].first < digit) {
        cnt += s[s.size() - 1].second;
        s.pop_back();
      }
      if (s.empty() || s[s.size() - 1].first > digit) {
        s.push_back(make_pair(digit, 1));
      } else {
        s[s.size() - 1].second++;
      }
    } else {
      cnt++;
    }
  }

  for (auto p: s) {
    PutLL(MASTER_NODE, p.first);
    Send(MASTER_NODE);
    PutLL(MASTER_NODE, p.second);
    Send(MASTER_NODE);
  }

  PutLL(MASTER_NODE, 0);
  Send(MASTER_NODE);
  PutLL(MASTER_NODE, cnt);
  Send(MASTER_NODE);

  PutLL(MASTER_NODE, DONE);
  Send(MASTER_NODE);

  vector<pair<ll, ll>> S;
  cnt = 0;
  if (my_id == MASTER_NODE) {
    ll ans = 0LL;
    for (int node = 0; node < nodes; node++) {
      while (true) {
        Receive(node);
        ll digit = GetLL(node);
        // cout << node << " " << digit << endl;
        if (digit == DONE) {
          break;
        }

        Receive(node);
        ll num = GetLL(node);

        if (digit != 0) {
          while (!S.empty() && S[S.size() - 1].first < digit) {
              cnt += S[S.size() - 1].second;
              S.pop_back();
          }
          if (S.empty() || S[S.size() - 1].first > digit) {
              S.push_back(make_pair(digit, num));
          } else {
              S[S.size() - 1].second += num;
          }
        } else {
          cnt += num;
        }
      }
    }

    for (auto p: S) {
      for (int node = 0; node < nodes; node++) {
        if (node == MASTER_NODE) {
          for (ll i = 0; i < min(unit, p.second); i++)
              ans = (10*ans + p.first) % mod;
          continue;
        }
        PutLL(node, p.first);
        Send(node);
        ll n = max(0LL, min(unit, p.second - node*unit + 1));
        PutLL(node, n);
        Send(node);
      }
      for (int node = 0; node < nodes; node++) {
        if (node == MASTER_NODE) continue;
        Receive(node);
        ll value = GetLL(node);
        ll n = max(0LL, min(unit, p.second - node*unit + 1));
        ans = ans * pow_mod(10, n, mod);
      }
    }
    

    for (int node = 0; node < nodes; node++) {
      if (node == MASTER_NODE) {
        for (ll i = 0; i < min(unit, cnt); i++)
            ans = 10*ans % mod;
        continue;
      }
      PutLL(node, 0);
      Send(node);
      ll n = max(0LL, min(unit, cnt - node*unit + 1));
      PutLL(node, n);
      Send(node);
    }

    for (int node = 0; node < nodes; node++) {
      if (node == MASTER_NODE) continue;
      Receive(node);
      ll value = GetLL(node);
      ll n = max(0LL, min(unit, cnt - node*unit + 1));
      ans = ans * pow_mod(10, n, mod);
    }

    for (int node = 0; node < nodes; node++) {
      if (node == MASTER_NODE) continue;
      PutLL(node, DONE);
      Send(node);
    }

    printf("%lld\n", ans);
  } else {
    while (true) {
      Receive(MASTER_NODE);
      ll first = GetLL(MASTER_NODE);
      if (first == DONE)
          break;
      Receive(MASTER_NODE);
      ll second = GetLL(MASTER_NODE);
      ll res = 0;
      for (ll i = 0; i < second; i++){
         res = (10*res + first)%mod; 
      }
      PutLL(MASTER_NODE, res);
      Send(MASTER_NODE);
    }
  }

  return 0;
}
