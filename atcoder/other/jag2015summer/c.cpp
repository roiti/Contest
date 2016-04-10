#include <bits/stdc++.h>
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
 
string S;
string abc[] = {"A", "B", "C"};
 
int count_all (string& str, const string &word) {
    string::size_type pos = 0;
    int res = 0;
    while(pos = str.find(word, pos), pos != string::npos) {
        pos += word.length();
        res++;
    }
    return res;
}
 
void replace_all (string& str, const string& from, const string& to) {
    string::size_type pos = 0;
    while(pos = str.find(from, pos), pos != string::npos) {
        str.replace(pos, from.length(), to);
        pos += to.length();
    }
}
 
bool rec(string s, int a, int b, int c) {
  //cout << s << endl;
  if (s == "ABC") return true;
  if (a + b + c <= 4) return false;
 
  int cnt = count_all(s, "ABC");
  if (cnt == 0) return false;
 
  int rep = -1;
  if      (a == cnt) rep = 0;
  else if (b == cnt) rep = 1;
  else if (c == cnt) rep = 2;
 
  if (rep == -1) return false;
 
  replace_all(s, "ABC", abc[rep]);
  if (rep == 0) b -= cnt, c -= cnt;
  if (rep == 1) a -= cnt, c -= cnt;
  if (rep == 2) a -= cnt, b -= cnt;
  return rec(s, a, b, c);
}
 
int main(void) {
  cin.tie(0);
  ios::sync_with_stdio(false);
 
  cin >> S;
  int a = count_all(S, "A");
  int b = count_all(S, "B");
  int c = count_all(S, "C");
  cout << (rec(S, a, b, c) ? "Yes":"No") << endl;
 
  return 0;
}
