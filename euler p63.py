i=1
s=0
while True:
    n=1
    while len(str(n**i))<=i:
        if len(str(n**i))==i: 
            s+=1
            print(s)
        n+=1
    i+=1