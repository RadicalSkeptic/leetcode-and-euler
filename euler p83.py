import heapq as hq
import matplotlib.pyplot as plt

matrix=[]
for s in open(r"D:\sifat\Downloads\0083_matrix.txt"):
    matrix.append([int(x) for x in s.split(',')])

grid=[[float('inf') for i in range(80)] for j in range(80)]
grid[0][0]=matrix[0][0]

visited=set()
next=[]
hq.heappush(next,(matrix[0][0],0,0))
plt.ion()
while True:
    x=[]
    y=[]
    nx=hq.heappop(next)
    if (nx[1],nx[2]) in visited:continue
    neib=[(nx[1]+1,nx[2]),(nx[1]-1,nx[2]),(nx[1],nx[2]+1),(nx[1],nx[2]-1)]
    for n in neib:
        if n in visited:continue
        if n[0]<0 or n[0]>79 or n[1]<0 or n[1]>79:continue
        grid[n[0]][n[1]]=min(grid[n[0]][n[1]],nx[0]+matrix[n[0]][n[1]])
        hq.heappush(next,(grid[n[0]][n[1]],n[0],n[1]))
        x.append(n[0])
        y.append(n[1])
    plt.gca().cla()
    plt.scatter(x,y)
    plt.axis([0,80,0,80])
    plt.draw()
    plt.pause(0.001)
    visited.add((nx[1],nx[2]))
    if grid[79][79]!=float('inf'):break
print(grid[79][79])
plt.show()

