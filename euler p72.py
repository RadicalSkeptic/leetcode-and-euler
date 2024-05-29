
R=1000000

def fac(n):
    facs=set([n])
    for i in range(2,n**.5+1):
        if n%i==0:
            facs.add(i)
            facs.add(n/i)
    return len(facs)
ans=0
for d in range(2,R):