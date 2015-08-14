N = int(raw_input())
a = map(int, raw_input().split())
sa = sum(a)
 
if sa % N != 0:
    print -1
    exit()
    
b = sa / N
ans = N
for i in xrange(N):
    if sum(a[:i + 1]) == (i + 1) * b:
        ans -= 1
print ans
