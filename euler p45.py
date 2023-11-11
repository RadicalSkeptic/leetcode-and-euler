import math
nh=144
while True:
    np=(1+math.sqrt(1+24*nh*(2*nh-1)))/6
    if abs(np-int(np))<.0000000001: 
        print(nh)
        break
    nh+=1
nt=2*nh-1
print(nt*(nt+1)/2)
    