s = raw_input()
ans = ""
b = s[0]
cnt = 1
for si in s[1:]:
    if si!= b:
        ans += b+str(cnt)
        b = si
        cnt = 1
    else:
        cnt += 1
if cnt > 0: ans += b+str(cnt)
print ans
