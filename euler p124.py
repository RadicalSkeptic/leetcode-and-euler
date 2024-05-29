


def rad(n1):
    n=n1
    fac=set()
    if n==1:return 1
    if n%2==0:
        fac.add(2)
        while n%2==0:n/=2
    for i in range(3,int(n1**.5)+1,2):
        if n%i==0:
            fac.add(i)
            while n%i==0:n/=i
    fac.add(n)
    ans=1
    for a in fac:
        ans*=a
    return ans

print(rad(504))
lst=[]
for i in range(1,100001):
    lst.append((rad(i),i))
lst.sort()
print(lst[9999])
