def gcd(a, b):
    while b: a, b = b, a % b
    return a

N = int(raw_input())
print gcd(N, N * (N + 1) / 2)
