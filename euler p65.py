

lst=[2]
for i in range(1,100//3+1):
    lst.append(1)
    lst.append(2*i)
    lst.append(1)
print(len(lst))
num=1
den=lst.pop(-1)
while lst:
    num,den=den,lst.pop(-1)*den+num
print(num,den)
print(sum([int(x) for x in str(num)]),sum([int(x) for x in str(den)]))
