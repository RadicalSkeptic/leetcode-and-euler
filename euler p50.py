from bisect import bisect_left

primes=[2]
maxnum=1000000
nums=[0]*maxnum
for i in range(3,maxnum,2):
    if nums[i]==0:
        primes.append(i)
        z=2*i
        while z<maxnum:
            nums[z]=1
            z+=i

def smpinprimes(n):
    i = bisect_left(primes, n)
    if i != len(primes) and primes[i] == n:
        return True
    return False

maxp=0
maxn=0

dp={'0_0':2}
for i in range(1,len(primes)):
    if i%1000==0: print(i)
    st0='0_'+str(i-1)
    st1='0_'+str(i)
    dp[st1]=dp[st0]+primes[i]
    m=dp[st1] 
    if m<maxnum:
        if smpinprimes(m)==True and i+1>maxn:
            maxp=m
            maxn=i+1
        
    
    for j in range(i-1):
        sub0='0_'+str(j)
        f=dp[st1]-dp[sub0] 
        if f<maxnum:
            if smpinprimes(f)==True and i-j>maxn:
                maxp=f
                maxn=i-j
            
print(maxp,maxn)
        