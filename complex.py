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
