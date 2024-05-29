

A=1504170715041707
B=4503599627370517
X=3451657199285664

# n=1
# e=float('inf')
# sum=0
# while True:
#     e1=A*n%B
#     if e>e1:
#         sum,e=sum+e1,e1
#         print(sum,e1,n)
#     n+=1
sm=1517926250410182
n=float('inf')
for e in range(1,14988102):
    if n>e*X%B:
        sm+=e
        n=e*X%B
print(sm)
# 1517926250410182 14988102



# def modInverse(A, M): 
#     m0 = M 
#     y = 0
#     x = 1

#     if (M == 1): 
#         return 0
  
#     while (A > 1): 
  
#         # q is quotient 
#         q = A // M 
  
#         t = M 
  
#         # m is remainder now, process 
#         # same as Euclid's algo 
#         M = A % M 
#         A = t 
#         t = y 
  
#         # Update x and y 
#         y = x - q * y 
#         x = t 
  
#     # Make x positive 
#     if (x < 0): 
#         x = x + m0 
  
#     return x 

# print(modInverse(A,B))

