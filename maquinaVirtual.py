from quadruple import Quad
import memoria

def division(quad, i):
    left = quad.left_operand
    right = quad.right_operand

    tipoLeft = memoria.getTipoDireccion(left)
    tipoRight = memoria.getTipoDireccion(right)

    valorLeft = memoria.regresaValor(left, tipoLeft)
    valorRight = memoria.regresaValor(right, tipoRight)

    resultado = valorLeft / valorRight

    memoria.updateTemporal(resultado, quad.result, 'int')
    
def mult(quad, i):
    left = quad.left_operand
    right = quad.right_operand

    tipoLeft = memoria.getTipoDireccion(left)
    tipoRight = memoria.getTipoDireccion(right)

    valorLeft = memoria.regresaValor(left, tipoLeft)
    valorRight = memoria.regresaValor(right, tipoRight)

    resultado = valorLeft * valorRight

    memoria.updateTemporal(resultado, quad.result, 'int')

def resta(quad, i):
    left = quad.left_operand
    right = quad.right_operand

    tipoLeft = memoria.getTipoDireccion(left)
    tipoRight = memoria.getTipoDireccion(right)

    valorLeft = memoria.regresaValor(left, tipoLeft)
    valorRight = memoria.regresaValor(right, tipoRight)

    resultado = valorLeft - valorRight

    memoria.updateTemporal(resultado, quad.result, 'int')

def suma(quad, i):
    left = quad.left_operand
    right = quad.right_operand

    tipoLeft = memoria.getTipoDireccion(left)
    tipoRight = memoria.getTipoDireccion(right)

    valorLeft = memoria.regresaValor(left, tipoLeft)
    valorRight = memoria.regresaValor(right, tipoRight)

    resultado = valorLeft + valorRight

    memoria.updateTemporal(resultado, quad.result, 'int')

#def gotof(quad, i):
#    print("GOTOFFFFFFFFFF")
#
#def goto(quad, i):
#    print("GOTOOOOOOOOO")

def printt(quad, i):
    direccionVariable = quad.result
    tipoVariable = memoria.getTipoDireccion(direccionVariable)

    imprime = memoria.regresaValor(direccionVariable, tipoVariable)

    print(imprime)

def era(quad, i):
    print("ERAAAAAAAAAAA")

def gosub(quad, i):
    print("GOSUUUUUUUB")

def param(quad, i):
    print("PARAAAAAAM")

#def endproc(quad, i):
#    print("ENDPROOOOOOOC")

def acciones(quad, i):

    switch = {
        '+': suma,
        '-': resta,
        '*': mult,
        '/': division,

        #'gotof': gotof,
        #'goto': goto,

        'era': era,
        'gosub': gosub,
        'param': param,
        #'endproc': endproc,

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
        #print(Quad[i].contQua, Quad[i].operator, Quad[i].left_operand, Quad[i].right_operand, Quad[i].result)
        i = acciones(Quad[i], i)