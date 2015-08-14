n = int(raw_input())
h = range(1,21)
all = h+h[::-1]+h+h[::-1]+h+h[::-1]+h+h[::-1]+h+h[::-1]
print all[n-1]
