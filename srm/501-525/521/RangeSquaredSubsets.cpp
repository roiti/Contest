#include <cstdio>
#include <cmath>
#include <cstring>
#include <ctime>
#include <iostream>
#include <algorithm>
#include <string>
#include <set>
#include <vector>
#include <sstream>
#include <typeinfo>
#include <fstream>

using namespace std;

class RangeSquaredSubsets {
public:
  long long countSubsets(int, int, vector<int>, vector<int>);
};

void proc(int low, int high, vector<int>& x, vector<int>& y, set<long long>& s) {
  int n = x.size();
  vector<int> X, Y;
  for (int i = 0; i < n; i++) {
    X.push_back(x[i]);
    X.push_back(x[i] + 1);
    X.push_back(x[i] - 1);
    Y.push_back(y[i]);
    Y.push_back(y[i] + 1);
    Y.push_back(y[i] - 1);
  }
  sort(X.begin(), X.end());
  sort(Y.begin(), Y.end());

  X.erase(unique(X.begin(), X.end()), X.end());
  Y.erase(unique(Y.begin(), Y.end()), Y.end());

  int w = X.size(), h = Y.size();
  for (int i = 0; i < h; i++) {
    for (int j = 0; j < w; j++) {
      for (int k = 0; k <= h + w; k++) {
	int d;
	if (k == 0) d = low;
	else if (k <= h) d = Y[k - 1] - Y[i];
	else d = X[k - h - 1] - X[j];

	if (!(low <= d && d <= high)) continue;

	long long z = 0;
	for (int l = 0; l < n; l++) {
	  if (X[j] <= x[l] && x[l] <= X[j] + d && Y[i] <= y[l] && y[l] <= Y[i] + d)
	    z += 1LL << l;
	}
	if (z) s.insert(z);
      }
    }
  }
}

long long RangeSquaredSubsets::countSubsets(int low, int high, vector<int> x, vector<int> y) {
  int n = x.size();
  low *= 2; high *= 2;
  for (int &t: x) t *= 2;
  for (int &t: y) t *= 2;

  vector<int> _x(n), _y(n);
  for (int i = 0; i < n; i++) {
    _x[i] = -x[i];
    _y[i] = -y[i];
  }

  set<long long> s;
  proc(low, high, x, y, s);
  proc(low, high, x, _y, s);
  proc(low, high, _x, y, s);
  proc(low, high, _x, _y, s);
  return s.size();
}

