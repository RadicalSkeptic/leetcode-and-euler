import math

# N=1000000000
# #Returns a list of True and False indicating if a number is prime, for example list[7] = True, list[8] = False
# def list_primality(n):
#   result = [True] * (n + 1)
#   result[0] = result[1] = False
#   for i in range(int(math.sqrt(n)) + 1):
#     if result[i]:
#       for j in range(2 * i, len(result), i):
#         result[j] = False
#   return result


# primetf=list_primality(N)

# #Returns all the prime numbers less than or equal to n, in ascending order.

# def list_primes(n):
#   return [i for (i, isprime) in enumerate(primetf) if isprime]

# primes=list_primes(N)


def is_prime(x):
	if x <= 1:
		return False
	elif x <= 3:
		return True
	elif x % 2 == 0:
		return False
	else:
		for i in range(3, int(math.sqrt(x)) + 1, 2):
			if x % i == 0:
				return False
		return True


i=3
d=2
pn=1
n=1
while True:
    i+=d
    n+=1
    if is_prime(i): pn+=1
    if n%4==0: d+=2
    if pn/n<.63: break
print(d)


