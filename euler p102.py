


def area(a,b,c):
    return abs(a[0]*(b[1]-c[1])+b[0]*(c[1]-a[1])+c[0]*(a[1]-b[1]))/2


def trichk(a,b,c):
    o=(0,0)
    return (area(a,b,o)+area(b,c,o)+area(c,a,o))==area(a,b,c)

ans=0
for line in open(r"D:\sifat\Downloads\0102_triangles.txt"):
    n=[int(s) for s in line.split(',')]
    a,b,c=(n[0],n[1]),(n[2],n[3]),(n[4],n[5])
    if trichk(a,b,c): ans+=1
print(ans)