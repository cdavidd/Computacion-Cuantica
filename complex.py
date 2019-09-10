from sys import stdin;
import math;

def suma(x,y):
    #1
    c=(x[0]+y[0],x[1]+y[1])
    return c
def producto(x,y):
    #2
    a1=x[0]*y[0]-(x[1]*y[1])
    b1=x[0]*y[1]+x[1]*y[0]
    c=(a1,b1)
    return c
def resta(x,y):
    #3
    c=(x[0]-y[0],x[1]-y[1])
    return c
def division(x,y):
    #4
    a1=producto(x,(y[0],-y[1]))
    a2=producto(y,(y[0],-y[1]))
    c= (a1[0]/a2[0],a1[1]/a2[0])
    return c
def modulo(real,imaginario):
    #5
    c= (real**2 + imaginario**2)**(1/2)
    return c
def conjugado(real,imaginario):
    #6
    c=(real,-imaginario)
    return c
def polar_cartesiano(n,teta):
    #7
    x=n*math.cos(math.radians(teta))
    y=n*math.sin(math.radians(teta))
    c=(x,y)
    return c
def cartesiano_polar(real,imaginario):
    #7.5
    n=modulo(real,imaginario)
    teta= math.degrees(math.atan2(imaginario,real))
    c=(n,teta)
    return c
def fase(real,imaginario):
    #8
    c = math.atan2(imaginario,real)
    return c

#vector-matrices
def vecSuma(v1,v2):
    #1
    res=[]
    for j in range (len(v1)):
          r=suma(v1[j],v2[j])
          res.append(r)
    return res
def vecRes(v1,v2):
    #1
    res=[]
    for j in range (len(v1)):
          r=resta(v1[j],v2[j])
          res.append(r)
    return res
def vecInv(v):
    #2
    res=[]
    for j in range (len(v)):
        r=(-v[j][0],-v[j][1])
        res.append(r)
    return res
def vecMulEsc(n,v):
    #3
    res=[]
    for j in range (len(v)):
        r=(n*v[j][0],n*v[j][1])
        res.append(r)
    return res
def matSuma(m1,m2):
    #4
    res=[]
    for j in range (len(m1)):
        re=vecSuma(m1[j],m2[j])
        res.append(re)
    return res
def matRes(m1,m2):
    res=[]
    for j in range (len(m1)):
        re=vecRes(m1[j],m2[j])
        res.append(re)
    return res
def matInv(m):
    #5
    res=[]
    for j in range(len(m)):
        r=vecInv(m[j])
        res.append(r)
    return res
def matMulEsc(n,m):
    #6
    res=[]
    for j in range(len(m)):
        r=vecMulEsc(n,m[j])
        res.append(r)
    return res
def matTras(m):
    #7
    res=[]
    for j in range(len(m[0])):
        r=[]
        for k in range(len(m)):
            r.append(m[k][j])
        res.append(r)
    return res

def matCon(m):
    #8
    res=[]
    for j in range(len(m)):
        r=[]
        for k in range(len(m[0])):
            r.append((m[j][k][0],-m[j][k][1]))
        res.append(r)
    #res=matTras(res)
    return res

def matAdj(m):
    #9
    r= matTras(m)
    res = matCon(r)
    return res

def multMat(m1,m2):
    res = [[(0,0) for x in range(len(m2[0]))] for y in range (len(m1))]
    for i in range(len(m1)):
        for j in range(len(m2[0])):
            for k in range(len(m2)):
                res[i][j] = suma(res[i][j], producto(m1[i][k],m2[k][j]))
    return res

def accion (v,m):
    #10
    res=[]
    for j in range(len(m)):
        c=(0,0)
        for k in range(len(m[0])):
            c=suma(c,producto(m[j][k],v[j]))
        res.append(c)
    return res

def normaMat(m):
    #11
    ad=matAdj(m)
    mul=multMat(ad,m)
    res=(0,0)
    for x in range(len(mul)):
        res= suma(res,mul[x][x])
    return (res[0]**(1/2),res[1]**(1/2))

def distMat(m1,m2):
    #12
    su=matRes(m1,m2)
    res=normaMat(su)
    return res

def unitaria(m):
    #13
    r = multMat( m , matAdj(m) )
    for i in range(len(r)):
        for j in range(len(r[0])):
            if (i==j and r[i][j][0]!=1 and r[i][j][0]!=1):
                return False
            elif (i!=j and r[i][j][0]!=0 and r[i][j][0]!=0):
                return False
    return True

def hermitian(m):
    #14
    adj= matAdj(m)
    return adj == m


def productoTensor(m1,m2):
    #15
    res= [[0 for x in range(len(m1[0])*len(m2[0]))] for y in range (len(m1)*len(m2))]
    for i in range(len(m1)):
        for j in range (len(m1[0])):
            for x in range(len(m2)):
                for y in range(len(m2[0])):
                    res[i*len(m2)+x][j*len(m2[0])+y]= producto(m1[i][j],m2[x][y])
    return res
