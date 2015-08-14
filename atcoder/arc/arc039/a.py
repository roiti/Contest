A, B = raw_input().split()
ans = int(A) - int(B)
for a in xrange(100, 1000):
    diff = 0
    for i, j in zip(str(a), A):
        if i != j: diff += 1
        
    if diff == 0:
        for b in xrange(100, 1000):
            diff = 0
            for i, j in zip(str(b), B):
                if i != j: diff += 1
            if diff <= 1:
                ans = max(ans, a - b)
    elif diff == 1:
        ans = max(ans, a - int(B))
        
print ans
