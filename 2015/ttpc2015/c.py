S = raw_input()
while 1:
    if "oookayama" in S:
        i = S.index("oookayama")
        j = i + len("oookayama")
        while i - 1 >= 0:
            if S[i - 1] == "o":
                i -= 1
            else:
                break
        while 1:
            if "oo" in S[i:j + 1]:
                k = S[i:j + 1].index("oo") + i
                S = S[:k] + "O" + S[k + 2:]
                j -= 1
                if "OO" in S[i:j  + 1]:
                    k = S[i:j + 1].index("OO") + i
                    S = S[:k] + "o" + S[k + 2:]
                    j -= 1
            else:
                break
    else:
        break
print S
