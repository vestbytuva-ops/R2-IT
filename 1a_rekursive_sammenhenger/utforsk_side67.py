import math as ma

s = 0
n = 5

for i in range(1,n+1):
    s = s+1/ma.factorial(i)
    print(s)
    