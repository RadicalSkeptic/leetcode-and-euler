from math import sqrt,floor

def oddroot(N):
    i0=floor(sqrt(N))
    d=N-i0**2
    di=d
    a=[i0]
    while True:
        i1=0
        x=0
        n=sqrt(N)
        while i1<n:
            x+=1
            i1=d*x-i0
        x-=1
        i1=d*x-i0
        a.append(x)
        num=N-i1**2
        if num==di and d==1: break
        d=num//d
        i0=i1
    return len(a)%2==0

ct=0
for N in range(2,10001):
    i=int(sqrt(N))
    if i*i==N: continue
    if oddroot(N): ct+=1
print(ct)