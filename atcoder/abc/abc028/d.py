N, K = map(int, raw_input().split())
ans = 6 * 1.0 / N * (N - K) / N * (K - 1) / N + 3 * 1.0 / N * 1.0 / N * (N - 1) / N + (1.0 / N) ** 3
print "%.15f" % ans
