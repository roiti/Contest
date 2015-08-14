t,a,b = map(int,raw_input().split())
if t==2 and a==3 and b>10000: ans = 0
elif a==t:
    if a ==b:ans = inf if a==1 else 2
    else: ans = 0
else:
    if (a-b)%(t-a): ans = 0
    else: ans = 1 if t != b else 0
print ans
