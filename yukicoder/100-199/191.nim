import strutils, sequtils, algorithm, math

var
    n = readLine(stdin).parseInt
    c = readLine(stdin).split().map(parseInt)
    s = c.sum
    ans = 0

for i in 0..(n - 1):
    if 10 * c[i] <= s: ans += 30

echo($ans)
