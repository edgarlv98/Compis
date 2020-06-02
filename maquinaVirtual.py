from quadruple import Quad
import memoriaPadre
import memoria
import vars_table as varTable
import sys

indexMemoria = 0
indexAntesdeFuncion = 0
esMain = True

def division(quad, i):
    left = quad.left_operand
    right = quad.right_operand

    tipoLeft = memoriaPadre.memoria_local[indexMemoria].getTipoDireccion(left)
    tipoRight = memoriaPadre.memoria_local[indexMemoria].getTipoDireccion(right)

    valorLeft = memoriaPadre.memoria_local[indexMemoria].regresaValor(left, tipoLeft)
    valorRight = memoriaPadre.memoria_local[indexMemoria].regresaValor(right, tipoRight)

    resultado = valorLeft / valorRight

    memoriaPadre.memoria_local[indexMemoria].updateTemporal(resultado, quad.result, 'int')

    return i + 1
    
def mult(quad, i):
    left = quad.left_operand
    right = quad.right_operand

    tipoLeft = memoriaPadre.memoria_local[indexMemoria].getTipoDireccion(left)
    tipoRight = memoriaPadre.memoria_local[indexMemoria].getTipoDireccion(right)

    valorLeft = memoriaPadre.memoria_local[indexMemoria].regresaValor(left, tipoLeft)
    valorRight = memoriaPadre.memoria_local[indexMemoria].regresaValor(right, tipoRight)

    resultado = valorLeft * valorRight

    memoriaPadre.memoria_local[indexMemoria].updateTemporal(resultado, quad.result, 'int')

    return i + 1

def resta(quad, i):
    left = quad.left_operand
    right = quad.right_operand

    tipoLeft = memoriaPadre.memoria_local[indexMemoria].getTipoDireccion(left)
    tipoRight = memoriaPadre.memoria_local[indexMemoria].getTipoDireccion(right)

    valorLeft = memoriaPadre.memoria_local[indexMemoria].regresaValor(left, tipoLeft)
    valorRight = memoriaPadre.memoria_local[indexMemoria].regresaValor(right, tipoRight)

    resultado = valorLeft - valorRight

    memoriaPadre.memoria_local[indexMemoria].updateTemporal(resultado, quad.result, 'int')

    return i + 1

def suma(quad, i):
    left = quad.left_operand
    right = quad.right_operand

    tipoLeft = memoriaPadre.memoria_local[indexMemoria].getTipoDireccion(left)
    tipoRight = memoriaPadre.memoria_local[indexMemoria].getTipoDireccion(right)

    valorLeft = memoriaPadre.memoria_local[indexMemoria].regresaValor(left, tipoLeft)
    valorRight = memoriaPadre.memoria_local[indexMemoria].regresaValor(right, tipoRight)

    resultado = valorLeft + valorRight

    memoriaPadre.memoria_local[indexMemoria].updateTemporal(resultado, quad.result, 'int')

    return i + 1

def mayor(quad, i):
    left = quad.left_operand
    right = quad.right_operand

    tipoLeft = memoriaPadre.memoria_local[indexMemoria].getTipoDireccion(left)
    tipoRight = memoriaPadre.memoria_local[indexMemoria].getTipoDireccion(right)

    valorLeft = memoriaPadre.memoria_local[indexMemoria].regresaValor(left, tipoLeft)
    valorRight = memoriaPadre.memoria_local[indexMemoria].regresaValor(right, tipoRight)

    resultado = valorLeft > valorRight
    
    memoriaPadre.memoria_local[indexMemoria].updateTemporal(resultado, quad.result, 'bool')

    return i + 1

def menor(quad, i):
    left = quad.left_operand
    right = quad.right_operand

    tipoLeft = memoriaPadre.memoria_local[indexMemoria].getTipoDireccion(left)
    tipoRight = memoriaPadre.memoria_local[indexMemoria].getTipoDireccion(right)

    valorLeft = memoriaPadre.memoria_local[indexMemoria].regresaValor(left, tipoLeft)
    valorRight = memoriaPadre.memoria_local[indexMemoria].regresaValor(right, tipoRight)

    resultado = valorLeft < valorRight
    
    memoriaPadre.memoria_local[indexMemoria].updateTemporal(resultado, quad.result, 'bool')

    return i + 1

def gotof(quad, i):
    left = quad.left_operand
    valor = memoriaPadre.memoria_local[indexMemoria].regresaValor(left, 'bool')

    if(valor == 'False' or valor == False):
        return quad.result
    else:
        return i + 1

def goto(quad, i):
    return quad.result

def printt(quad, i):
    direccionVariable = quad.result
    tipoVariable = memoriaPadre.memoria_local[indexMemoria].getTipoDireccion(direccionVariable)

    imprime = memoriaPadre.memoria_local[indexMemoria].regresaValor(direccionVariable, tipoVariable)

    print(imprime)

    return i + 1

def inputt(quad, i):
    direccionVariable = quad.result
    tipoVariable = memoriaPadre.memoria_local[indexMemoria].getTipoDireccion(direccionVariable)

    miInput = input()

    memoriaPadre.memoria_local[indexMemoria].updateTemporal(miInput, direccionVariable, tipoVariable)

    return i + 1

def equal(quad, i):
    left = quad.left_operand
    tipoLeft = memoriaPadre.memoria_local[indexMemoria].getTipoDireccion(left)
    valorLeft = memoriaPadre.memoria_local[indexMemoria].regresaValor(left, tipoLeft)

    result = quad.result
    tipoResult = memoriaPadre.memoria_local[indexMemoria].getTipoDireccion(result)

    memoriaPadre.memoria_local[indexMemoria].updateTemporal(valorLeft, result, tipoResult)

    return i + 1

def doubleEqual(quad, i):
    left = quad.left_operand
    right = quad.right_operand

    tipoLeft = memoriaPadre.memoria_local[indexMemoria].getTipoDireccion(left)
    tipoRight = memoriaPadre.memoria_local[indexMemoria].getTipoDireccion(right)

    valorLeft = memoriaPadre.memoria_local[indexMemoria].regresaValor(left, tipoLeft)
    valorRight = memoriaPadre.memoria_local[indexMemoria].regresaValor(right, tipoRight)

    resultado = valorLeft == valorRight
    
    memoriaPadre.memoria_local[indexMemoria].updateTemporal(resultado, quad.result, 'bool')

    return i + 1

def different(quad, i):
    left = quad.left_operand
    right = quad.right_operand

    tipoLeft = memoriaPadre.memoria_local[indexMemoria].getTipoDireccion(left)
    tipoRight = memoriaPadre.memoria_local[indexMemoria].getTipoDireccion(right)

    valorLeft = memoriaPadre.memoria_local[indexMemoria].regresaValor(left, tipoLeft)
    valorRight = memoriaPadre.memoria_local[indexMemoria].regresaValor(right, tipoRight)

    resultado = valorLeft != valorRight
    
    memoriaPadre.memoria_local[indexMemoria].updateTemporal(resultado, quad.result, 'bool')

    return i + 1


def era(quad, i):
    global indexMemoria
    memoriaPadre.memoria_local.append(memoria.memoria())
    indexMemoria += 1
    memoriaPadre.memoria_local[indexMemoria] = memoriaPadre.memoria_local[indexMemoria - 1]
    return i + 1

def gosub(quad, i):
    global indexAntesdeFuncion
    global esMain
    if esMain:
        indexAntesdeFuncion = i
    esMain = False
    i = quad.result
    return i

def param(quad, i):
    tipo = memoriaPadre.memoria_local[indexMemoria].getTipoDireccion(quad.left_operand)
    valorParam = memoriaPadre.memoria_local[indexMemoria].getValor(quad.left_operand, tipo)
    memoriaPadre.memoria_local[indexMemoria].updateVariableLocal(valorParam, quad.result, tipo)
    return i + 1

def endproc(quad, i):
    global indexMemoria
    global esMain
    esMain = True
    indexMemoria -= 1
    i = indexAntesdeFuncion

    return i + 1

def returnN(quad, i):
    tipo = memoriaPadre.memoria_local[indexMemoria].getTipoDireccion(quad.left_operand)
    tipo2 = memoriaPadre.memoria_local[indexMemoria].getTipoDireccion(quad.result)
    valor = memoriaPadre.memoria_local[indexMemoria].getValor(quad.result, tipo2)
    memoriaPadre.memoria_local[indexMemoria - 1].updateVariableLocal(valor, quad.left_operand, tipo)
    return i + 1

def verifica(quad, i):
    miDim = quad.left_operand
    dimOriginal = quad.right_operand

    miDim = int(miDim)
    dimOriginal = int(dimOriginal)

    if(miDim > dimOriginal or miDim < 0):
        print("ERROR: El indide de la matriz/arreglo esta fuera de la dimension declarada")
        sys.exit()
    else:
        return i + 1

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
        'param': param,
        'endproc': endproc,

        '>': mayor,
        '=': equal,
        '<': menor,
        '==': doubleEqual,
        '!=': different,

        'print': printt,
        'input': inputt,

        'return': returnN
        'input': inputt,

        'ver': verifica
    }
    func = switch.get(quad.operator, 'x')
    if func != 'x':
        position = func(quad, i)
        return position
    return i + 1

def inicio(quadrupleMain):
    i = quadrupleMain + 1
    while Quad[i].operator != 'end':
        #print(Quad[i].contQua, Quad[i].operator, Quad[i].left_operand, Quad[i].right_operand, Quad[i].result)
        i = acciones(Quad[i], i)
        
        