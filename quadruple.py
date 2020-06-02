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

def pushID(id):
    size = len(simbolos)
    for i in range(size):
        if(id == simbolos[i].id):
            AVAIL.append(simbolos[i].value)
            PTypes.append(simbolos[i].tipo)
            PilaO.append(simbolos[i].direccion)
            break

def is_float(cte):
    try:
        return float(cte) and '.' in cte
    except ValueError:
        return False

def pushCTE(cte, direccion):
    isFloat = is_float(cte)
    if(isFloat):
        PTypes.append('float')
        PilaO.append(direccion)
        AVAIL.append(float(cte))
    else:
        isInt = cte.isdigit()
        if(isInt):
            PTypes.append('int')
            PilaO.append(direccion)
            AVAIL.append(int(cte))
        else:
            PTypes.append('char')
            PilaO.append(direccion)
            AVAIL.append(cte)

def pushTipo(tipo):
    PTypes.append(tipo)

def pushPoper(operador):
    POper.append(operador)

def createQuadAssign():
    POperSize = len(POper)
    if POperSize > 0:
        if(POper[POperSize-1] == '='):
            right_operand = PilaO.pop()
            right_type = PTypes.pop()
            right_value = AVAIL.pop()
            left_operand = PilaO.pop()
            left_type = PTypes.pop()
            operator = POper.pop()
            result_type = semantic(left_type, right_type, operator)
            if(result_type != 'error'):
                quadr = quadruple(len(Quad), operator, right_operand, None, left_operand)
                Quad.append(quadr)
                result = right_value
    #else:
    #    print("ERROR")
    return result

def cuadruplos():
    for i in range(len(Quad)):
        print(Quad[i].contQua, Quad[i].operator, Quad[i].left_operand, Quad[i].right_operand, Quad[i].result)

def createQuadTerm():
    POperSize = len(POper)
    if(POperSize > 0):
        if(POper[POperSize-1] == '+' or POper[POperSize-1] == '-'):
            right_operand = PilaO.pop()
            right_type = PTypes.pop()
            right_value = AVAIL.pop()
            left_operand = PilaO.pop()
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
                PilaO.append(direccion)
                PTypes.append(result_type)
    #else:
    #    print("ERROR")

def createQuadFact():
    POperSize = len(POper)
    if(POperSize > 0):
        if (POper[POperSize-1] == '*' or POper[POperSize-1] == '/'):
            right_operand = PilaO.pop()
            right_type = PTypes.pop()
            right_value = AVAIL.pop()
            left_operand = PilaO.pop()
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
                PilaO.append(direccion)
                PTypes.append(result_type)
    #else:
    #    print("ERROR")

def createQuadComp():
    POperSize = len(POper)
    if(POper[POperSize-1] == '>' or POper[POperSize-1] == '<' or POper[POperSize-1] == '==' or POper[POperSize-1] == '!='):
        right_operand = PilaO.pop()
        right_type = PTypes.pop()
        right_value = AVAIL.pop()
        left_operand = PilaO.pop()
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
            PilaO.append(direccion)
            PTypes.append('bool')
    #else:
    #    print("ERROR")

def createQuadPrint():
    POperSize = len(POper)
    if POperSize > 0:
        if (POper[POperSize-1] == 'print') or (POper[POperSize-1] == 'input'):
            right_operand = PilaO.pop()
            PTypes.pop()
            AVAIL.pop()
            operator = POper.pop()
            quadr = quadruple(len(Quad), operator, None, None, right_operand)
            Quad.append(quadr)

def fill(cuadruplo, salto):
    Quad[cuadruplo].result = salto

def createQuadCond():
    exp_type = PTypes.pop()
    if exp_type == "bool":
        result = PilaO.pop()
        quadr = quadruple(len(Quad), "gotof", result, None, None)
        Quad.append(quadr)
        PJumps.append(len(Quad) - 1)
    else:
        print("ERROR:")

def updateQuadCondIFJump():
    end = PJumps.pop()
    fill(end, len(Quad))

def updateQuadCondIfElseJump():
    quadr = quadruple(len(Quad), "goto", None, None, None)
    Quad.append(quadr)
    false = PJumps.pop()
    PJumps.append(len(Quad) - 1)
    fill(false, len(Quad))

def while1():
    PJumps.append(len(Quad))

def while2():
    exp_type = PTypes.pop()
    if(exp_type == 'bool'):
        result = PilaO.pop()
        quadr = quadruple(len(Quad), 'gotof', result, None, None)
        Quad.append(quadr)
        PJumps.append(len(Quad)-1)
    else:
        print("ERROR")

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
        result = PilaO.pop()
        quadr = quadruple(len(Quad), 'gotof', result, None, None)
        Quad.append(quadr)
        PJumps.append(len(Quad)-1)
    else:
        print("ERROR")

def mostrarSize():
    for i in range(len(POper)):
        print(POper[i])



def moduloDos(direccion):
    quadr = quadruple(len(Quad), 'era', None, None, direccion)
    getFunc(direccion)
    Quad.append(quadr)
    global paramCont
    paramCont = 1

quadAuxParaParametros = []
funcName = None
paramDireccion = None
varsTableAux = []

def moduloTres():
    argument = PilaO.pop()
    AVAIL.pop()
    quadr = quadruple(0, 'param', argument, None, 'param')
    quadAuxParaParametros.append(quadr)
    sumaParametro()



def getFunc(direccion):
    for x in directFunc.funciones:
        if x.direccion == direccion:
            global funcName 
            funcName = x.id
    filterSimbolosDeFunc()
            
def filterSimbolosDeFunc():
    for x in simbolos:
        if x.funcion == funcName:
            varsTableAux.append(x)
    
def sumaParametro():
    global paramCont
    paramCont = paramCont + 1

def moduloSeis(id, alcance, direccion):
    for i in range(1,paramCont):
        x = quadAuxParaParametros.pop()
        x.contQua = len(Quad)
        x.result = varsTableAux[i-1].direccion
        Quad.append(x)
    quadr = quadruple(len(Quad), 'gosub', direccion, None, alcance)
    Quad.append(quadr)

def miReturn():
    result = PilaO.pop()
    PTypes.pop()
    AVAIL.pop()
    quadr = quadruple(len(Quad), 'return', None, None, result)
    Quad.append(quadr)
    
def endproc():
    quadr = quadruple(len(Quad), 'endproc', None, None, None)
    Quad.append(quadr)
    #memoriaPadre.memoria_local[0].cleanMemory()

def endPrograma():
    quadr = quadruple(len(Quad), 'end', None, None, None)
    Quad.append(quadr)

def verificaDim(id):
    size = len(simbolos)
    for i in range(size):
        if(simbolos[i].id == id):
            dimension = simbolos[i].dimension
    
    #direccion = memoriaPadre.memoria_local[0].getDirTemporal('int')
    operand = PilaO.pop()
    value = AVAIL.pop()
    tipo = PTypes.pop()
    quadr = quadruple(len(Quad), 'ver', value, dimension, value)
    Quad.append(quadr)
    prueba = PilaO.pop()
    prueba = int(prueba) + int(value)
    PilaO.append(prueba)
    PilaDim.append(value)

def asignacionDimensionada():
    PoperSize = len(POper)
    if (PoperSize > 0):
        if(POper[PoperSize- 1] == '='):
            leftDireccion = PilaO.pop()
            rightDireccion = PilaO.pop()
            dim1 = AVAIL.pop()
            AVAIL.pop()
            dim2 = AVAIL.pop()
            operator = POper.pop()
            left = int(leftDireccion) + int(dim1)
            right = int(rightDireccion) + int(dim2)
            quadr = quadruple(len(Quad), operator, left, None, right)
            Quad.append(quadr)
            result = rightDireccion