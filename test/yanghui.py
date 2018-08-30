# -*- coding: utf-8 -*-
def aaa():
    n = 1
    a = []
    while True :
        l = []
        for i in range(0, n):
            if i == 0:
                b = 1
            elif i == n - 1:
                b = 1
            else:
                b = a[i-1] + a[i]
            l.insert(i, b)
        yield l
        a = l
        n += 1


n = 0
for t in aaa():
    print(t)
    n = n + 1
    if n == 10:
        break
