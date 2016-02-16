I=lambda:map(int,list(raw_input()));A=I();B=I();
while A and B:
 s=A.pop(0)-B.pop(0)
 while s!=0:
  if A:s=(s+A.pop(0))%10
  else:break
print["NO","YES"][not B and sum(A)%10==0]
