
M=50000000
primes={2:1,3:2,5:3,7:4,11:5}
nn=6
for i in range(12,8000):
    z=0
    for j in range(2,int(i**.5)+1):
        if i%j==0:z=1;break
    if not z: primes[i]=nn;nn+=1

# ans=0
# for n4 in primes:
#     l4=n4**4
#     if l4>M:break
#     for n3 in primes:
#         l3=n3**3
#         if (l3+l4)>M:break
#         l2=M-n3**3-n4**4
#         n2=int(l2**.5)
#         while True:
#             if n2 in primes:
#                 if n2**2+l3+l4<=M:
#                     ans+=primes[n2]
#                     break
#             n2-=1
# print(ans)
ans=set()
for a in primes:
    a4=a**4
    if a4>M:break
    for b in primes:
        b3=b**3
        if a4+b3>M:break
        for c in primes:
            R=c**2+b3+a4
            if R<=M:
                ans.add(R)
print(len(ans))