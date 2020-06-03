from quadruple import Quad
import memoriaPadre
import memoria
import vars_table as varTable
import sys
import numpy as np

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

auxiliarBreak = 0

def gotof(quad, i):
    left = quad.left_operand
    valor = memoriaPadre.memoria_local[indexMemoria].regresaValor(left, 'bool')

    global auxiliarBreak
    auxiliarBreak = quad.result
    if(valor == 'False' or valor == False):
        return quad.result
    else:
        return i + 1

def goto(quad, i):
    return quad.result

def printt(quad, i):
    
    dimension = 0
    for x in varTable.simbolos:
        if x.direccion == quad.result:
            dimension = x.dimension
    if dimension == 0:

        direccionVariable = quad.result
        tipoVariable = memoriaPadre.memoria_local[indexMemoria].getTipoDireccion(direccionVariable)

        imprime = memoriaPadre.memoria_local[indexMemoria].regresaValor(direccionVariable, tipoVariable)

        print(imprime)    
    elif type(dimension) == int and dimension>0:
        aux = int(memoriaPadre.memoria_local[indexMemoria].getValor(direccionDelIndice, None))
        direccionVariable = quad.result
        aux = direccionVariable + int(aux)

        tipoVariable = memoriaPadre.memoria_local[indexMemoria].getTipoDireccion(aux)
        imprime = memoriaPadre.memoria_local[indexMemoria].getValor(aux, tipoVariable)

        print(imprime)
        dimension = 0
    else:
        s1 = int(memoriaPadre.memoria_local[indexMemoria].getValor(int(valoresCorchetes[0]), None))
        d2 = int(limiteMatriz[1])
        s2 = int(memoriaPadre.memoria_local[indexMemoria].getValor(int(valoresCorchetes[1]), None))
        aux = int(direccionDelIndice) + s1 * d2 + s2

        tipoVariable = memoriaPadre.memoria_local[indexMemoria].getTipoDireccion(aux)
        imprime = memoriaPadre.memoria_local[indexMemoria].getValor(aux, tipoVariable)

        print(imprime)
        dimension = 0

    return i + 1

def inputt(quad, i):
    direccionVariable = quad.result
    tipoVariable = memoriaPadre.memoria_local[indexMemoria].getTipoDireccion(direccionVariable)

    miInput = input()

    memoriaPadre.memoria_local[indexMemoria].updateTemporal(miInput, direccionVariable, tipoVariable)

    return i + 1

direccionDelIndice = 0

def equal(quad, i):

    left = quad.left_operand
    dimension = 0

    for x in varTable.simbolos:
        if x.direccion == quad.result:
            dimension = x.dimension

    tipoLeft = memoriaPadre.memoria_local[indexMemoria].getTipoDireccion(left)
    valorLeft = memoriaPadre.memoria_local[indexMemoria].regresaValor(left, tipoLeft)    
    result = quad.result
    if dimension == 0:
        
        tipoResult = memoriaPadre.memoria_local[indexMemoria].getTipoDireccion(result)

        memoriaPadre.memoria_local[indexMemoria].updateTemporal(valorLeft, result, tipoResult)
    elif dimension > 0 and type(dimension) == int:
        aux = int(memoriaPadre.memoria_local[indexMemoria].getValor(direccionDelIndice, None))
        direccionVariable = quad.result
        aux = direccionVariable + int(aux)

        tipoResult = memoriaPadre.memoria_local[indexMemoria].getTipoDireccion(result)
        memoriaPadre.memoria_local[indexMemoria].updateVariableLocal(valorLeft, aux, tipoResult)
        dimension = 0
    else :
        s1 = int(memoriaPadre.memoria_local[indexMemoria].getValor(int(valoresCorchetes[0]), None))
        d2 = int(limiteMatriz[1])
        s2 = int(memoriaPadre.memoria_local[indexMemoria].getValor(int(valoresCorchetes[1]), None))
        aux = int(direccionDelIndice) + s1 * d2 + s2

        tipoResult = memoriaPadre.memoria_local[indexMemoria].getTipoDireccion(result)
        memoriaPadre.memoria_local[indexMemoria].updateVariableLocal(valorLeft, aux, tipoResult)

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

limiteMatriz = None
valoresCorchetes = None

def breakk(quad, i):
    i = auxiliarBreak
    return i

def verifica(quad, i):
    global direccionDelIndice
    global limiteMatriz
    global valoresCorchetes

    direccionDelIndice = quad.left_operand
    miDim = quad.result
    dimOriginal = quad.right_operand

    if(type(dimOriginal) == int):
        miDim = memoriaPadre.memoria_local[indexMemoria].getValor(miDim, None)
        miDim = int(miDim)
        dimOriginal = int(dimOriginal)
        if(miDim >= dimOriginal or miDim < 0):
            print("ERROR: El indide del arreglo esta fuera de la dimension declarada")
            sys.exit()
        else:
            return i + 1
    else:
        
        limiteMatriz = quad.right_operand
        valoresCorchetes = quad.result

        dimLeft = int(memoriaPadre.memoria_local[indexMemoria].getValor(int(miDim[0]), None))
        dimRight = int(memoriaPadre.memoria_local[indexMemoria].getValor(int(miDim[1]), None))
        dimOrig = int(dimOriginal[0])
        dimOrig1 = int(dimOriginal[1])
        
        if(dimLeft > dimOrig or dimLeft < 0 or dimRight > dimOrig1 or dimRight < 0):
            print("ERROR: El indide de la matriz esta fuera de la dimension declarada")
            sys.exit()
        else:
            return i + 1

def trans(quad, i):
    trans = quad.left_operand
    funcion = quad.result
    copiaDirec = 0
    for x in varTable.simbolos:
        if trans == x.id and funcion == x.funcion:
            direccion = x.direccion
            dimensiones = x.dimension
            break
    
    copiaDirec = direccion
    r = int(dimensiones[0])
    c = int(dimensiones[1])
    matriz = []
    for a in range(0,r):
        matriz.append([])
        for j in range(0,c):
            aux = memoriaPadre.memoria_local[indexMemoria].getValor(direccion,None)
            matriz[a].append(aux) 
            direccion += 1
    
    matriz = np.array(matriz).transpose()

    for x in varTable.simbolos:
        if trans == x.id and funcion == x.funcion:
            x.dimension = (x.dimension[1], x.dimension[0])

    baseDir = copiaDirec
    for a in range(0,c):
        for j in range(0,r):
            copiaDirec = baseDir + a*r + j
            tipo = memoriaPadre.memoria_local[indexMemoria].getTipoDireccion(copiaDirec)
            memoriaPadre.memoria_local[indexMemoria].updateVariableLocal(matriz[a][j], copiaDirec, tipo)
    
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

        'return': returnN,
        'input': inputt,
        'break': breakk,
        'ver': verifica,
        'transpuesta': trans
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
        
        