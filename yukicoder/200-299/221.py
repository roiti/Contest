N = int(raw_input())
P = 1000000

miss = (P - P / 10000 * N) * 0.01
correct = P / 10000 * N * 0.99
print miss / (miss + correct) * 100
