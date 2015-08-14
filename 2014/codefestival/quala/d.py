A,K = raw_input().split()
K = int(K)
 
ans = 10**16
for p in xrange(len(A)):
    for q in xrange(10):
        for r in xrange(10):
            n = A[:p] + str(q) + str(r)*(len(A)-p-1)
            if len(n) > 1 and n[0] == "0":
                n = n[1:]
            if len(set(n)) <= K:
                ans = min(ans,abs(int(A)-int(n)))
print ans
