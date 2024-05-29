for i in range(1010101010,1389026623):
    c=str(i**2)
    x = ''.join([c[j] for j in range(0,len(c),2)])
    if x=='1234567890': 
        print(i)
        break
    
    