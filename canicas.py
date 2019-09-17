import complex;

def canicas(m,v,n):
    for x in range(n):
        r=[]
        for i in range(len(m)):
            cont=0
            for j in range(len(m[0])):
                cont+=m[i][j]*v[j]
            r.append(cont)
        v=r
    return v

def tensor (m1,m2):
    res= [[0 for x in range(len(m1[0])*len(m2[0]))] for y in range (len(m1)*len(m2))]
    for i in range(len(m1)):
        for j in range (len(m1[0])):
            for x in range(len(m2)):
                for y in range(len(m2[0])):
                    res[i*len(m2)+x][j*len(m2[0])+y]= m1[i][j]*m2[x][y]
    return res
def vecc(v1,v2):
    v=[]
    for x in range(len(v1)):
        for y in range(len(v2)):
            v.append(v1[x]*v2[y])
    return v

def system(m1,m2,v1,v2,n):
    m=tensor(m1,m2)
    v=vecc(v1,v2)
    for x in range(n):
        r=[]
        for i in range(len(m)):
            cont=0
            for j in range(len(m[0])):
                cont+=m[i][j]*v[j]
            r.append(cont)
        v=r
    for x in range(len(v)):
        v[x]= round(v[x]*100,2)
    return v
