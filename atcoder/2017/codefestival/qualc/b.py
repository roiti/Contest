N = int(raw_input())
A = map(int, raw_input().split())   
even = 0
odd = 1
for ai in A:
    if ai % 2 == 0:
        even = 3*even + odd
        odd = 2*odd
    else:
        even = 3*even + 2*odd
        odd = odd
print even
