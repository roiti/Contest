a = len(raw_input())-2
b = len(raw_input())-2
c = len(raw_input())-2
d = len(raw_input())-2
ans = ""
if (a >= 2*b and a >= 2*c and a >= 2*d) or (2*a <= b and 2*a <= c and 2*a <= d):
    ans += "A"
if (b >= 2*a and b >= 2*c and b >= 2*d) or (2*b <= a and 2*b <= c and 2*b <= d):
    ans += "B"
if (c >= 2*a and c >= 2*b and c >= 2*d) or (2*c <= a and 2*c <= b and 2*c <= d):
    ans += "C"
if (d >= 2*a and d >= 2*b and d >= 2*c) or (2*d <= a and 2*d <= b and 2*d <= c):
    ans += "D"
print ans if len(ans) == 1 else "C"
