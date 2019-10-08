import complex;
from numpy import linalg as LA

#multiple rendija

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
def rendija(rendija, blancos, click, v):
    n = len(v)
    m = [[0 for x in range(n)]for z in range (n)]
    bT= blancos * rendija - (rendija -1)
    
    cont=-1
    for x in range(1,rendija+1):
        m[x][0]=round(1/rendija,3)
    for x in range(bT):
        m[cont][cont]=1
        cont-=1
    ini= rendija+1
    for x in range(1,rendija+1):
        for y in range(blancos):
            m[ini+y][x]=round(1/blancos,3)
        ini+=blancos-1
    return canicas(m,v,click)    

def rendijasComplejos(n,m,v):
    for i in range(n):
        v= complex.accion(v,m)
        print(v)
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
#sistema cuantico particula en una linea

def prob(ket,pos):
    c= ket[pos][0]**2+ket[pos][1]**2
    norma=0
    for x in range(len(ket)):
        norma+=ket[x][0]**2+ket[x][1]**2
    return round(c/norma*100,2)
def amplitud (si,fi):
    bra=[]
    res=(0,0)
    for x in fi:
        bra.append((x[0],-x[1]))
    for x in range(len(si)):
        p= complex.producto(bra[x],si[x])
        res=complex.suma(res,p)
    return res

#Teoria cuantica basica
def media(m,k):
   oh=complex.accion(k,m)
   bra=[]
   for x in oh:
       bra.append((x[0],-x[1]))
   res=(0,0)
   for x in range(len(bra)):
       res = complex.suma(res,complex.producto(bra[x],k[x]))
    
   return res
def varianza(m,k):
    medi=media(m,k)
    mpr= [[ (0,0) for x in range(len(m[0]))] for y in range(len(m))]
    for x in range(len(mpr)):
        mpr[x][x]= medi
    mat= complex.matRes(m,mpr)
    mat = complex.multMat(mat,mat)
    
    vconj = []
    for x in k:
        vconj.append( (x[0],-x[1]) )

    v=[]
    for x in range(len(mat)):
        c=(0,0)
        for y in range(len(vconj)):
            c=complex.suma(c,complex.producto(vconj[y],mat[y][x] ))
        v.append(c)
    res=(0,0)
    for x in range(len(v)):
        res = complex.suma(res,complex.producto(v[x],k[x]))
    
    return res
    

def media_Varianza(m,k):
    var,medi=0,0
    if (complex.hermitian(m)):
        medi=media(m,k)
        var=varianza(m,k)
    return (medi[0],var[0])
        


def valoresPropios(mat):
    mat1=[[] for x  in range(len(mat))]
    for i in range(len(mat)):
        for j in range(len(mat[0])):
            mat1[i].append(complex(mat[i][j][0],mat[i][j][1]))
    w , v= LA.eigh(mat1)
    return [w[0],w[1]]        
    
    
       
