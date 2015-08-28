def dfs(s):
    if memo[s] > 0: return memo[s]
    res = 1
    for i in xrange(s, N):
        if S[s:i + 1] == S[s:i + 1][::-1]:
            res = max(res, i - s + 1, dfs(i + 1))
    memo[s] = res
    return res

S = raw_input()
N = len(S)
memo = [0] * (N + 1)
ans = 1
for i in xrange(N - 1):
    if S[:i + 1] == S[:i + 1][::-1]:
        ans = max(ans, i + 1, dfs(i + 1))
print ans
