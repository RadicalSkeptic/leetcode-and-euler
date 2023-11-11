fac={0:1,1:1}

for i in range(2,101):
    fac[i]=fac[i-1]*i

z=0
for n in range(23,101):
    for r in range(0,n+1):
        if fac[n]/(fac[r]*fac[n-r]) >= 1000000:
            z+=n-2*r+1
            break

print(z)