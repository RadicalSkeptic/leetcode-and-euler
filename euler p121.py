div=2*3*4*5*6*7*8*9*10*11*12*13*14*15*16
# div=2*3*4*5
ans=1
# for i in range(1,5):
#     ans+=i
for i in range(1,16):
    ans+=i
for i in range(1,15):
    for j in range(i+1,16):
        ans+=i*j
for i in range(1,14):
    for j in range(i+1,15):
        for k in range(j+1,16):
            ans+=i*j*k
for i in range(1,13):
    for j in range(i+1,14):
        for k in range(j+1,15):
            for l in range(k+1,16): 
                ans+=i*j*k*l
for i in range(1,12):
    for j in range(i+1,13):
        for k in range(j+1,14):
            for l in range(k+1,15): 
                for m in range(l+1,16):
                    ans+=i*j*k*l*m
for i in range(1,11):
    for j in range(i+1,12):
        for k in range(j+1,13):
            for l in range(k+1,14): 
                for m in range(l+1,15):
                    for n in range(m+1,16):
                        ans+=i*j*k*l*m*n
for i in range(1,10):
    for j in range(i+1,11):
        for k in range(j+1,12):
            for l in range(k+1,13): 
                for m in range(l+1,14):
                    for n in range(m+1,15):
                        for o in range(n+1,16):
                            ans+=i*j*k*l*m*n*o
print(ans,div)
print(div/ans)