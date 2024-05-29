

mx=0

for s in open(r"D:\sifat\Documents\code\0098_words.txt"):
    lst=[x for x in s.split(',')]

for i in range(len(lst)):
    lst[i]=lst[i].strip('"')
    if len(lst[i]) > mx:
        print(lst[i],len(lst[i]))
        mx=len(lst[i])



sqr={}
n=0
i=0
while n<10**15:
    i+=1
    n=i**2
    m=str(n)
    if len(m)!=len(set(m)):continue
    if len(m) not in sqr:sqr[len(m)]=[m]
    else:sqr[len(m)]+=[m]
    
for k in sqr.keys():
    sqr[k]=set(sqr[k])
print(sqr)

y=lambda a:len(a)
lst.sort(reverse=True,key=y)



def chk(a,b,x):
    v={}
    for i in range(len(a)):
        v[a[i]]=x[i]
    r=''
    for i in b:
        r+=v[i]
    if r in sqr[len(a)]:
        return True
    return False





for i in range(len(lst)):
    n=len(lst[i])
    for j in range(i+1,len(lst)):
        m=len(lst[j])
        if m<n:break
        if sorted(lst[i])!=sorted(lst[j]):continue
        for x in sqr[m]:
            if chk(lst[i],lst[j],x) or chk(lst[j],lst[i],x):print(lst[i],lst[j],x)
            

        