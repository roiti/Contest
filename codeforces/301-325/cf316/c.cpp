#include <iostream>
#include <cstdio>
#include <string>
using namespace std;

int n, m;
string s;

int main(void) {
  cin >> n >> m;
  cin >> s;
  int ans = 0, seq = 0;
  for (int i = 0; i < n; i++) {
    if (s[i] == '.') seq++;
    else {
      ans += max(0, seq - 1);
      seq = 0;
    }
  }
  ans += max(0, seq - 1);

  while (m--) {
    int x;
    char c;
    scanf("%d %c", &x, &c);
    x--;
    if (c == '.' && s[x] != '.') {
      if (x > 0     && s[x - 1] == '.') ans++;
      if (x < n - 1 && s[x + 1] == '.') ans++;
    }
    else if (c != '.' && s[x] == '.') {
      if (x > 0     && s[x - 1] == '.') ans--;
      if (x < n - 1 && s[x + 1] == '.') ans--;
    }
    s[x] = c;
    printf("%d\n", ans);
  }
  return 0;
}
