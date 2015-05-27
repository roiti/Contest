def dfs(A,B,w):
    n = len(A)
    if n == 0: return 1 if w > N/2 else 0
    res = 0
    for i in range(n):
        for j in range(n):
            a = [A[k] for k in range(n) if k != i]
            b = [B[k] for k in range(n) if k != j]
            if A[i] > B[j]:
                res += dfs(a,b,w+1)
            else:
                res += dfs(a,b,w)
    return res*1.0/n/n

N = int(raw_input())
A = map(int,raw_input().split())
B = map(int,raw_input().split())

print dfs(A,B,0)
