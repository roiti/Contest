N = int(raw_input())
s = set(range(10))
for loop in xrange(N):
    A = raw_input().split()
    if A[-1] == "YES":
        s &= set(map(int,A[:-1]))
    else:
        s -= set(map(int,A[:-1]))
print list(s)[0]