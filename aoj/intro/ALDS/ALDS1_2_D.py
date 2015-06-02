def shellsort(A):
    def insertionSort(A, g):
        cnt = 0
        for i in xrange(g, len(A)):
            v = A[i]
            j = i - g
            while j >= 0 and A[j] > v:
                A[j + g] = A[j]
                j = j - g
                cnt += 1
            A[j + g] = v
        return cnt
    cnt = 0
    G = []
    h = 1
    while h <= n:
        G.append(h)
        h = 3 * h + 1
    G = G[::-1]
    print len(G)
    print " ".join(map(str, G))
    for i in G:
        cnt += insertionSort(A, i)
    print cnt

n = int(raw_input())
A = [int(raw_input()) for i in xrange(n)]
shellsort(A)
for i in A:
    print i
