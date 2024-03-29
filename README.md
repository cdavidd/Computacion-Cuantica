﻿# Librería computación Cuántica

Librería realizada en python donde podrá realizar operaciones con números complejos


## Operaciones
### Numeros Complejos
1.  Suma 
	- Recibe  dos tuplas x:(real,imaginario)  y:(real,imaginario) retorna x+y: (real,imaginario)
2.  Producto 
	- Recibe  dos tuplas x:(real,imaginario)  y:(real,imaginario) retorna x*y: (real,imaginario)
3.  Resta
	 - Recibe  dos tuplas x:(real,imaginario)  y:(real,imaginario) retorna x-y: (real,imaginario)
4.  División
	- Recibe  dos tuplas x:(real,imaginario)  y:(real,imaginario) retorna x/y: (real,imaginario)
5.  Módulo
	- Recibe  un complejo (real,imaginario)  retorna el modulo: real
6.  Conjugado
	- Recibe  un complejo: (real,imaginario)  retorna el conjugado complejo: (real,imaginario)
7.  Conversión entre representaciones polar y cartesiano
	- Recibe una polar (real,teta)  retorna un complejo: (real,imaginario)
8.  Retornar la fase de un número complejo.
	- Recibe un complejo: (real,imaginario) retorna la fase: real
### Vectores
- Adición de vectores complejos.
- Inversa de vectores complejos.
- Multiplicación escalar de vectores complejos.
### Matrices
- Adición de matrices complejos.
- Inversa de matrices complejos.
- Multiplicación escalar de matrices complejas.
- Matriz transpuesta
- Matriz conjugada
- Matriz adjunta
- Función para calcular la "acción" de una matriz sobre un vector.
- Norma de matrices
- Distancia entrematrices
- Revisar si es unitaria
- Revisar si es Hermitian
- Producto tensor.
### Simulación de lo clásico a lo cuántico
- Experimento de las canicas
- Experimento de la multiple rendija
- Experimento de la multiple rendija con complejos
### Sistema cuántico de partícula en una línea
- Probabilidad de encontrarlo en una posición en particular
- Probabilidad de transitar del primer vector al segundo
### Teoría Cuántica básica
- Media y Varianza

## Como utilizarlo
#### Prerequisitos
- Debe tener Python 3, en caso de no tenerlo lo podra descargar desde su pagina principal [Python Download](https://www.python.org/downloads/)

### Uso
- descargamos la libreria
- Importamos el archivo complex a nuestro programa
```Python
import complex;
su programa
```
- Utilizamos las funciones en el mediante "complex.[funsion]" siendo [funsion] la operacion a utilizar 
```Python
Complejos
c1=(1,5)
c2=(2,-3)
r=complex.resta(c1,c2)
Vectores
v=[(0,9),(78,65),(-99,5)]
r=[(-0,-9),(-78,-65),(99,-5)]
res=complex.vecInv(v)
Matrices
m=[[(1,5),(-3,5)],[(10,2),(4,8)]]
res= complex.matAdj(m)
```
## Pruebas
- Para la ejecucion de las pruebas podremos abrir el archivo con el IDLE de python y darle **F5** o vamos a la pestaña **Run** y le seleccionamos **Run module**. 
```Python
class Testcomplex(unittest.TestCase):
    def testSuma(self):
        c1=(1,5)
        c2=(2,-3)
        r=complex.suma(c1,c2)
        res=(3,2)
        self.assertEqual(r,res)
    ...
    #mas pruebas
if __name__ == "__main__":
    unittest.main()
```
Salida de las pruebas:

![alt text](https://github.com/cdavidd/Computacion-Cuantica/blob/master/img/test.PNG)

- multiple rendija
```Python
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
```

- Sistema cuantico particula en una linea
```Python
def testProb(self):
    ket=[(2,1),(-1,2),(0,1),(1,0),(3,-1),(2,0),(0,-2),(-2,1),(1,-3),(0,-1)]
    pos=7
    r= simulacion.prob(ket,pos)
    res=10.87
    self.assertEqual(r,res)
```
- Teoria cuantica basica
```Python
def testMediaVarianza(self):
    m=[[(1,0),(0,-1)],[(0,1),(2,0)]]
    k=[(  (2**(1/2))/2 ,0 ),(  0,  (2**(1/2))/2  )]
    r=simulacion.media_Varianza(m,k)
    res=(2.5000000000000004, 0.25)
    self.assertEqual(r,res)
 ```

O desde la terminal escribimos **python *programa*** o **py *programa*** si estamos en el mismo directorio si no en la parte de *programa* ponemos el direccionamiento al programa ejmplo **Documents/carpeta/programa.py**

## Construido
- Con [Python](https://www.python.org/) .

## Autor
- Cristian David Lopez Arevalo
