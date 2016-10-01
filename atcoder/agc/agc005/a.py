X = raw_input()
ans = ""
for c in X:
    ans += c
    if len(ans) >= 2 and ans[-2:] == "ST":
        ans = ans[:-2]
print len(ans)
