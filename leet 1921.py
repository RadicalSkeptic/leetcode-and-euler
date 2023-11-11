
dist=[1,3,4]
speed=[1,1,1]


time = sorted([dist[i]/speed[i] for i in range(len(dist))])
for i in range(len(time)):
    if i+1>time[i]: 
        print(i)
        break
print(len(time))