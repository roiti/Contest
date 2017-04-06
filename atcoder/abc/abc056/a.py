# -*- coding: utf-8 -*-
dic = {"H":1, "D":-1}
a, b = raw_input().split()
print "H" if dic[a]*dic[b] > 0 else "D"
