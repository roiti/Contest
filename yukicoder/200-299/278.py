from collections import defaultdict
N = int(raw_input())

num1, num2 = defaultdict(int), defaultdict(int)
n = N
i = 2
while i*i <= n:
    p = 0
    while n % i == 0:
        n /= i
        p += 1
    if p > 0:
        num1[i] = num2[i] = p
    i += 1
if n > 1:
    num1[n] = num2[n] = 1

num2[2] -= 1
n = N + 1
while i*i <= n:
    p = 0
    while n % i == 0:
        n /= i
        p += 1
    if p > 0:
        num2[i] += p
    i += 1
if n > 1:
    num2[n] += 2

ans = 1
for a, p in num1.items():
    p = min(p, num2[a])
    ans *= (pow(a, p + 1) - 1) / (a - 1)
print ans
