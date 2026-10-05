import math as ma

s = 0
n = 100

for i in range(n+1):
    s = s+1/ma.factorial(i)
    print(s)
