from numpy.polynomial import polynomial



ans=0
p=polynomial.polyfit
xp=[]
yp=[]
for x in range(1,11):
    y=(1+x**11)/(1+x)
    #y=x**3
    xp.append(x)
    yp.append(y)
    pol=p(xp,yp,x-1)
    for i in range(len(pol)):
        ans+=pol[i]*(x+1)**i
print(ans)