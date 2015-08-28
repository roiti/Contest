N, M = map(int, raw_input().split())
a = 2 * N
print (a ** N % MOB) ** 3 % M
