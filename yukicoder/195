eps = 1e-8
def gauss_jordan(A, b):
    n = len(A)
    B = [map(float, A[i] + [b[i]]) for i in xrange(n)]

    for i in xrange(n):
        pivot = i
        for j in xrange(i, n):
            if abs(B[j][i]) > abs(B[pivot][i]): pivot = j
        B[i], B[pivot] = B[pivot], B[i]
        
        if abs(B[i][i]) < eps: return []
        
        for j in xrange(i + 1, n + 1):
            B[i][j] /= B[i][i]
        for j in xrange(0, n):
            if i != j:
                for k in xrange(i + 1, n + 1):
                    B[j][k] -= B[j][i] * B[i][k]
        
    res = [0] * n
    for i in xrange(n):
        res[i] = B[i][n]
    return res

coeff = [1, 0, 1, 1]
while coeff[-2] <= 10 ** 10:
    coeff.append(coeff[-1] + coeff[-2])
N = len(coeff)

X, Y, Z = sorted(map(int, raw_input().split()))
uniq = len(set([X, Y, Z]))
if uniq == 1:
    A = 1
    B = 99999999
    for i in xrange(1, N - 1):
        if X - coeff[i] > 0 and (X - coeff[i]) % coeff[i + 1] == 0:
            B = min(B, (X - coeff[i]) / coeff[i + 1])
    print A, B
    exit()

if uniq == 2:
    X, Y = sorted(list(set([X, Y, Z])))
    
A = B = 1e10
for i in xrange(N - 1):
    for j in xrange(N - 1):
        if i == j: continue
        Ax = [[coeff[i], coeff[i + 1]],
              [coeff[j], coeff[j + 1]]]
        b = [X, Y]
        tmp = gauss_jordan(Ax, b)
        if len(tmp) == 0: continue
        tA, tB = tmp
        if min(tA, tB) < 1 or max(abs(tA - int(tA + eps)), abs(tB - int(tB + eps))) > eps: continue
        tA, tB = int(tA + eps), int(tB + eps)
        if uniq == 3:
            for k in xrange(N - 1):
                if coeff[k] * tA + coeff[k + 1] * tB == Z:
                    break
            else:
                continue
        if tA < A or tA == A and tB < B:
            A, B = tA, tB

if max(A, B) < 1e10:
    print A, B
else:
    print -1