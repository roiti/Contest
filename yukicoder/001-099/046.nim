import strutils, sequtils, algorithm, math

var
    ab = readLine(stdin).split().map(parseInt)
    ans = (ab[0] + ab[1] - 1) div ab[0]

echo($ans)