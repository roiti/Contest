n = int(raw_input())
abc = sorted(int(raw_input()) for _ in range(3))[::-1]
a,b,c = abc
budge = 0
ans = 0
while budge < n:
    if ans%3 == 0: budge += a
    if ans%3 == 1: budge += b
    if ans%3 == 2: budge += c
    ans += 1
print ans
