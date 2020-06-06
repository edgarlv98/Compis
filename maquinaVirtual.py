from quadruple import Quad
import memoriaPadre
import memoria
import vars_table as varTable
import sys
import numpy as np

indexMemoria = 0
indexAntesdeFuncion = 0
esMain = True

#Funcion que realiza la operacion de division en la maquina virtual
def division(quad, i):
    left = quad.left_operand
    right = quad.right_operand

    #obtener dimension real del op
    dimensionLeft = getDimension(left)
    dimensionRight = getDimension(right)

    #checar si es matrix del lado izq
    if type(dimensionLeft) != int:
        left = realDirMatrix()

    if type(dimensionRight) != int:
        right = realDirMatrix()

    if(dimensionLeft > 0):
        left = getDirArreglo(left)

    if(dimensionRight > 0):
        right = getDirArreglo(right)

    tipoLeft = memoriaPadre.memoria_local[indexMemoria].getTipoDireccion(left)
    tipoRight = memoriaPadre.memoria_local[indexMemoria].getTipoDireccion(right)

    valorLeft = memoriaPadre.memoria_local[indexMemoria].regresaValor(left, tipoLeft)
    valorRight = memoriaPadre.memoria_local[indexMemoria].regresaValor(right, tipoRight)

    resultado = valorLeft / valorRight

    memoriaPadre.memoria_local[indexMemoria].updateTemporal(resultado, quad.result, 'int')

    return i + 1

#Funcion que realiza la operacion de multiplicacion en la maquina virtual
def mult(quad, i):
    left = quad.left_operand
    right = quad.right_operand

    #obtener dimension real del op
    dimensionLeft = getDimension(left)
    dimensionRight = getDimension(right)

    #checar si es matrix del lado izq
    if type(dimensionLeft) != int:
        left = realDirMatrix()

    if type(dimensionRight) != int:
        right = realDirMatrix()

    if(dimensionLeft > 0 and type(dimensionLeft) == int):
        left = getDirArreglo(left)

    if(dimensionRight > 0 and type(dimensionLeft) == int):
        right = getDirArreglo(right)

    tipoLeft = memoriaPadre.memoria_local[indexMemoria].getTipoDireccion(left)
    tipoRight = memoriaPadre.memoria_local[indexMemoria].getTipoDireccion(right)

    valorLeft = memoriaPadre.memoria_local[indexMemoria].regresaValor(left, tipoLeft)
    valorRight = memoriaPadre.memoria_local[indexMemoria].regresaValor(right, tipoRight)

    resultado = valorLeft * valorRight

    memoriaPadre.memoria_local[indexMemoria].updateTemporal(resultado, quad.result, 'int')

    return i + 1

#Funcion que realiza la operacion de resta en la maquina virtual
def resta(quad, i):
    left = quad.left_operand
    right = quad.right_operand

    #obtener dimension real del op
    dimensionLeft = getDimension(left)
    dimensionRight = getDimension(right)

    #checar si es matrix del lado izq
    if type(dimensionLeft) != int:
        left = realDirMatrix()

    if type(dimensionRight) != int:
        right = realDirMatrix()

    if(dimensionLeft > 0):
        left = getDirArreglo(left)

    if(dimensionRight > 0):
        right = getDirArreglo(right)

    tipoLeft = memoriaPadre.memoria_local[indexMemoria].getTipoDireccion(left)
    tipoRight = memoriaPadre.memoria_local[indexMemoria].getTipoDireccion(right)

    valorLeft = memoriaPadre.memoria_local[indexMemoria].regresaValor(left, tipoLeft)
    valorRight = memoriaPadre.memoria_local[indexMemoria].regresaValor(right, tipoRight)

    resultado = valorLeft - valorRight

    memoriaPadre.memoria_local[indexMemoria].updateTemporal(resultado, quad.result, 'int')

    return i + 1

def realDirMatrix():
    valorCorch1 = valoresCorchetes.pop()
    direc1 = direccionDelIndice.pop()
    dim1 = limiteMatriz.pop()

    s11 = int(memoriaPadre.memoria_local[indexMemoria].getValor(int(valorCorch1[0]), None))
    d22 = int(dim1[1])
    s22 = int(memoriaPadre.memoria_local[indexMemoria].getValor(int(valorCorch1[1]), None))
    aux2 = int(direc1) + s11 * d22 + s22
    return aux2

def getDimension(dir):
    for x in varTable.simbolos:
        if x.direccion == dir:
            dimension = x.dimension
            if(dimension == 0):
                return dimension
            dimension = memoriaPadre.memoria_local[0].getValor(dimension, 'dimension')
            return dimension
    return 0

#Funcion que realiza la operacion de suma en la maquina virtual
def suma(quad, i):
    left = quad.left_operand
    right = quad.right_operand

    #obtener dimension real del op
    dimensionLeft = getDimension(left)
    dimensionRight = getDimension(right)

    #checar si es matrix del lado izq
    if type(dimensionLeft) != int:
        left = realDirMatrix()

    if type(dimensionRight) != int:
        right = realDirMatrix()

    if(dimensionLeft > 0):
        left = getDirArreglo(left)

    if(dimensionRight > 0):
        right = getDirArreglo(right)

    tipoLeft = memoriaPadre.memoria_local[indexMemoria].getTipoDireccion(left)
    tipoRight = memoriaPadre.memoria_local[indexMemoria].getTipoDireccion(right)

    valorLeft = memoriaPadre.memoria_local[indexMemoria].regresaValor(left, tipoLeft)
    valorRight = memoriaPadre.memoria_local[indexMemoria].regresaValor(right, tipoRight)

    resultado = valorLeft + valorRight

    memoriaPadre.memoria_local[indexMemoria].updateTemporal(resultado, quad.result, 'int')

    return i + 1

#Funcion que realiza la operacion de mayor que en la maquina virtual
def mayor(quad, i):
    left = quad.left_operand
    right = quad.right_operand

    #obtener dimension real del op
    dimensionLeft = getDimension(left)
    dimensionRight = getDimension(right)

    #checar si es matrix del lado izq
    if type(dimensionLeft) != int:
        left = realDirMatrix()

    if type(dimensionRight) != int:
        right = realDirMatrix()

    if(dimensionLeft > 0):
        left = getDirArreglo(left)

    if(dimensionRight > 0):
        right = getDirArreglo(right)

    tipoLeft = memoriaPadre.memoria_local[indexMemoria].getTipoDireccion(left)
    tipoRight = memoriaPadre.memoria_local[indexMemoria].getTipoDireccion(right)

    valorLeft = memoriaPadre.memoria_local[indexMemoria].regresaValor(left, tipoLeft)
    valorRight = memoriaPadre.memoria_local[indexMemoria].regresaValor(right, tipoRight)

    resultado = valorLeft > valorRight
    
    memoriaPadre.memoria_local[indexMemoria].updateTemporal(resultado, quad.result, 'bool')

    return i + 1

#Funcion que realiza la operacion de menor que en la maquina virtual
def menor(quad, i):
    left = quad.left_operand
    right = quad.right_operand
    
    #obtener dimension real del op
    dimensionLeft = getDimension(left)
    dimensionRight = getDimension(right)

    #checar si es matrix del lado izq
    if type(dimensionLeft) != int:
        left = realDirMatrix()

    if type(dimensionRight) != int:
        right = realDirMatrix()

    if(dimensionLeft > 0):
        left = getDirArreglo(left)

    if(dimensionRight > 0):
        right = getDirArreglo(right)

    tipoLeft = memoriaPadre.memoria_local[indexMemoria].getTipoDireccion(left)
    tipoRight = memoriaPadre.memoria_local[indexMemoria].getTipoDireccion(right)

    valorLeft = memoriaPadre.memoria_local[indexMemoria].regresaValor(left, tipoLeft)
    valorRight = memoriaPadre.memoria_local[indexMemoria].regresaValor(right, tipoRight)

    resultado = valorLeft < valorRight
    
    memoriaPadre.memoria_local[indexMemoria].updateTemporal(resultado, quad.result, 'bool')

    return i + 1

auxiliarBreak = 0

#Funcion que realiza el gotof en la maquina virtual
def gotof(quad, i):
    left = quad.left_operand
    valor = memoriaPadre.memoria_local[indexMemoria].regresaValor(left, 'bool')

    global auxiliarBreak
    if auxiliarBreak == 0:
        auxiliarBreak = quad.result
    
    if(valor == 'False' or valor == False):
        return quad.result
    else:
        return i + 1

#Funcion que realiza el goto en la maquina virtual
def goto(quad, i):
    global auxiliarBreak
    auxiliarBreak = 0
    return quad.result

#Funcion que realiza la operacion de print en la maquina virtual
def printt(quad, i):
    
    dimension = 0
    for x in varTable.simbolos:
        if x.direccion == quad.result:
            dimension = x.dimension

        #variable normal
    if dimension == 0:
        direccionVariable = quad.result
        tipoVariable = memoriaPadre.memoria_local[indexMemoria].getTipoDireccion(direccionVariable)
        imprime = memoriaPadre.memoria_local[indexMemoria].getValor(direccionVariable, None)

        print(imprime)
        return i + 1    

    dimension = memoriaPadre.memoria_local[0].getValor(dimension, 'dimension')
        #4rr3610
    if type(dimension) == int and dimension>0:
        aux = int(memoriaPadre.memoria_local[indexMemoria].getValor(direccionDelIndice.pop(), None))
        direccionVariable = quad.result
        aux = direccionVariable + int(aux)

        tipoVariable = memoriaPadre.memoria_local[indexMemoria].getTipoDireccion(aux)
        imprime = memoriaPadre.memoria_local[indexMemoria].getValor(aux, tipoVariable)

        print(imprime)
        dimension = 0
    else:
        valorCORCH1 = valoresCorchetes.pop()

        dim = limiteMatriz.pop()
        s1 = int(memoriaPadre.memoria_local[indexMemoria].getValor(int(valorCORCH1[0]), None))
        d2 = int(dim[1])
        s2 = int(memoriaPadre.memoria_local[indexMemoria].getValor(int(valorCORCH1[1]), None))
        aux = int(direccionDelIndice.pop()) + s1 * d2 + s2
        tipoVariable = memoriaPadre.memoria_local[indexMemoria].getTipoDireccion(aux)
        imprime = memoriaPadre.memoria_local[indexMemoria].getValor(aux, tipoVariable)

        print(imprime)
        dimension = 0

    return i + 1

#Funcion que realiza la operacion de input en la maquina virtual
def inputt(quad, i):
    direccionVariable = quad.result
    tipoVariable = memoriaPadre.memoria_local[indexMemoria].getTipoDireccion(direccionVariable)

    miInput = input()

    memoriaPadre.memoria_local[indexMemoria].updateTemporal(miInput, direccionVariable, tipoVariable)

    return i + 1

direccionDelIndice = []

#Funcion que realiza la asignacion en la maquina virtual
def equal(quad, i):

    left = quad.left_operand
    right = quad.result

    dimensionLeft = getDimension(left)
    dimensionRight = getDimension(right)

    if type(dimensionLeft) != int:
        left = realDirMatrix()

    if type(dimensionRight) != int:
        right = realDirMatrix()

    if(dimensionLeft > 0 and type(dimensionLeft) == int):
        left = getDirArreglo(left)

    if(dimensionRight > 0 and type(dimensionRight) == int):
        right = getDirArreglo(right)

    valorLeft = memoriaPadre.memoria_local[indexMemoria].getValor(left, None)
    tipo = memoriaPadre.memoria_local[indexMemoria].getTipoDireccion(left)
    memoriaPadre.memoria_local[indexMemoria].updateVariableLocal(valorLeft, right, tipo)
        
    return i + 1

def getDirArreglo(dir):
    aux = int(memoriaPadre.memoria_local[indexMemoria].getValor(direccionDelIndice.pop(), None))
    nuevaDireccion = dir + aux
    return nuevaDireccion

#Funcion que realiza la operacion de igual en la maquina virtual
def doubleEqual(quad, i):
    left = quad.left_operand
    right = quad.right_operand

    #obtener dimension real del op
    dimensionLeft = getDimension(left)
    dimensionRight = getDimension(right)

    #checar si es matrix del lado izq
    if type(dimensionLeft) != int:
        left = realDirMatrix()

    if type(dimensionRight) != int:
        right = realDirMatrix()

    if(dimensionLeft > 0 and type(dimensionLeft) == int):
        left = getDirArreglo(left)

    if(dimensionRight > 0 and type(dimensionRight) == int):
        right = getDirArreglo(right)

    tipoLeft = memoriaPadre.memoria_local[indexMemoria].getTipoDireccion(left)
    tipoRight = memoriaPadre.memoria_local[indexMemoria].getTipoDireccion(right)

    valorLeft = memoriaPadre.memoria_local[indexMemoria].regresaValor(left, tipoLeft)
    valorRight = memoriaPadre.memoria_local[indexMemoria].regresaValor(right, tipoRight)
    resultado = valorLeft == valorRight
    
    memoriaPadre.memoria_local[indexMemoria].updateTemporal(resultado, quad.result, 'bool')

    return i + 1

#Funcion que realiza la operacion de diferente en la maquina virtual
def different(quad, i):
    left = quad.left_operand
    right = quad.right_operand

    #obtener dimension real del op
    dimensionLeft = getDimension(left)
    dimensionRight = getDimension(right)

    #checar si es matrix del lado izq
    if type(dimensionLeft) != int:
        left = realDirMatrix()

    if type(dimensionRight) != int:
        right = realDirMatrix()

    if(dimensionLeft > 0):
        left = getDirArreglo(left)

    if(dimensionRight > 0):
        right = getDirArreglo(right)

    tipoLeft = memoriaPadre.memoria_local[indexMemoria].getTipoDireccion(left)
    tipoRight = memoriaPadre.memoria_local[indexMemoria].getTipoDireccion(right)

    valorLeft = memoriaPadre.memoria_local[indexMemoria].regresaValor(left, tipoLeft)
    valorRight = memoriaPadre.memoria_local[indexMemoria].regresaValor(right, tipoRight)

    resultado = valorLeft != valorRight
    
    memoriaPadre.memoria_local[indexMemoria].updateTemporal(resultado, quad.result, 'bool')

    return i + 1

#Funcion que realiza la llamada de funcion en la maquina virtual
def era(quad, i):
    global indexMemoria
    memoriaPadre.memoria_local.append(memoria.memoria())
    indexMemoria += 1
    memoriaPadre.memoria_local[indexMemoria] = memoriaPadre.memoria_local[indexMemoria - 1]
    return i + 1

#Funcion que realiza el gosub en la maquina virtual
def gosub(quad, i):
    global indexAntesdeFuncion
    global esMain
    if esMain:
        indexAntesdeFuncion = i
    esMain = False
    i = quad.result
    return i

#Funcion que realiza la operacion de los parametros en la maquina virtual
def param(quad, i):
    tipo = memoriaPadre.memoria_local[indexMemoria].getTipoDireccion(quad.left_operand)
    valorParam = memoriaPadre.memoria_local[indexMemoria].getValor(quad.left_operand, tipo)
    memoriaPadre.memoria_local[indexMemoria].updateVariableLocal(valorParam, quad.result, tipo)
    return i + 1

#Funcion que realiza el endproc de una funcion
def endproc(quad, i):
    global indexMemoria
    global esMain
    esMain = True
    indexMemoria -= 1
    i = indexAntesdeFuncion

    return i + 1

#Funcion que realiza la operacion de return en la maquina virtual
def returnN(quad, i):
    tipo = memoriaPadre.memoria_local[indexMemoria].getTipoDireccion(quad.left_operand)
    tipo2 = memoriaPadre.memoria_local[indexMemoria].getTipoDireccion(quad.result)
    valor = memoriaPadre.memoria_local[indexMemoria].getValor(quad.result, tipo2)
    memoriaPadre.memoria_local[indexMemoria - 1].updateVariableLocal(valor, quad.left_operand, tipo)
    return i + 1

limiteMatriz = []
valoresCorchetes = []

#Break en desarrollo
def breakk(quad, i):
    global auxiliarBreak
    i = auxiliarBreak
    auxiliarBreak = 0
    return i

#Funcion que verifica las dimensiones en la maquina virtual
def verifica(quad, i):
    global direccionDelIndice
    global limiteMatriz
    global valoresCorchetes

    direccionDelIndice.append(quad.left_operand)
    miDim = quad.result
    dimOriginal = memoriaPadre.memoria_local[0].getValor(quad.right_operand, 'dimension') 

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
        
        limiteMatriz.append(dimOriginal)
        valoresCorchetes.append(quad.result)

        dimLeft = int(memoriaPadre.memoria_local[indexMemoria].getValor(int(miDim[0]), None))
        dimRight = int(memoriaPadre.memoria_local[indexMemoria].getValor(int(miDim[1]), None))
        dimOrig = int(dimOriginal[0])
        dimOrig1 = int(dimOriginal[1])
        
        if(dimLeft > dimOrig or dimLeft < 0 or dimRight > dimOrig1 or dimRight < 0):
            print("ERROR: El indide de la matriz esta fuera de la dimension declarada")
            sys.exit()
        else:
            return i + 1

#Funcion que realiza la operacion de transpuesta de una matriz en la maquina virtual
def trans(quad, i):
    trans = quad.left_operand
    funcion = quad.result
    copiaDirec = 0
    for x in varTable.simbolos:
        if trans == x.id and funcion == x.funcion:
            direccion = x.direccion
            dimensiones = x.dimension
            break
    dimensiones =  memoriaPadre.memoria_local[0].getValor(dimensiones, 'dimension')
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
            memoriaPadre.memoria_local[0].updateVariableLocal((c,r),x.dimension,'dimension')

    baseDir = copiaDirec
    for a in range(0,c):
        for j in range(0,r):
            copiaDirec = baseDir + a*r + j
            tipo = memoriaPadre.memoria_local[indexMemoria].getTipoDireccion(copiaDirec)
            memoriaPadre.memoria_local[indexMemoria].updateVariableLocal(matriz[a][j], copiaDirec, tipo)

    return i + 1

#Funcion que realiza la operacion de inversa de una matriz en la maquina virtual
def inversa(quad, i):
    inv = quad.left_operand
    funcion = quad.result
    copiaDirec = 0
    for x in varTable.simbolos:
        if inv == x.id and funcion == x.funcion:
            direccion = x.direccion
            dimensiones = x.dimension
            break

    if memoriaPadre.memoria_local[0].getTipoDireccion(direccion) != 'float':
        print("Para calcular la inversa es necesario que la matriz sea de tipo float.")
        sys.exit()

    dimensiones =  memoriaPadre.memoria_local[0].getValor(dimensiones, 'dimension')
    copiaDirec = direccion
    r = int(dimensiones[0])
    c = int(dimensiones[1])

    if r != c:
        print("No es posible calcular la inversa, la matriz no es cuadrada.")
        sys.exit()

    matriz = []

    for a in range(0,r):
        matriz.append([])
        for j in range(0,c):
            aux = memoriaPadre.memoria_local[indexMemoria].getValor(direccion,None)
            matriz[a].append(aux) 
            direccion += 1

    try:
        matriz = np.linalg.inv(np.array(matriz))
    except:
        print("No es posible calcular matriz inversa, ya que es matriz singular.")
        sys.exit()

    baseDir = copiaDirec
    for a in range(0,c):
        for j in range(0,r):
            copiaDirec = baseDir + a*r + j
            tipo = memoriaPadre.memoria_local[indexMemoria].getTipoDireccion(copiaDirec)
            matriz[a][j] = round(matriz[a][j], 4)
            memoriaPadre.memoria_local[indexMemoria].updateVariableLocal(matriz[a][j], copiaDirec, tipo)
    
    return i + 1

#Funcion que realiza la operacion de determinante de una matriz en la maquina virtual
def determinante(quad, i):
    det = quad.left_operand

    for x in varTable.simbolos:
        if det == x.direccion :
            direccion = x.direccion
            dimensiones = x.dimension
            break
    dimensiones =  memoriaPadre.memoria_local[0].getValor(dimensiones, 'dimension')

    r = int(dimensiones[0])
    c = int(dimensiones[1])

    matriz = []

    for a in range(0,r):
        matriz.append([])
        for j in range(0,c):
            aux = memoriaPadre.memoria_local[indexMemoria].getValor(direccion,None)
            matriz[a].append(aux) 
            direccion += 1
    
    aux = np.linalg.det(np.array(matriz))
    aux = round(aux, 4)
    memoriaPadre.memoria_local[0].updateVariableLocal(aux, quad.result, 'float')
    
    return i + 1

#Switch de la maquina virtual
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
        'transpuesta': trans,
        'inversa': inversa,
        'det': determinante
    }
    func = switch.get(quad.operator, 'x')
    if func != 'x':
        position = func(quad, i)
        return position
    return i + 1

#Inicio de la maquina virtual
def inicio(quadrupleMain):
    i = quadrupleMain + 1
    while Quad[i].operator != 'end':
        i = acciones(Quad[i], i)
        
        