
def odd(n):
    for d in str(n):
        if int(d)%2==0:return False
    return True

ans=0
for i in range(100000000):
    if i%10:
        ir=int(str(i)[::-1])
        if odd(i+ir):
            ans+=1 

print(ans)



# dp=set([])

# for i in range(100):
