n = int(raw_input())
b = map(int, raw_input().split())
b25 = b50 = 0
for bi in b:
    if bi == 25:
        b25 += 1
    if bi == 50:
        if b25 == 0:
            print "NO"
            break
        else:
           b25 -= 1
           b50 += 1
    if bi == 100:
        if min(b25, b50) == 0:
            if b25 >= 3:
                b25 -= 3
            else:
                print "NO"
                break
        else:
            b25 -= 1
            b50 -= 1
else:
    print "YES"
