n, w = map(int, raw_input().split())
a = map(int, raw_input().split())
a.sort()

mg, mb = a[0], a[n]
m = min(mg, mb / 2.0)

ans = min(3 * n * m, w)
print ans

