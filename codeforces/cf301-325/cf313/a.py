a1, a2, a3, a4, a5, a6 = map(int, raw_input().split())

l = a1 + a2 + a3
ans = l * l - a1 * a1 - a3 * a3 - a5 * a5
print ans
