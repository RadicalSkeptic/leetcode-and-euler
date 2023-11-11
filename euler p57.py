n=5
d=2
x=0
for i in range(1000):
    n,d=2*n+d,n

    if len(str(n-d))>len(str(d)): x+=1
    
print(x)

