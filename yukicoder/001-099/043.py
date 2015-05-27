N = int(raw_input())
s = [raw_input() for _ in range(N)]
remain = [[i,j] for i in range(N) for j in range(i+1,N) if s[i][j] == "-"]
ans = 6
for i in range(2**len(remain)):
    win = [si.count("o") for si in s]
    for a,b in remain:
        win[[a,b][i&1]] += 1
        i >>= 1
    ans = min(ans, sorted(list(set(win)))[::-1].index(win[0])+1)
print ans