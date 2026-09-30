#a

n = 0
a1 = 1
k = 3
sum = 0

while sum < 1000:
    sum = sum + a1*k**n
    n = n + 1

print(n)

#b

n = 0
a1 = 300
k = 0.8
sum = 0

while sum < 1000:
    sum = sum + a1*k**n
    n = n + 1
print(n)