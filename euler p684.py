
m=1000000007
def S(k):
    q=k//9
    r=k%9
    return (6*(pow(10,q,m)-1)-9*q%m+r*((3+r)*pow(10,q,m)-2)//2)%m

f0,f1=0,1
ans=0
for i in range(2,91):
    f0,f1=f1,f0+f1
    ans+=S(f1)
print(ans%m)

print(S(20))

