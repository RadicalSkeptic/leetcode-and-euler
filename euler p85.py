
M=2000000
i=1
d=float('inf')
val=lambda a,b: a*b*(a+1)*(b+1)/4
while val(i,i)<=M:
    i+=1
    z=abs(M-val(i,i))
    if z<d:
        d=z
        ans=i*i
x,y=i,i
while x>0:
    while val(x,y)<=M:
        y+=1
        z=abs(M-val(x,y))
        if z<d:
            d=z
            ans=x*y
    x-=1
print(ans)


