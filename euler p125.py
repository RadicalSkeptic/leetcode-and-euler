

N=10**8
pal={}

def palchk(n):
    if n in pal:return pal[n]
    if len(n)==1:pal[n]=True;return True
    if len(n)==2:
        if n[0]==n[1]:
            pal[n]=True
            return True
        else:
            pal[n]=False
            return False
    pal[n]=(n[0]==n[-1] and palchk(n[1:len(n)-1]))
    return pal[n]

ans=set()
ansval=0

mul={0:0,1:1}
val=1
for i in range(2,int(N**.5)):
    val+=i**2
    mul[i]=val



for i in range(N):
    if i not in mul:break
    for j in range(2+i,N):
        if j not in mul:break
        x=mul[j]-mul[i]
        if x>N:break
        if palchk(str(x)):
            ansval+=x
            ans.add(x)

print(ansval)
print(sum(list(ans)))


