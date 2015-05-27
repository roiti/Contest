from itertools import combinations
def judge(s):
    if any(s[i] == s[i-Kr] == "R" for i in range(Kr,len(s))): return False
    if any(s[i] == s[i-Kb] == "B" for i in range(Kb,len(s))): return False
    return True

def rec(s):
    global ans
    if s in used or len(s) <= ans: return
    used.add(s)
    if judge(s):
        ans = len(s)
        return
    for i in range(len(s)):
        if s[i] == "W": continue
        rec(s[:i]+s[i+1:])

Kr,Kb = map(int,raw_input().split())
S = raw_input()
used = set([])
ans = 12
rec(S)
print ans