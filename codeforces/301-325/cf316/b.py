n, m = map(int, raw_input().split())

if n == 1:
    print 1
    exit()

a1 = m - 1
a2 = m + 1
r1 = r2 = 0
if a1 >= 1:
    r1 = a1
if a2 <= n:
    r2 = n - a2 + 1
print a1 if r1 >= r2 else a2
    
