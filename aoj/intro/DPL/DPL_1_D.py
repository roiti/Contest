import bisect
def lis(A):
    n = len(A)
    L = [0] * n
    L[0] = A[0]
    length = 1

    for i in xrange(1, n):
        if L[length - 1] < A[i]:
            L[length] = A[i]
            length += 1
        else:
            L[bisect.bisect_left(L[:length], A[i])] = A[i]

    return length

n = int(raw_input())
a = [int(raw_input()) for i in xrange(n)]
print lis(a)

