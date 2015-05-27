N=input()
print abs(sum((-1)**(x%2) for x in map(int,raw_input().split())))