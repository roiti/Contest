N = int(raw_input())
S = raw_input()
num = [0]*10
for s in S:
    if   s  < "i": num[0] += 1
    elif s == "i": num[1] += 1
    elif s  < "k": num[2] += 1
    elif s == "k": num[3] += 1
    elif s  < "u": num[4] += 1
    elif s == "u": num[5] += 1
    elif s  < "y": num[6] += 1
    elif s == "y": num[7] += 1
    elif s  > "y": num[8] += 1

ans = 0
ans += num[8]
while num[7]:
    num[7] -= 1
    if   num[6] > 0: num[6] -= 1; ans += 1; continue
    elif num[5] > 0:
        num[5] -= 1
        if   num[4] > 0: num[4] -= 1; ans += 1; continue
        elif num[3] > 0:
            num[3] -= 1
            if   num[2] > 0: num[2] -= 1; ans += 1; continue
            elif num[1] > 0:
                num[1] -= 1
                if num[0] > 0: num[0] -= 1; ans += 1; continue

                if num[1] > 0: num[1] -= 1; ans += 1; continue
            if num[3] > 0: num[3] -= 1; ans += 1; continue
        if num[5] > 0: num[5] -= 1; ans += 1; continue
    if num[7] > 0: num[7] -= 1; ans += 1; continue
print ans
