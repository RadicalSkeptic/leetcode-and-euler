
lst=[[0]]

for i in range(1,101):
    a=[0]
    r=0
    for j in range(1,i):
        if j>i-j:r+=lst[i-j][-1]
        else:r+=lst[i-j][j]
        a.append(r)
    a.append(r+1)
    lst.append(a)
print(lst[100][-1]-1)