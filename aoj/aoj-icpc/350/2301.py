K,R,L = map(int,raw_input().split())
P = float(raw_input())
E = float(raw_input())
T = float(raw_input())

def rec(r,l,k):
    h = (r+l)/2.0
    if k == 0:
        return 1.0 if T-E <= h <= T+E else 0.0
    if T-E <= r and l <= T+E: return 1.0
    if T+E <= r or l <= T-E: return 0.0

    if h >= T:
        return (1-P)*rec(r,h,k-1)+P*rec(h,l,k-1)
    else:
        return (1-P)*rec(h,l,k-1)+P*rec(r,h,k-1)

print "%.10f"%rec(R,L,K)

