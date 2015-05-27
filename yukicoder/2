def get_pow(n):
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
x = 0
for stone in get_pow(N): x ^= stone
print "Alice" if x != 0 else "Bob"