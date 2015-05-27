import sys
sys.setrecursionlimit(100000)
def get_pow(n):
    if n == 1: return [1]
    res = []
    i = 2
    while i*i <= n:
        cnt = 0
        while n%i == 0:
            n /= i
            cnt += 1
        if cnt > 0: res.append(cnt)
        i += 1
    if n > 1: res.append(1)
    return res

N = int(raw_input())
M = map(int,raw_input().split())
x = 0
for Mi in M:
    for stone in get_pow(Mi): x ^= stone%3
print "Alice" if x != 0 else "Bob"
