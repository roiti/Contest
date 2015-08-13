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
const int inf = 100000000;

class LuckyCycle {
  public:
  vector<int> getEdge(vector<int> e1, vector<int> e2, vector<int> w) {
    int N = e1.size();
    for (int i = 0; i < N; i++) e1[i]--, e2[i]--;
    vector<vector<int>> d(N + 1, vector<int>(N + 1, inf));
    for (int i = 0; i < N; i++) d[e1[i]][e2[i]] = d[e2[i]][e1[i]] = (w[i] == 4 ? 1:1000);
    
    for (int k = 0; k < N + 1; k++)
      for (int i = 0; i < N + 1; i++)
	for (int j = 0; j < N + 1; j++)
	  d[i][j] = min(d[i][j], d[i][k] + d[k][j]);
    
    for (int i = 0; i < N + 1; i++) {
      for (int j = i + 1; j < N + 1; j++) {
	if (d[i][j] == 1000 || d[i][j] == 1) continue;
	int four = d[i][j] % 1000;
	int seven = d[i][j] / 1000;
	if (abs(four - seven) == 1) {
	  int add = (four - seven == 1 ? 7:4);
	  vector<int> res = {i + 1, j + 1, add};
	  return res;
	}
      }
    }
    return vector<int>();
  }
};

