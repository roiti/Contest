A, B = sorted(map(int, raw_input().split()))
ans = 0
while A != B:
    if   A + 8 <= B: A += 10
    elif A + 4 <= B: A += 5
    else: A += 1
    ans += 1
    if A > B:
        ans += A - B
        A = B
print ans
 
