
primes=[]
nonprimes=set()

for i in range(2,100000):
    if i in nonprimes:continue
    primes.append(i)
    j=i
    n=i*j
    while n<100000:
        nonprimes.add(n)
        j+=1
        n=i*j
ans=0
for p in primes:
    fac=1
    for n in range(1,101):
        if pow(10,pow(10,n),9*p)==1:
            print(n,p)
            fac=0
            break
    if fac:ans+=p
print(ans)