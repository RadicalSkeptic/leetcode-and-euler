import math

d=12001
st=set()
n=0
for i in range(d):
    for j in range(math.ceil(i/2)):
        f=j/i
        if f>1/3:st.add(f)
print(len(st))