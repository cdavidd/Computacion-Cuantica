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
