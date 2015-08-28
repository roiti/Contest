import itertools as it
L1, L2, L3 = map(int, raw_input().split())
R, B, Y = map(int, raw_input().split())

ans = 100000
for l1, l2, l3 in it.permutations([L1, L2, L3], 3):
    ans = min(ans, 2 * (R * (l1 + l2) + B * (l2 + l3) + Y * (l3 + l1)))

print ans
