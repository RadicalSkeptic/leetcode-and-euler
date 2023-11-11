for i in range(100000,1000000000):
    n=0
    for j in range(2,7):
        if set(str(i))!=set(str(j*i)): 
            break
        else: n+=1
    if n>=5:
        print(i)