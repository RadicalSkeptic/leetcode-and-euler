import math
l2=math.log10(2)

def p(L,n):
    j=0
    x=0
    z=len(str(L))-1
    while x<n:
        j+=1
        if math.floor(10**((j*l2)%1+z))==L: x+=1
    return j

print(p(12,1))
print(p(12,2))
print(p(123,45))
print(p(123,678910))

# 193060223