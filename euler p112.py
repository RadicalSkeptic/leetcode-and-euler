
tar=.99


def bchk(n):
    if n<=100:return False
    n=str(n)
    for i in range(1,len(n)):
        if n[i-1]==n[i]:continue
        if n[i-1]>n[i]:
            for j in range(i+1,len(n)):
                if n[j]>n[j-1]:return True
        else:
            for j in range(i+1,len(n)):
                if n[j]<n[j-1]:return True
            
    return False

n=2
t=1
b=0


while b/t < tar:
    if bchk(n):b+=1
    n+=1
    t+=1

print(n-1)

