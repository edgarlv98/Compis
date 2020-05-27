from quadruple import Quad
import memoria

def division(quad, i):
    print("DIVISIOOOOON")
    
def mult(quad, i):
    print("MULTIPLICACION")

def resta(quad, i):
    print("RESTAAAAAAAAAAAAA")

def suma(quad, i):
    print("SUMAAAAAAAAA")

def gotof(quad, i):
    print("GOTOFFFFFFFFFF")

def goto(quad, i):
    print("GOTOOOOOOOOO")

def printt(quad, i):
    print("PRIIIIIIIINT")

def era(quad, i):
    print("ERAAAAAAAAAAA")

def gosub(quad, i):
    print("GOSUUUUUUUB")

def acciones(quad, i):

    switch = {
        '+': suma,
        '-': resta,
        '*': mult,
        '/': division,

        'gotof': gotof,
        'goto': goto,

        'era': era,
        'gosub': gosub,

        'print': printt
    }
    func = switch.get(quad.operator, 'x')
    if func != 'x':
        position = func(quad, i)
        return position
    return i + 1

def inicio():
    i = 0
    for i in range(len(Quad)):
        print(Quad[i].contQua, Quad[i].operator, Quad[i].left_operand, Quad[i].right_operand, Quad[i].result)
        i = acciones(Quad[i], i)