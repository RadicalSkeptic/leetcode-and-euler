
mat=[]

for line in open(r"D:\sifat\Downloads\0082_matrix.txt"):
    mat.append([int(x) for x in line[:-1].split(',')])
# print(mat)
for b in range(1,79):
    buff=[]
    for a in range(80):
        buff.append(mat[a][b])
    for a in range(80):
        mn=float('inf')
        for i in range(80):
            if i>a:
                sm=sum(buff[a:i+1])
            elif i<=a:
                sm=sum(buff[i:a+1])
            mn=min(mn,mat[i][b-1]+sm)
        mat[a][b]=mn
ans=float('inf')
for a in range(80):
    ans=min(ans,mat[a][78]+mat[a][79])
print(ans)
