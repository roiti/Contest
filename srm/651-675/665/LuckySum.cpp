#include <cstdio>
#include <cmath>
#include <cstring>
#include <ctime>
#include <iostream>
#include <algorithm>
#include <set>
#include <vector>
#include <sstream>
#include <typeinfo>
#include <fstream>

using namespace std;
typedef long long ll;

class LuckySum {

int l, a[1000];
ll ans = -1L;

public:
  void dfs(int pos, int alive, int carry, ll num, ll step) {
    if (pos == -1) {
      if (carry == 1)
	return;
      if (ans == -1L || num < ans){
	ans = num;
      }
      return;
    }

    if (alive == 0) {
      test_add(pos, alive, carry, num, step, 0);
      return;
    }

    if (pos != l - 1)
      dfs(pos, alive - 1, carry, num, step);

    if (alive == 1) {
      test_add(pos, alive, carry, num, step, 4);
      test_add(pos, alive, carry, num, step, 7);
    } else {
      test_add(pos, alive, carry, num, step, 8);
      test_add(pos, alive, carry, num, step, 11);
      test_add(pos, alive, carry, num, step, 14);
    }
  }
  
  void test_add(int pos, int alive, int carry, ll num, ll step, int add) {
    int digit = add + carry;
    int ncarry = 0;
    if (digit >= 10) {
      digit -= 10;
      ncarry = 1;
    }
    if (pos == 0 and digit == 0) {
      return;
    }
    if (a[pos] != -1 && a[pos] != digit) {
      return ;
    }
    dfs(pos - 1, alive, ncarry, num + step * digit, step * 10);
  }

  long long construct(string note) {
    l = note.size();
    for (int i = 0; i < l; i++) {
      if (note[i] == '?') a[i] = -1;
      else a[i] = note[i] - '0';
    }
    dfs(l - 1, 2, 0, 0L, 1L);
    return ans;
  }
};

