n, k, x = map(int, raw_input().split())
a = sorted(map(int, raw_input().split()))

_bit = [0] * 70 
for ai in a:
    for i, j in enumerate(bin(ai)[2:][::-1]):
        if j == "1":
            _bit[i] += 1
ans = 0
for ai in a:
    bit = _bit[:]
    for i, j in enumerate(bin(ai)[2:][::-1]):
        if j == "1":
            bit[i] -= 1
    nai = ai * x ** k
    for i, j in enumerate(bin(nai)[2:][::-1]):
        if j == "1":
            bit[i] += 1
    tmp = 0
    for i, j in enumerate(bit):
        if j:
            tmp += 1 << i
    ans = max(ans, tmp)
print ans
