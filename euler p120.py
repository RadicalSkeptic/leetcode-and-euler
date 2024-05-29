ans=0
for a in range(3,1001):
    z=2
    for i in range(1,a**2,2):
        z=max(z,(2*i*a)%(a**2))
    ans+=z

print(ans)

