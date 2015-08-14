A,B = map(int,raw_input().split())
ans = (B//4-A//4) - (B//100-A//100) + (B//400-A//400)
etc = 0
if A%4==0:
    if A%100==0:
        if A%400==0:
            etc = 1
    else:
        etc = 1
print ans+etc
