import math
N = int(raw_input())
A = map(int,raw_input().split())
A = [i for i in A if i != 0]
print int(math.ceil(sum(A)*1.0/len(A)))
