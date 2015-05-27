D = int(raw_input())
s = ["x"] * 15 + list(raw_input() + raw_input()) + ["x"] * 15
ans = 0
for d in xrange(0, D + 1):
    for i in xrange(len(s)):
        if "o" in s[i:i + d]: continue
        ss = s[:]
        ss[i:i + d] = "o" * d
        cnt = 0
        for si in ss:
            if si == "o": cnt += 1
            else:
                ans = max(ans, cnt)
                cnt = 0
        ans = max(ans, cnt)
print ans
