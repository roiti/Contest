def dodo():
    res = 0
    for i in xrange(n):
        if pos[p[i]] <= i: continue
        for j in xrange(i + 1, n):
            if pos[p[i]] >= j > i and pos[p[j]] <= i < j:
                res += j - i
                swap.append((i + 1, j + 1))
                p[i], p[j] = p[j], p[i]
    return res

def revdo():
    res = 0
    for i in xrange(n - 1, -1, -1):
        if pos[p[i]] >= i: continue
        for j in xrange(i - 1, -1, -1):
            if pos[p[j]] >= i > j and pos[p[i]] <= j < i:
                res += i - j
                swap.append((i + 1, j + 1))
                p[i], p[j] = p[j], p[i]
    return res

n = int(raw_input())
p = map(int, raw_input().split())
s = map(int, raw_input().split())
pos = [0] * (n + 1)
for i in xrange(n):
    pos[s[i]] = i

ans = 0
swap = []
while not p == s:
    ans += dodo()
    ans += revdo()

print ans
print len(swap)
for i, j in swap:
    print i, j

