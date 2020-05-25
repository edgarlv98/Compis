from quadruple import Quad
import memoria

def division(quad, i):
    print("DIVISIOOOOON")
    

def mult(quad, i):
    print("MULTIPLICACION")

def resta(quad, i):
    print("RESTAAAAAAAAAAAAA")

def suma(quad, i):
    print("PLUSSSSSSSS")
def acciones(quad, i):

    switch = {
        '+': suma,
        '-': resta,
        '*': mult,
        '/': division
    }
    func = switch.get(quad.operator, 'x')
    if func != 'x':
        position = func(quad, i)
        return position
    return i + 1

def inicio():
    i = 0
    for i in range(len(Quad)):
        i = acciones(Quad[i], i)