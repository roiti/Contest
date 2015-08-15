MX = 10 ** 5 + 1
N = int(raw_input())
A = map(int, raw_input().split())

used = [False] * MX
ans = i = j = 0
while j < N:
    if not used[A[j]]:
        used[A[j]] = True
        j += 1
        ans = max(ans, j - i)
    else:
        while A[i] != A[j]:
            used[A[i]] = False
            i += 1
        i += 1
        j += 1
print ans
