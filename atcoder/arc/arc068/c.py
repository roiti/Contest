x = int(raw_input())
ans = (x + 10)/11*2
x %= 11
if 0 < x <= 6:
    ans -= 1
print ans
