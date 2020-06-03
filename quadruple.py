import sys
from vars_table import simbolos
import directorio_funciones as directFunc
from sematic_cube import semantic
import memoriaPadre

#Pilas
POper = []
PilaO = []
PTypes = []
Quad = []
AVAIL = []
PJumps = []
paramCont = 0
temporales = []
auxFuncSalto = 0
PilaDim = []

indice_memoria = 0

#Clase del cuadruplo
class quadruple(object):
    def __init__(self, contQua, operator, left_operand, right_operand, result=None):
        self.contQua = contQua
        self.left_operand = left_operand
        self.right_operand = right_operand
        self.operator = operator
        self.result = result

#Funcion que hace push a un id
def pushID(id, funcion):
    size = len(simbolos)
    for i in range(size):
        if(id == simbolos[i].id and funcion == simbolos[i].funcion):
            AVAIL.append(simbolos[i].value)
            PTypes.append(simbolos[i].tipo)
            appendPilaO(simbolos[i].direccion)
            break

#Funcion que checa si una cte es float
def is_float(cte):
    try:
        return float(cte) and '.' in cte
    except ValueError:
        return False

#Funcion que hace push a una cte
def pushCTE(cte, direccion):
    isFloat = is_float(cte)
    if(isFloat):
        PTypes.append('float')
        appendPilaO(direccion)
        AVAIL.append(float(cte))
    else:
        isInt = cte.isdigit()
        if(isInt):
            PTypes.append('int')
            appendPilaO(direccion)
            AVAIL.append(int(cte))
        else:
            PTypes.append('char')
            appendPilaO(direccion)
            AVAIL.append(cte)

#Funcion que hace push a un tipo
def pushTipo(tipo):
    PTypes.append(tipo)

#Funcion que hace push a un operador
def pushPoper(operador):
    POper.append(operador)

#Funcion que crea el cuadrplo de asignacion
def createQuadAssign():
    POperSize = len(POper)
    if POperSize > 0:
        if(POper[POperSize-1] == '='):
            right_operand = popPilaO()
            right_type = PTypes.pop()
            right_value = AVAIL.pop()
            left_operand = popPilaO()
            left_type = PTypes.pop()
            operator = POper.pop()
            result_type = semantic(left_type, right_type, operator)
           
            quadr = quadruple(len(Quad), operator, right_operand, None, left_operand)
            Quad.append(quadr)
            result = right_value

#Funcion que muestralos cuadruplos
def cuadruplos():
    for i in range(len(Quad)):
        print(Quad[i].contQua, Quad[i].operator, Quad[i].left_operand, Quad[i].right_operand, Quad[i].result)

#Funcion que crea el cuadrplo de termino
def createQuadTerm():
    POperSize = len(POper)
    if(POperSize > 0):
        if(POper[POperSize-1] == '+' or POper[POperSize-1] == '-'):
            right_operand = popPilaO()
            right_type = PTypes.pop()
            AVAIL.pop()
            left_operand = popPilaO()
            left_type = PTypes.pop()
            AVAIL.pop()
            operator = POper.pop()
            result_type = semantic(left_type, right_type, operator)
            if(result_type != 'error'):
                direccion = memoriaPadre.memoria_local[0].getDirTemporal(result_type)
                memoriaPadre.memoria_local[0].updateTemporal(None, direccion, result_type)
                quadr = quadruple(len(Quad), operator, left_operand, right_operand, direccion)
                Quad.append(quadr)
                AVAIL.append(direccion)
                appendPilaO(direccion)
                PTypes.append(result_type)

#Funcion que crea el cuadrplo de factor
def createQuadFact():
    POperSize = len(POper)
    if(POperSize > 0):
        if (POper[POperSize-1] == '*' or POper[POperSize-1] == '/'):
            right_operand = popPilaO()
            right_type = PTypes.pop()
            right_value = AVAIL.pop()
            left_operand = popPilaO()
            left_type = PTypes.pop()
            left_value = AVAIL.pop()
            operator = POper.pop()
            result_type = semantic(left_type, right_type, operator)
            if(result_type != 'error'):
                direccion = memoriaPadre.memoria_local[0].getDirTemporal(result_type)
                memoriaPadre.memoria_local[0].updateTemporal(None, direccion, result_type)
                quadr = quadruple(len(Quad), operator, left_operand, right_operand, direccion)
                Quad.append(quadr)
                AVAIL.append(direccion)
                appendPilaO(direccion)
                PTypes.append(result_type)

#Funcion que crea el cuadrplo de comparacion
def createQuadComp():
    POperSize = len(POper)
    if(POper[POperSize-1] == '>' or POper[POperSize-1] == '<' or POper[POperSize-1] == '==' or POper[POperSize-1] == '!='):
        right_operand = popPilaO()
        right_type = PTypes.pop()
        right_value = AVAIL.pop()
        left_operand = popPilaO()
        left_type = PTypes.pop()
        left_value = AVAIL.pop()
        operator = POper.pop()
        result_type = semantic(left_type, right_type, operator)
        if(result_type != 'error'):
            direccion = memoriaPadre.memoria_local[0].getDirTemporal(result_type)
            memoriaPadre.memoria_local[0].updateTemporal(None, direccion, result_type)
            quadr = quadruple(len(Quad), operator, left_operand, right_operand, direccion)
            Quad.append(quadr)
            AVAIL.append(direccion)
            appendPilaO(direccion)
            PTypes.append('bool')

#Funcion que crea el cuadrplo de print
def createQuadPrint():
    POperSize = len(POper)
    if POperSize > 0:
        if (POper[POperSize-1] == 'print') or (POper[POperSize-1] == 'input'):
            right_operand = popPilaO()
            PTypes.pop()
            AVAIL.pop()
            operator = POper.pop()
            quadr = quadruple(len(Quad), operator, None, None, right_operand)
            Quad.append(quadr)

#Funcion que crea el cuadrplo de return
def createQuadReturn(funcionPadre):
    direccion = 0
    tipo = None
    for x in simbolos:
        if x.id == funcionPadre:
            direccion = x.direccion
            tipo = x.tipo
            break
    right_operand = popPilaO()
    PTypes.pop()
    AVAIL.pop()
    PTypes.append(tipo)
    appendPilaO(direccion)
    quadr = quadruple(len(Quad), 'return', direccion, None, right_operand)
    Quad.append(quadr)

#Funcion que rellena los gotof y goto
def fill(cuadruplo, salto):
    Quad[cuadruplo].result = salto

#Funcion que crea el cuadrplo de condicion
def createQuadCond():
    exp_type = PTypes.pop()
    if exp_type == "bool":
        result = popPilaO()
        quadr = quadruple(len(Quad), "gotof", result, None, None)
        Quad.append(quadr)
        PJumps.append(len(Quad) - 1)
    else:
        print("ERROR:")

#Funcion quea el actualiza el valor del salto
def updateQuadCondIFJump():
    end = PJumps.pop()
    fill(end, len(Quad))

#Funcion quea el actualiza el valor del salto en condiciones
def updateQuadCondIfElseJump():
    quadr = quadruple(len(Quad), "goto", None, None, None)
    Quad.append(quadr)
    false = PJumps.pop()
    PJumps.append(len(Quad) - 1)
    fill(false, len(Quad))

#Funion que hace push al salto
def while1():
    PJumps.append(len(Quad))

#Funcion quea el actualiza el valor del salto en gotof
def while2():
    exp_type = PTypes.pop()
    if(exp_type == 'bool'):
        result = popPilaO()
        quadr = quadruple(len(Quad), 'gotof', result, None, None)
        Quad.append(quadr)
        PJumps.append(len(Quad)-1)
    else:
        print("ERROR")

#Funcion quea el actualiza el valor del salto en goto
def while3():
    final = PJumps.pop()
    regresa = PJumps.pop()
    quadr = quadruple(len(Quad), "goto", None, None, regresa)
    Quad.append(quadr)
    fill(final, len(Quad))

def loop1():
    PJumps.append(len(Quad))

def loop2():
    exp_type = PTypes.pop()
    if(exp_type == 'bool'):
        result = popPilaO()
        quadr = quadruple(len(Quad), 'gotof', result, None, None)
        Quad.append(quadr)
        PJumps.append(len(Quad)-1)
    else:
        print("ERROR")

#Muestra el tamano de la pila de operadores
def mostrarSize():
    for i in range(len(POper)):
        print(POper[i])

#Funcion que crea el cuadruplo de era
def moduloDos(direccion):
    quadr = quadruple(len(Quad), 'era', None, None, direccion)
    getFunc(direccion)
    Quad.append(quadr)

quadAuxParaParametros = []
funcName = None

paramDireccion = None
varsTableAux = []

#Funcion que crea el cuadruplo de param
def moduloTres():
    argument = popPilaO()
    AVAIL.pop()
    quadr = quadruple(len(Quad), 'param', argument, None, getDireccionParam()+ paramCont )
    Quad.append(quadr)
    sumaParametro()

#Funcion que actualiza el valor de funcName
def getFunc(direccion):
    for x in directFunc.funciones:
        if x.direccion == direccion:
            global funcName 
            funcName = x.id

#Funcion que regfresa la direccion de los parametros
def getDireccionParam():
    for x in simbolos:
        if x.funcion == funcName:
            return x.direccion

#Funcion que suma el param
def sumaParametro():
    global paramCont
    paramCont = paramCont + 1

#Funcion que crea el cuadruplo gosub
def moduloSeis(id, alcance, direccion):
    quadr = quadruple(len(Quad), 'gosub', direccion, None, alcance)
    Quad.append(quadr)
    appendPilaO(direccion)
    global paramCont
    paramCont = 0

#Funcion que crea el cuadruplo endproc
def endproc():
    quadr = quadruple(len(Quad), 'endproc', None, None, None)
    Quad.append(quadr)

#Funcion que crea el cuadruplo end
def endPrograma():
    quadr = quadruple(len(Quad), 'end', None, None, None)
    Quad.append(quadr)

#Funcion que crea el cuadruplo ver para arreglos
def verificaDim(id, funcion):
    size = len(simbolos)
    for i in range(size):
        if(simbolos[i].id == id and simbolos[i].funcion == funcion):
            dimension = simbolos[i].dimension
    
    value = AVAIL.pop()
    operand = popPilaO()
    tipo = PTypes.pop()

    quadr = quadruple(len(Quad), 'ver', operand, dimension, operand)
    Quad.append(quadr)
    aux = popPilaO()
    aux = int(aux)
    appendPilaO(aux)
    PilaDim.append(value)

#Funcion que crea el cuadruplo break
def breakk():
    quadr = quadruple(len(Quad), 'break', None, None, None)
    Quad.append(quadr)

#Funcion que crea el cuadruplo trans
def creaTrans(id1, funcionPadre):
    quadr = quadruple(len(Quad), 'transpuesta', id1, None, funcionPadre)
    Quad.append(quadr)

#Funcion que crea el cuadruplo inversa
def creaInversa(id1, funcionPadre):
    quadr = quadruple(len(Quad), 'inversa', id1, None, funcionPadre)
    Quad.append(quadr)

#Funcion que crea el cuadruplo ver para matrices
def verificaDim2(id, funcion):
    size = len(simbolos)
    for i in range(size):
        if(simbolos[i].id == id and simbolos[i].funcion == funcion):
            dimension = simbolos[i].dimension
            direccion = simbolos[i].direccion
            break

    operand1 = popPilaO()
    operand = popPilaO()
    tipo = PTypes.pop()
    quadr = quadruple(len(Quad), 'ver', direccion , dimension, (operand, operand1))
    Quad.append(quadr)
    aux = popPilaO()
    appendPilaO(aux)

#Funcion que crea el cuadruplo asignar para variables dimensionadas
def asignacionDimensionada():
    PoperSize = len(POper)
    if (PoperSize > 0):
        if(POper[PoperSize- 1] == '='):
            leftDireccion = popPilaO()
            rightDireccion = popPilaO()
            dim1 = AVAIL.pop()
            AVAIL.pop()
            dim2 = AVAIL.pop()
            operator = POper.pop()
            left = int(leftDireccion) + int(dim1)
            right = int(rightDireccion) + int(dim2)
            quadr = quadruple(len(Quad), operator, left, None, right)
            Quad.append(quadr)
            result = rightDireccion

#Funcion que crea el cuadruplo determinante
def determinante(matriz, var, funcion):
    size = len(simbolos)
    for i in range(size):
        if(simbolos[i].id == matriz and simbolos[i].funcion == funcion):
            direccion = simbolos[i].direccion
            break

    for i in range(size):
        if(simbolos[i].id == var and simbolos[i].funcion == funcion):
            direccion1 = simbolos[i].direccion
            break

    quadr = quadruple(len(Quad), 'det', direccion, None, direccion1)
    Quad.append(quadr)

#Funcion que hace pop a la pilaO
def popPilaO():
    global PilaO
    x =  PilaO.pop()
    return x

#Funcion hace append a la pilaO
def appendPilaO(value):
    global PilaO
    PilaO.append(value)