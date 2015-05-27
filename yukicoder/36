N = int(raw_input())
cnt = 0
i = 2
while i * i <= N:
    while N % i == 0:
        cnt += 1
        N /= i
    i += 1
if N > 1: cnt += 1
print "YES" if cnt > 2 else "NO"