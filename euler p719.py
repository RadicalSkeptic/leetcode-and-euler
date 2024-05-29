
snums=0
for i in range(10**6+1):
    s=str(i**2)
    for j in range(1,2**(len(s)-1)):
        c=bin(j)[:1:-1]
        sm=0
        x=1
        first=0
        for n in c:
            if int(n):
                sm+=int(s[first:first+x])
                if sm>=i: break
                first+=x
                x=1
            else: x+=1
        sm+=int(s[first:])
        if sm==i:
            print(i,i**2)
            snums+=i**2
            break
        
print(snums)
