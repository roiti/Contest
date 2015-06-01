from itertools import combinations
N,M = map(int,raw_input().split())
lab = [map(float,raw_input().split()) for _ in range(N)]
dist = [[sum((lab[i][k]-lab[j][k])**2 for k in range(3)) for i in range(N)] for j in range(N)]
print max(sum(dist[i][j] for i,j in combinations(ele,2)) for ele in combinations(range(N),M))

