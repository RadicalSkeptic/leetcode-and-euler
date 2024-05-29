
from itertools import product

peter={}
pt=4**9

collin={}
ct=6**6

for a in list(product(range(1,5),repeat=9)):
    n=sum(a)
    if n in peter:
        peter[n]+=1
    else:peter[n]=1

for a in list(product(range(1,7),repeat=6)):
    n=sum(a)
    if n in collin:
        collin[n]+=1
    else:collin[n]=1
    
for a in peter:
    peter[a]/=pt

for a in collin:
    collin[a]/=ct

ans=0
for a in peter:
    for b in collin:
        if a>b:
            ans+=(peter[a]*collin[b])

print(ans)