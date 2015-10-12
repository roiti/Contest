# -*- coding: utf-8 -*-
import sys,copy,math,heapq,itertools as it,fractions,re,bisect,collections as coll

dic = {"19":"nineteen", "18":"eighteen", "17":"seventeen", "16":"sixteen", "15":"fifteen", "14":"fourteen", "13":"thirteen",
       "12":"twelve", "11":"eleven", "10":"ten", "9":"nine", "8":"eight", "7":"seven",
       "6":"six" , "5":"five", "4":"four", "3":"three", "2":"two", "1":"one", "0":"zero"}
dic10 = {"9":"ninety", "8":"eighty", "7":"seventy", "6":"sixty", "5":"fifty", "4":"forty", "3":"thirty", "2":"twenty"}

s = raw_input()
if s in dic:
    print dic[s]
else:
    if s[1] != "0":
        print dic10[s[0]] + "-" + dic[s[1]]
    else:
        print dic10[s[0]]
