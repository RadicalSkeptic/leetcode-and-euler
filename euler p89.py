
r={'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
giv=[]

for num in open(r"D:\sifat\Downloads\0089_roman.txt"):
    val,i=0,0
    num=num[:-1]
    while i<len(num):
        if i==len(num)-1:
            val+=r[num[i]]
            break
        elif r[num[i]]<r[num[i+1]]:
            val+=r[num[i+1]]-r[num[i]]
            i+=2
        else: val+=r[num[i]];i+=1
    
    giv.append((val,len(num)))

zz=[0,1,2,3,2,1,2,3,4,2]
z4=[0,1,2,3,4]
def rom(x):
    n=1
    ans=0
    while x>0:
        d=x%10
        if n<4:
            ans+=zz[d]
        else:ans+=z4[d]
        x//=10
        n+=1
    return ans

print(rom(3332))
ans=0
for num,n in giv:
    print(num,n)
    ans+=n-rom(num)
print(ans)

