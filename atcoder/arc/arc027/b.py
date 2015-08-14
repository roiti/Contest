num = "0123456789"
N = int(raw_input())
A = raw_input()
B = raw_input()
while A != B:
    for i in range(N):
        if A[i] != B[i]:
            if A[i] in num:
                A = A.replace(B[i],A[i])
                B = B.replace(B[i],A[i])
            if B[i] in num:
                B = B.replace(A[i],B[i])
                A = A.replace(A[i],B[i])
            else:
                A = A.replace(B[i],A[i])
                B = B.replace(B[i],A[i])
ref = []
ans = 1
for i in range(N):
    if A[i] not in num and A[i] not in ref:
        ans *= 9 if i == 0 else 10
        ref += A[i]
print ans
