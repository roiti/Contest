K, T = map(int, raw_input().split())
a = map(int, raw_input().split())
print max(max(a) - (sum(a) - max(a) + 1), 0)
