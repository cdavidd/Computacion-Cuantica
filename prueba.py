import complex;
import simulacion;
import unittest;

class Testcomplex(unittest.TestCase):
    def testSuma(self):
        c1=(1,5)
        c2=(2,-3)
        r=complex.suma(c1,c2)
        res=(3,2)
        self.assertEqual(r,res)
    def testProducto(self):
        c1=(1,4)
        c2=(5,1)
        r=complex.producto(c1,c2)
        res=(1,21)
        self.assertEqual(r,res)
    def testResta(self):
        c1=(1,5)
        c2=(2,-3)
        r=complex.resta(c1,c2)
        res=(-1,8)
        self.assertEqual(r,res)
    def testDivision(self):
        c1=(3,2)
        c2=(-1,2)
        r=complex.division(c1,c2)
        res=(1/5,-8/5)
        self.assertEqual(r,res)
    def testModulo(self):
        c1=(1,-3)
        r=complex.modulo(c1[0],c1[1])
        res=(c1[0]**2+c1[1]**2)**(1/2)
        self.assertEqual(r,res)
    def testConjugado(self):
        c1=(4,2)
        r=complex.conjugado(c1[0],c1[1])
        res=(4,-2)
        self.assertEqual(r,res)
    def testPolarCart(self):
        r=complex.polar_cartesiano(13.0, 22.619864948040426)
        res=(12,5)
        self.assertEqual(r,res)
    def testCartPolar(self):
        r=complex.cartesiano_polar(12,5)
        res=(13.0, 22.619864948040426)
        self.assertEqual(r,res)
    def testFase(self):
        r=complex.fase(1,-1)
        res=-0.7853981633974483
        self.assertEqual(r,res)
    def testVecSuma(self):
        v1=[(0,9),(78,65),(-99,5)]
        v2=[(10,9),(8,60),(99,-1)]
        suma= [(10,18),(86,125),(0,4)]
        res=complex.vecSuma(v1,v2)
        self.assertEqual(suma,res)
    def testVecInv(self):
        v=[(0,9),(78,65),(-99,5)]
        r=[(-0,-9),(-78,-65),(99,-5)]
        res=complex.vecInv(v)
        self.assertEqual(r,res)
    def testVecMulEsc(self):
        v=[(0,9),(3,2),(1,5)]
        n=10
        r=[(0,90),(30,20),(10,50)]
        res=complex.vecMulEsc(n,v)
        self.assertEqual(r,res)
    def testMatSuma(self):
        m1=[[(1,5),(10,2)],[(-3,5),(4,8)]]
        m2=[[(1,5),(2,3)],[(0,1),(4,8)]]
        r=[[(2,10),(12,5)],[(-3,6),(8,16)]]
        res=complex.matSuma(m1,m2)
        self.assertEqual(r,res)
    def testMatInv(self):
        m1=[[(1,5),(10,2)],[(-3,5),(4,8)]]
        r=[[(-1,-5),(-10,-2)],[(3,-5),(-4,-8)]]
        res=complex.matInv(m1)
        self.assertEqual(r,res)
    def testMatMulEsc(self):
        m1=[[(1,5),(10,2)],[(-3,5),(4,8)]]
        n=10
        r=[[(10,50),(100,20)],[(-30,50),(40,80)]]
        res= complex.matMulEsc(n,m1)
        self.assertEqual(r,res)
    def testMatTras(self):
        m1=[[(1,5),(10,2)],[(-3,5),(4,8)]]
        r=[[(1,5),(-3,5)],[(10,2),(4,8)]]
        res=complex.matTras(m1)
        self.assertEqual(r,res)
    def testMatCon(self):
        m=[[(1,5),(-3,5)],[(10,2),(4,8)]]
        r=[[(1,-5),(-3,-5)],[(10,-2),(4,-8)]]
        res= complex.matCon(m)
        self.assertEqual(r,res)
    def testMatAdj(self):
        m=[[(1,5),(-3,5)],[(10,2),(4,8)]]
        r=[[(1,-5),(10,-2)],[(-3,-5),(4,-8)]]
        res= complex.matAdj(m)
        self.assertEqual(r,res)
    def testAccion(self):
        v=[(0,9),(3,2),(1,5)]
        m=[[(1,5),(-3,5)],[(10,2),(4,8)]]
        r=[(-64, 18), (-22, 122)]
        res=complex.accion(v,m)
        self.assertEqual(r,res)
    def testNormaMat(self):
        m=[[(3,0),(5,0)],[(2,0),(3,0)]]
        r=(47**(1/2),0)
        res=complex.normaMat(m)
        self.assertEqual(r,res)
    def testDistMat(self):
        m1=[[(3,0),(5,0)],[(2,0),(3,0)]]
        m2 = [[(0,0),(1,0)],[(-1,0),(0,0)]]
        r=(6.557438524302, 0.0)
        res=complex.distMat(m1,m2)
        self.assertEqual(r,res)
    def testUnitaria(self):
        m = [[(0,0),(1,0)],[(-1,0),(0,0)]]
        res=complex.unitaria(m)
        self.assertTrue(res)
    def testHermitian(self):
        m = [[(7,0),(6,5)],[(6,-5),(-3,0)]]
        her=complex.hermitian(m)
        self.assertTrue(her)
    def testProductoTensor(self):
        m1=[[(1,0),(2,0)],[(0,0),(1,0)]]
        m2=[[(3,0),(2,0)],[(-1,0),(0,0)]]
        r= [[(3, 0), (2, 0), (6, 0), (4, 0)], [(-1, 0), (0, 0), (-2, 0), (0, 0)], [(0, 0), (0, 0), (3, 0), (2, 0)], [(0, 0), (0, 0), (-1, 0), (0, 0)]]
        res=complex.productoTensor(m1,m2)
        self.assertEqual(r,res)
    #multiple rendija
    def testCanicas(self):
        m = [[0,0,0,0,0,0,0,0],[0.5,0,0,0,0,0,0,0],[0.5,0,0,0,0,0,0,0],[0,0.33,0,1,0,0,0,0],[0,0.33,0,0,1,0,0,0],[0,0.33,0.33,0,0,1,0,0],[0,0,0.33,0,0,0,1,0],[0,0,0.33,0,0,0,0,1]]
        v = [1,0,0,0,0,0,0,0]
        n=5
        r=[0.0, 0.0, 0.0, 0.165, 0.165, 0.33, 0.165, 0.165]
        res=simulacion.canicas(m,v,n)
        self.assertEqual(r,res)
    def testRendija(self):
        v=[1,0,0,0,0,0,0,0]
        r=simulacion.rendija(2,3,2,v)
        res=[0.0, 0.0, 0.0, 0.1665, 0.1665, 0.333, 0.1665, 0.1665]
        self.assertEqual(r,res)
    def testRendijasComplejos(self):
        m = [[(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0)],[(0.5,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0)],[(0.5,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0)],[(0,0),(0.33,0),(0,0),(1,0),(0,0),(0,0),(0,0),(0,0)],[(0,0),(0.33,0),(0,0),(0,0),(1,0),(0,0),(0,0),(0,0)],[(0,0),(0.33,0),(0.33,0),(0,0),(0,0),(1,0),(0,0),(0,0)],[(0,0),(0,0),(0.33,0),(0,0),(0,0),(0,0),(1,0),(0,0)],[(0,0),(0,0),(0.33,0),(0,0),(0,0),(0,0),(0,0),(1,0)]]
        v = [(1,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0)]
        r=simulacion.rendijasComplejos(2,m,v)
        res=[(0.0, 0.0), (0.0, 0.0), (0.0, 0.0), (0.165, 0.0), (0.165, 0.0), (0.33, 0.0), (0.165, 0.0), (0.165, 0.0)]
        self.assertEqual(r,res)
    #sistema cuantico particula en una linea
    def testProb(self):
        ket=[(2,1),(-1,2),(0,1),(1,0),(3,-1),(2,0),(0,-2),(-2,1),(1,-3),(0,-1)]
        pos=7
        r= simulacion.prob(ket,pos)
        res=10.87
        self.assertEqual(r,res)
    def testAmplitud(self):
        si=[(2,1),(-1,2),(0,1),(1,0),(3,-1),(2,0),(0,-2),(-2,1),(1,-3),(0,-1)]
        fi=[(-1,-4),(2,-3),(-7,6),(-1,1),(-5,-3),(5,0),(5,8),(4,-4),(8,-7),(2,-7)]
        r= simulacion.amplitud(si,fi)
        res=(-3, -19)
        self.assertEqual(r,res)
    #Teoria cuantica basica
    def testMediaVarianza(self):
        m=[[(1,0),(0,-1)],[(0,1),(2,0)]]
        k=[(  (2**(1/2))/2 ,0 ),(  0,  (2**(1/2))/2  )]
        r=simulacion.media_Varianza(m,k)
        res=(2.5000000000000004, 0.25)
        self.assertEqual(r,res)
        
    
if __name__ == "__main__":
    unittest.main()
