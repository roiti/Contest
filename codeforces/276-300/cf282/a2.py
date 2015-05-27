possible = [2,7,2,3,3,4,2,5,1,2]
digit = raw_input()
ans = 1
for i in digit:
    ans *= possible[int(i)]
print ans
