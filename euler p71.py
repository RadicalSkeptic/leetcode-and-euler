

def fac(n):
    for i in range(n*3//7,0,-1):
        if n%i!=0: return i

mx=0
num=0

for x in range(100,1000000):
    if 3/7>fac(x)/x>mx:
        num=fac(x)
        mx=num/x
        
print(num,mx)