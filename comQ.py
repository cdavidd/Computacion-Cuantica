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
def division():
    #4
    None
def modulo(real,imaginario):
    #5
    c= (real**2 + imaginario**2)**(1/2)
    return c
    
def conjugado(real,imaginario):
    #6
    c=(real,-imaginario)
    return c
def polar_cartesiano():
    #7
    None
def fase(real,imaginario):
    #8
    c = math.atan2(imaginario,real)
    return c

