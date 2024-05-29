import fileinput

val=[]

for line in fileinput.input(files=r"C:\Users\sifat\Downloads\0081_matrix.txt"):
    val.append([int(x) for x in line.split(',')])

n=79

for i in range(n-1,-1,-1):
    for j in range(n,i-1,-1):
        if i==j:
            val[i][j]+=min(val[i][j+1],val[i+1][j])
            continue
        if j==n: 
            val[i][j]+=val[i+1][j]
            val[j][i]+=val[j][i+1]
        
        
        else: 
            val[i][j]+=min(val[i+1][j],val[i][j+1])
            val[j][i]+=min(val[j][i+1],val[j+1][i])
print(val[0][0])