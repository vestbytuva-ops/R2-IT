from math import log
sum = 0
n=1

for i in range(1,n+1):
    sum = sum + 1/n
    print(sum-log(n))