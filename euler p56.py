mx=0

def sm(n):
    n=str(n)
    x=0
    for c in n:
        x+=int(c)
    return x


for a in range(100):
    for b in range(100):
        mx=max(mx, sm(a**b))
        
print(mx)