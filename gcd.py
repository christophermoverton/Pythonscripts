def gcd(p, q):
    if (q == 0):
        return p
    else:
        return gcd(q, p % q)

def gcd2(p, q):
    cset = []
    gval = gcd(p,q)
    p1 = p
    q1 = q
    while q1 != 0:
        a = [p1,p1/q1,q1,p1%q1]
        cset.append(a)
        q2 = q1
        q1 = p1 % q1
        p1 = q2
        print(q1)
    return [gval, cset]



def revgcd(cset):
    cset.reverse()
    c = 0
    if len(cset) > 1:
        coeff = cset[1]
    print(coeff)
    solu = [1, coeff[0],-1*coeff[1],coeff[2]]
    for coeff in cset:
        if c == 0:
            c+=1
            continue
        if c == 1:
            c+=1
            continue
##        if c == len(cset)-1:
##            continue
        a = [1, coeff[0],-1*coeff[1],coeff[2], coeff[3]]
        if a[4] == solu[1]:
            solu = [a[0]*solu[0], a[1], a[2]*solu[0],
                    a[3], solu[2],solu[3]]
        elif a[4] == solu[3]:
            solu = [a[0]*solu[2], a[1], a[2]*solu[2],
                    a[3], solu[0],solu[1]]
        if len(solu) == 6:
            if solu[1] == solu[3]:
                solu = [solu[0] + solu[2], solu[1], solu[2],solu[3]]
            elif solu[1] == solu[5]:
                solu = [solu[0] + solu[4], solu[1], solu[2],solu[3]]
            elif solu[3] == solu[5]:
                solu = [solu[0],solu[1], solu[2] + solu[4], solu[3]]
        c += 1
    return solu

