import math
import collections

n=1000000
primes=[True]*(n+1)

p = 2
while (p * p <= n): 
    if (primes[p] == True): 
        for i in range(p * p, n+1, p): 
            primes[i] = False
    p += 1


def is_prime(x):
	if x <= 1:
		return False
	elif x <= 3:
		return True
	elif x % 2 == 0:
		return False
	else:
		for i in range(3, int(math.sqrt(x)) + 1, 2):
			if x % i == 0:
				return False
		return True

fil=[]
for p in range(1001,n+1,2):
    if primes[p] and len(str(p))-len(set(str(p)))>=2:
        fil.append(str(p))


s = "helloworld"
for p in fil:
    c=collections.Counter(p).most_common(1)[0][0]
    n=0
    for i in range(0,10):
        if p.replace(c,str(i)) in fil:
            n+=1
    if n>=8:
        print(p)
        