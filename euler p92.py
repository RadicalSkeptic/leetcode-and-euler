ans=0
for i in range(2,10000000):
    n=i
    while True:
        x=str(n)
        n=sum([int(c)**2 for c in x])
        if n==89: 
            ans+=1
            break
        elif n==1: break
print(ans)