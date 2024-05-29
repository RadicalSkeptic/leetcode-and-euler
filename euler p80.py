from decimal import *

getcontext().prec=103
ans=0
for n in range(1,101):
    if (n**.5)%1==0:continue
    z=Decimal(n)**Decimal('.5')
    ff=str(int(z*10**103))
    for a in ff[:100]:
        ans+=int(a)

print(ans)