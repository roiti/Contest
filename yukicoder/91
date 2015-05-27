R,G,B = map(int,raw_input().split())
M = min(R,G,B)
R,G = sorted([R-M,G-M,B-M],reverse = True)[:2]
ans = M
while 1:
    if R >= G > 0 and R >= 3  : R -= 3; G -= 1
    elif G >= R > 0 and G >= 3: R -= 1;G -= 3
    elif G == 0 and R >= 5    : R -= 5
    elif R == 0 and G >= 5    : G -= 5
    else: break
    ans += 1
print ans