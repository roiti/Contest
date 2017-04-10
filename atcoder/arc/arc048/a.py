A, B = map(int, raw_input().split())
if A < 0 and B > 0:
    print B + abs(A) - 1
else:
    print abs(B - A)
