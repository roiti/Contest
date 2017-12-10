def solve():
    s = raw_input()
    n = len(s)
    ans = 0
    i, j = 0, n - 1
    while i < j:
        if s[i] != s[j]:
            if s[i] == 'x':
                ans += 1
                i += 1
            elif s[j] == 'x':
                ans += 1
                j -= 1
            else:
                return -1
        else:
            i += 1
            j -= 1
    return ans

print solve()
