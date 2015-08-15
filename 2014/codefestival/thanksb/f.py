import sys
sys.setrecursionlimit(10000)
mod = 10**9+7
 
def solve(x):
    if not x: return 1
    res = 0
    if x.endswith(s):
        nxt = x[:-len(s)]
        if nxt not in table:
            table[nxt] = solve(nxt)
        res += table[nxt]
    if x.endswith(t):
        nxt = x[:-len(t)]
        if nxt not in table:
            table[nxt] = solve(nxt)
        res += table[nxt]
    return res
    
x = raw_input()
s = raw_input()
t = raw_input()
table = {}
print solve(x)%mod
