A, B, C, D = map(int, raw_input().split())  
print max(0, min(B, D) - max(A, C))
