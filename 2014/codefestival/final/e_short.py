N=input()
R=map(int,raw_input().split())
R=[R[0]]+[R[i] for i in range(1,N) if R[i]!=R[i-1]]
A=sum(a<b>c or a>b<c for a,b,c in zip(R[:-2],R[1:-1],R[2:]))+2
print A if A>2 else 0
