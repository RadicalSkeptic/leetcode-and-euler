

import numba as nb

@nb.njit('List(int64)(int64)')
def get_prime_divisors(n):
    divisors = []
    while n % 2 == 0:
        divisors.append(2)
        n //= 2
    while n % 3 == 0:
        divisors.append(3)
        n //= 3
    i = 5
    while i*i <= n:
        for k in (i, i+2):
            while n % k == 0:
                divisors.append(k)
                n //= k
        i += 6
    if n > 1:
        divisors.append(n)
    return divisors

@nb.njit('List(int64)(int64)')
def get_divisors(n):
    divisors = []
    if n == 1:
        divisors.append(1)
    elif n > 1:
        prime_factors = get_prime_divisors(n)
        divisors = [1]
        last_prime = 0
        factor = 0
        slice_len = 0
        # Find all the products that are divisors of n
        for prime in prime_factors:
            if last_prime != prime:
                slice_len = len(divisors)
                factor = prime
            else:
                factor *= prime
            for i in range(slice_len):
                divisors.append(divisors[i] * factor)
            last_prime = prime
        divisors.sort()
    return divisors[:-1]

ans=0
skip=set()
ln=0
for i in range(2,1000000):
    chain={}
    n=1
    fac=i
    ex=0
    while True:
        if fac in chain:break
        elif fac in skip or fac>1000000:
            ex=1
            break
        chain[fac]=n
        skip.add(fac)
        n+=1
        fac=sum(get_divisors(fac))
    if ex==0:
        length=n-chain[fac]
        if length>ln:
            ln=length
            lst=list(chain.keys())[chain[fac]-1:]
            ans=min(lst)
print(ans)
    
