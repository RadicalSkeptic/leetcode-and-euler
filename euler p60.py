import math

N=100000000
#Returns a list of True and False indicating if a number is prime, for example list[7] = True, list[8] = False
def list_primality(n):
  result = [True] * (n + 1)
  result[0] = result[1] = False
  for i in range(int(math.sqrt(n)) + 1):
    if result[i]:
      for j in range(2 * i, len(result), i):
        result[j] = False
  return result


primetf=list_primality(N)

#Returns all the prime numbers less than or equal to n, in ascending order.

def list_primes(n):
  return [i for (i, isprime) in enumerate(primetf) if isprime]

primes=list_primes(N)


def mpc(*p):
    for i in range(len(p)-1):
        if int(str(p[i])+str(p[-1]))>N: return False
        if primetf[int(str(p[i])+str(p[-1]))]==False or primetf[int(str(p[-1])+str(p[i]))]==False:
            return False        
    return True




sums=[]
n=10000

for i in range(n-4):
    a=primes[i]
    for j in range(i+1,n-3):
        b=primes[j]
        if mpc(a,b):
            for k in range(j+1,n-2):
                c=primes[k]
                if mpc(a,b,c):
                    for l in range(k+1,n-1):
                        d=primes[l]
                        if mpc(a,b,c,d):
                            for m in range(l+1,n):
                                e=primes[m]
                                if mpc(a,b,c,d,e):
                                    sums.append(a+b+c+d+e)
                                    print(sums[-1])
                
print(min(sums))
