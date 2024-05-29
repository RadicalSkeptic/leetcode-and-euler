
def prime_factors(n):
    factors = []
    d = 2
    while n > 1:
        while n % d == 0:
            factors.append(d)
            n /= d
        d = d + 1
        if d*d > n:
            if n > 1: 
                factors.append(n)
            break
    return set(factors)

def phi(n):
    ph=1
    for i in prime_factors(n):
        ph*=1-1/i
    return n*ph

m=0
for n in range(2,1000001):
    x=n/phi(n)
    if m<x:
        m=x
        a=n
print(a)
