A = raw_input()
diff = 0
N = len(A)
for i in xrange(N / 2):
    if A[i] != A[-i - 1]:
        diff += 1

ans = 25 * N
if diff == 0:
    if N % 2 == 1:
        ans -= 25
elif diff == 1:
    ans -= 2
print ans
