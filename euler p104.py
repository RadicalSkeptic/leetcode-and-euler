import math

from itertools import permutations

x=[i for i in permutations(range(1,10))]

lst={0}
for r in x:
    lst.add(int(''.join([str(e) for e in r])))

def panchk(n):
    if n<123456789:return False
    n1=n%1000000000
    n2=n//10**(math.floor(math.log10(n))-8)
    if (n2 in lst) and (n1 in lst) :return True
    return False
    


f1=1
f2=1
for i in range(3,100000000):
    f1,f2=f2,f1+f2
    if panchk(f2):print(i)