fact = {i:0 for i in [2,3,5,7]}
n = int(raw_input())
a = raw_input()
for ai in a:
    ai = int(ai)
    if ai in [2,3,5,7]: fact[ai] += 1
    elif ai == 4:
        fact[2] += 2
        fact[3] += 1
    elif ai == 6:
        fact[3] += 1
        fact[5] += 1
    elif ai == 8:
        fact[2] += 3
        fact[7] += 1
    elif ai == 9:
        fact[2] += 1
        fact[3] += 2
        fact[7] += 1
ans = ""
for i in [7,5,3,2]:
    ans += str(i)*fact[i]
print ans
