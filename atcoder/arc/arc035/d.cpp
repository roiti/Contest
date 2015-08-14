#include <iostream>
#include <vector>
#include <cstdio>
#include <cmath>
 
using namespace std;
 
class BIT {
private:
  typedef double T;
  int n;
  vector<T> data;
 
public:
  BIT(int n){
    this->n = n;
    data.assign(n+1, 0);
  }
  void add(int i, T x){
    i++;
    while(i <= n){
      data[i] += x;
      i += i & -i;
    }
  }
  T sum(int i){
    i++;
    T ret = 0;
    while(i > 0){
      ret += data[i];
      i -= i & -i;
    }
    return ret;
  }
 
  T sum(int a, int b){
    return sum(b) - sum(a-1);
  }
};
 
int main() {
  vector<double> f(2000001,0);
  f[0] = 0.0;
  for(int i = 1; i <= 2000000; i++)
    f[i] = f[i-1] + log((double)i);
 
  int n;
  cin >> n;
  vector<int> p(n+2), q(n+2);
  p[0] = q[0] = 1;
  for(int i = 1; i <= n; i++)
    cin >> p[i] >> q[i];
 
  BIT bit(n+1);
  for(int i = 1; i < n; i++) {
    int x = abs(p[i] - p[i+1]);
    int y = abs(q[i] - q[i+1]);
    double tmp = f[x+y] - f[x] - f[y];
    bit.add(i, tmp);
  }
 
  int Q;
  cin >> Q;
  while(Q--){
    int t;
    cin >> t;
    if (t == 1){
      int k, a, b;
      cin >> k >> a >> b;
      p[k] = a;
      q[k] = b;
      for(int i = k-1; i <= k; i++){
	int x = abs(p[i] - p[i+1]);
	int y = abs(q[i] - q[i+1]);
	double tmp = f[x+y] - f[x] - f[y];
	bit.add(i, tmp - bit.sum(i, i));
      }
    }
    else {
      int l1, r1, l2, r2;
      cin >> l1 >> r1 >> l2 >> r2;
      if (bit.sum(l1, r1 - 1) > bit.sum(l2, r2 - 1))
	cout << "FIRST" << endl;
      else
	cout << "SECOND" << endl;
    }
  }
 
  return 0;
}
