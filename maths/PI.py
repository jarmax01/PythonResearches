from math import *
import time

a = 1.0
b = 1.0/sqrt(2)
t = 1.0/4.0
p = 1.0




for i in range(25):
    aNew = (a+b)/2
    bNew = sqrt(a*b)
    tNew = t-p*(a-aNew)**2
    pNew = 2*p

    a = aNew
    b = bNew
    t = tNew
    p = pNew
    print((a + b) ** 2 / ((4 * t)))
