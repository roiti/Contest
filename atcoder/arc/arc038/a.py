N = int(raw_input())
A = sorted(map(int, raw_input().split()), reverse = True)
print sum(A[::2])
