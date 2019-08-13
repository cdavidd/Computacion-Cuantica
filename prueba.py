import complex;
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
    
if __name__ == "__main__":
    unittest.main()
