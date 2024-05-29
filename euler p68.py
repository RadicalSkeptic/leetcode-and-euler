n=[1,2,3,4,5,6,7,8,9,10]
n=set(n)
l=[]
for a in n:
    for b in n-set([a]):
        for c in n-set([a,b]):
            sum=a+b+c
            for d in n-set([a,b,c]):
                for e in n-set([a,b,c,d]):
                    if d+c+e!=sum: continue
                    for f in n-set([a,b,c,d,e]):
                        for g in n-set([a,b,c,d,e,f]):
                            if f+e+g!=sum: continue
                            for h in n-set([a,b,c,d,e,f,g]):
                                for i in n-set([a,b,c,d,e,f,g,h]):
                                    if h+g+i!=sum: continue
                                    for j in n-set([a,b,c,d,e,f,g,h,i]):
                                        if j+i+b!=sum: continue
                                        s=[a,b,c,d,c,e,f,e,g,h,g,i,j,i,b]
                                        l.append(s)     
ans=[]
for n in l:
    #print(n)
    low=11
    lowi=0
    for i in range(0,14,3):
        if n[i]<low: 
            lowi=i
            low=n[i]
    s=n[lowi:]+n[:lowi]
    print(s)
    for z in range(len(s)):
        s[z]=str(s[z])
    s=''.join(s)
    if len(s)==16:
        ans.append(int(s))
print(max(ans))