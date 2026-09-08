n = 0
s = 0
a = 1
 
for i in range(6):
    s = s + a
    n = n + 1
    a = 1 / (n + 1)
    print(s)

#
from math import log as l


n = 0
s = 0
a = 1
 
for i in range(10000):
    s = s + a - l(n)
    n = n + 1
    a = 1 / (n + 1)
    print(s)
    s = s + l(n)

#

tall = 5

for i in range(6):
    print(tall)
tall = (tall-1)**2

#

from math import log, e

for i in range(6):
    