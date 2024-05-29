

primes=[]
nonprimes=set()

for i in range(2,1000000):
    if i in nonprimes:continue
    primes.append(i)
    j=i
    n=i*j
    while n<1000000:
        nonprimes.add(n)
        j+=1
        n=i*j

ans=0
n=0

for p in primes:
    if pow(10,pow(10,9),9*p)==1:
        ans+=p
        n+=1
        print(n,p)
    if n==40:break
print(ans)