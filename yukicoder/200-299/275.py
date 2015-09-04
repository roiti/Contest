n = int(raw_input())
a = sorted(map(int, raw_input().split()))
print (a[n/2] + a[(n - 1) / 2]) / 2.0
