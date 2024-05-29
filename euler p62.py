def perm(a):
    return ''.join(sorted(str(a)))


mn=10

for i in range(mn,10000000):
    x=perm(i**3)
    for j in range(i-1,mn-1,-1):
        if x==perm(j**3):
            for k in range(j-1,mn-2,-1):
                if x==perm(k**3):
                    for l in range(k-1,mn-3,-1):
                        if x==perm(l**3):
                            for m in range(l-1,mn-4,-1):
                                if x==perm(m**3):
                                    print(i,j,k,l,m)
                              