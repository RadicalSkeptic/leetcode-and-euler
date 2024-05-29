#prim's algo?
import heapq as hq
mat=[]
for s in open(r"D:\sifat\Documents\code\0107_network.txt"):
    d=[]
    for a in s.split(','):
        if a=='-' or a=='-\n':
            d.append(float('inf'))
        else:d.append(int(a))
    mat.append(d)
tot=0
ver=set([0])
edge=[]
for i in range(1,len(mat[0])):
    hq.heappush(edge,(mat[0][i],i))
while len(ver)<40:
    x=hq.heappop(edge)
    if x[1] in ver:continue
    tot+=x[0]
    ver.add(x[1])
    for i in range(40):
        hq.heappush(edge,(mat[x[1]][i],i))
toto=0
for i in range(39):
    for j in range(i+1,40):
        if mat[i][j]!=float('inf'):
            toto+=mat[i][j]
print(toto-tot)