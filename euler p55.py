def palchk(n):
    return str(n)==str(n)[::-1]

def rev(n):
    return int(str(n)[::-1])

x=0

for i in range(10000):
    n=i
    for j in range(50):
        n+=rev(n)
        if palchk(n): break
  
    if j==49: x+=1
    
print(x)