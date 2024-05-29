p3=lambda n: n*(n+1)//2
p4=lambda n: n**2
p5=lambda n: n*(3*n-1)//2
p6=lambda n: n*(2*n-1)
p7=lambda n: n*(5*n-3)//2
p8=lambda n: n*(3*n-2)

def cyclic(a,b):
    return a%100 == b//100

n3=[(p3(x),'tri') for x in range(1,1000) if 999<p3(x)<10000]
n4=[(p4(x),'squ') for x in range(1,1000) if 999<p4(x)<10000]
n5=[(p5(x),'pen') for x in range(1,1000) if 999<p5(x)<10000]
n6=[(p6(x),'hex') for x in range(1,1000) if 999<p6(x)<10000]
n7=[(p7(x),'hep') for x in range(1,1000) if 999<p7(x)<10000]
n8=[(p8(x),'oct') for x in range(1,1000) if 999<p8(x)<10000]

al=n3+n4+n5+n6+n7+n8
dic={}
for a in al:
    dic[a]=[]
    for b in al:
        if a[0]!=b[0] and a[1]!=b[1] and cyclic(a[0],b[0]):
            dic[a].append(b)


for a in n8:
    for b in dic[a]:
        for c in dic[b]:
            for d in dic[c]:
                for e in dic[d]:
                    for f in dic[e]:
                        if cyclic(f[0],a[0]) and len(set([a[1],b[1],c[1],d[1],e[1],f[1]]))==6:
                            print(a[0]+b[0]+c[0]+d[0]+e[0]+f[0])
                            print(a,b,c,d,e,f)
                            exit()