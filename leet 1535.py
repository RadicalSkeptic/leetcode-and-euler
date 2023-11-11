
arr = [2,1,3,5,4,6,7]
k = 2

if k>len(arr): print(max(arr))

t=0
x=arr[0]
for i in range(1,len(arr)):
    if x>arr[i]:
        t+=1
    else:
        x=arr[i]
        t=1
    if t==k: 
        print(x)
        break
        
