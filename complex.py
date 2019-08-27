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
    if(real<0 or imaginario < 0):
        c+=180
    return c

#vector-matrices
def vecSuma(v1,v2):
    #1
    res=[]
    for j in range (len(v1)):
          r=suma(v1[j],v2[j])
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
    res=[]
    for j in range(len(m[0])):
        r=[]
        for k in range(len(m)):
            r.append(m[k][j])
        res.append(r)
    return res
def matConj(m):
    res=[]
    for j in range(len(m)):
        r=[]
        for k in range(len(m[0])):
            r.append((m[j][k][0],-m[j][k][1]))
        res.append(r)
    return res
def matAdj(m):
    res=[]
    for j in range(len(m)):
        r=[]
        for k in range(len(m[0])):
            r.append((m[j][k][0],-m[j][k][1]))
        res.append(r)
    res=matTras(res)
    return res
def accion (v,m):
    res=[]
    for j in range(len(m)):
        c=(0,0)
        for k in range(len(m[0])):
            c=suma(c,producto(m[j][k],v[j]))
        res.append(c)
    return res
def norma(m):
    return None
