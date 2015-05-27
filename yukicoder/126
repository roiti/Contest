a,b,s = map(int,raw_input().split())
if s == 1:
    ans = abs(a-s)+s
else:
    if abs(a-s) <= abs(b-s):
        ans = abs(a-s)+s
    else:
        ans = abs(b-s)
        if s-1 < abs(a-s):
            ans += s-1+abs(a-1)+1
        else:
            ans += abs(a-s)+a
print ans