def chkpent(x):
    if (1+(1+24*x)**.5)%6==0: return True
    return False

def pent(n):
    return n*(3*n-1)/2 

for i in range(2,100000):
    for j in range(i,0,-1):
        a=pent(i)
        b=pent(j)
        if chkpent(a-b) and chkpent(a+b):
            print(a-b)
            exit