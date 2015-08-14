import string
N = int(raw_input())
print 1.0 * sum(map(int, list(raw_input().translate(string.maketrans("ABCDF","43210"))))) / N

