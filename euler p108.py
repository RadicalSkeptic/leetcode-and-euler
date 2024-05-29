


def facnum(n):
    ans=1
    i=2
    while n>1:
        x=1
        while n%i==0:
            n/=i
            x+=1
        ans*=x
        i+=1
        if i*i>n:
            if n>1:
                ans*=2
            break
    if ans%2==0:return ans 
    return ans+1


f=0
i=49
mx=0
for i in range(100,600000):
    f=facnum(i*i)
    if f>mx:
        mx=f
        print(i,f)



