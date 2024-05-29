import fileinput
import math

def smolfac(a,b):
    i=min(a,b)
    if a%i==0 and b%i==0: return i
    else:    i=i//2
    while True:
        i-=1
        if a%i!=0 or b%i!=0: continue
        return i
            
    

lst=[]
for line in fileinput.input(files=r'C:\Users\sifat\Downloads\0099_base_exp.txt'):
    lst.append([int(x) for x in line.split(sep=',')])

mx=0

# for i in range(len(lst)):
#     n=smolfac(lst[mx][1],lst[i][1])
#     basemx=lst[mx][1]//n
#     basei=lst[i][1]//n                                the fuck am i doing with my life
#     if lst[mx][0]**basemx<lst[i][0]**basei:
#         mx=i
        
        
for i in range(len(lst)):
    if lst[mx][1]*math.log(lst[mx][0])<lst[i][1]*math.log(lst[i][0]):
        mx=i                                                                            #a fucking retard i am

print(mx+1)
        