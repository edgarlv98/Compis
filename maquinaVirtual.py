from quadruple import Quad
import memoria
import estructuraMemorias
import directorio_funciones as direcFunc

quadAntesFuncion = 0
llamoFuncion = False

def division(quad, i):
    left = quad.left_operand
    right = quad.right_operand

    tipoLeft = memoria.getTipoDireccion(left)
    tipoRight = memoria.getTipoDireccion(right)

    valorLeft = memoria.regresaValor(left, tipoLeft)
    valorRight = memoria.regresaValor(right, tipoRight)

    resultado = valorLeft / valorRight

    memoria.updateTemporal(resultado, quad.result, 'int')

    return i + 1
    
def mult(quad, i):
    left = quad.left_operand
    right = quad.right_operand

    tipoLeft = memoria.getTipoDireccion(left)
    tipoRight = memoria.getTipoDireccion(right)

    valorLeft = memoria.regresaValor(left, tipoLeft)
    valorRight = memoria.regresaValor(right, tipoRight)

    resultado = valorLeft * valorRight

    memoria.updateTemporal(resultado, quad.result, 'int')

    return i + 1

def resta(quad, i):
    left = quad.left_operand
    right = quad.right_operand

    tipoLeft = memoria.getTipoDireccion(left)
    tipoRight = memoria.getTipoDireccion(right)

    valorLeft = memoria.regresaValor(left, tipoLeft)
    valorRight = memoria.regresaValor(right, tipoRight)

    resultado = valorLeft - valorRight

    memoria.updateTemporal(resultado, quad.result, 'int')

    return i + 1

def suma(quad, i):
    left = quad.left_operand
    right = quad.right_operand

    tipoLeft = memoria.getTipoDireccion(left)
    tipoRight = memoria.getTipoDireccion(right)

    valorLeft = memoria.regresaValor(left, tipoLeft)
    valorRight = memoria.regresaValor(right, tipoRight)

    resultado = valorLeft + valorRight

    memoria.updateTemporal(resultado, quad.result, 'int')

    return i + 1

def mayor(quad, i):
    left = quad.left_operand
    right = quad.right_operand

    tipoLeft = memoria.getTipoDireccion(left)
    tipoRight = memoria.getTipoDireccion(right)

    valorLeft = memoria.regresaValor(left, tipoLeft)
    valorRight = memoria.regresaValor(right, tipoRight)

    resultado = valorLeft > valorRight
    
    memoria.updateTemporal(resultado, quad.result, 'bool')

    return i + 1

def menor(quad, i):
    left = quad.left_operand
    right = quad.right_operand

    tipoLeft = memoria.getTipoDireccion(left)
    tipoRight = memoria.getTipoDireccion(right)

    valorLeft = memoria.regresaValor(left, tipoLeft)
    valorRight = memoria.regresaValor(right, tipoRight)

    resultado = valorLeft < valorRight
    
    memoria.updateTemporal(resultado, quad.result, 'bool')

    return i + 1

def gotof(quad, i):
    left = quad.left_operand
    valor = memoria.regresaValor(left, 'bool')

    if(valor == 'False' or valor == False):
        return quad.result
    else:
        return i + 1

def goto(quad, i):
    return quad.result

def printt(quad, i):
    direccionVariable = quad.result
    tipoVariable = memoria.getTipoDireccion(direccionVariable)

    imprime = memoria.regresaValor(direccionVariable, tipoVariable)

    print(imprime)

    return i + 1

def inputt(quad, i):
    direccionVariable = quad.result
    tipoVariable = memoria.getTipoDireccion(direccionVariable)

    miInput = input()

    memoria.updateTemporal(miInput, direccionVariable, tipoVariable)

    return i + 1

def equal(quad, i):
    left = quad.left_operand
    tipoLeft = memoria.getTipoDireccion(left)
    valorLeft = memoria.regresaValor(left, tipoLeft)

    result = quad.result
    tipoResult = memoria.getTipoDireccion(result)

    memoria.updateTemporal(valorLeft, result, tipoResult)

    return i + 1

def doubleEqual(quad, i):
    left = quad.left_operand
    right = quad.right_operand

    tipoLeft = memoria.getTipoDireccion(left)
    tipoRight = memoria.getTipoDireccion(right)

    valorLeft = memoria.regresaValor(left, tipoLeft)
    valorRight = memoria.regresaValor(right, tipoRight)

    resultado = valorLeft == valorRight
    
    memoria.updateTemporal(resultado, quad.result, 'bool')

    return i + 1

def different(quad, i):
    left = quad.left_operand
    right = quad.right_operand

    tipoLeft = memoria.getTipoDireccion(left)
    tipoRight = memoria.getTipoDireccion(right)

    valorLeft = memoria.regresaValor(left, tipoLeft)
    valorRight = memoria.regresaValor(right, tipoRight)

    resultado = valorLeft != valorRight
    
    memoria.updateTemporal(resultado, quad.result, 'bool')

    return i + 1

def era(quad, i):
    memoria.memoria_local.append(estructuraMemorias.memoria())
    memoria.indiceMemoria += 1
    return i + 1

def gosub(quad, i):
    global quadAntesFuncion
    quadAntesFuncion = i
    global llamoFuncion
    llamoFuncion = True
    i = quad.result
    return i

def param(quad, i):
    left = quad.left_operand
    tipoLeft = memoria.getTipoDireccion(left)
    valorLeft = memoria.regresaValor(left, tipoLeft)

    result = quad.result
    tipoResult = memoria.getTipoDireccion(result)

    memoria.updateTemporal(valorLeft, result, tipoResult)

    return i + 1

def endproc(quad, i):
    if (llamoFuncion):
        i = quadAntesFuncion
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
        'input': inputt
    }
    func = switch.get(quad.operator, 'x')
    if func != 'x':
        position = func(quad, i)
        return position
    return i + 1

def inicio(quadInicial):
    i = quadInicial
    while Quad[i].operator != 'end':
        #print(Quad[i].contQua, Quad[i].operator, Quad[i].left_operand, Quad[i].right_operand, Quad[i].result)
        i = acciones(Quad[i], i)