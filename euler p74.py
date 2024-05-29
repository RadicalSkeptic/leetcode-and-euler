
f={0:1}
z=1
for i in range(1,10):
    z*=i
    f[i]=z

for i in range(10,10000000):
    z=str(i)
    f[i]=f[int(z[:-1])]+f[int(z[-1])]

ans=0
for i in range(1000000):
    d=set([])
    num=i
    while num not in d:
        d.add(num)
        num=f[num]
    if len(d)==60:ans+=1
print(ans)
    

    


