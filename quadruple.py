import sys
from vars_table import simbolos
from sematic_cube import semantic
import memoria

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

#Clase del cuadruplo
class quadruple(object):
    def __init__(self, contQua, operator, left_operand, right_operand, result=None):
        self.contQua = contQua
        self.left_operand = left_operand
        self.right_operand = right_operand
        self.operator = operator
        self.result = result

def pushID(id):
    PilaO.append(id)
    size = len(simbolos)
    for i in range(size):
        if(id == simbolos[i].id):
            AVAIL.append(simbolos[i].value)
            PTypes.append(simbolos[i].tipo)

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
                if(operator == '+'):
                    result = left_value + right_value
                else:
                    result = left_value - right_value
                direccion = memoria.getDirTemporal(result_type)
                memoria.updateTemporal(result, direccion, result_type)
                quadr = quadruple(len(Quad), operator, left_operand, right_operand, direccion)
                Quad.append(quadr)
                AVAIL.append(result)
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
                if(operator == '*'):
                    result = left_value * right_value
                else:
                    result = left_value / right_value
                direccion = memoria.getDirTemporal(result_type)
                memoria.updateTemporal(result, direccion, result_type)
                quadr = quadruple(len(Quad), operator, left_operand, right_operand, direccion)
                Quad.append(quadr)
                AVAIL.append(result)
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
            if(operator == '>'):
                result = left_value > right_value
            elif(operator == '<'):
                result = left_value < right_value
            elif(operator == '=='):
                result = left_value == right_value
            elif(operator == '!='):
                result = left_value != right_value
            direccion = memoria.getDirTemporal(result_type)
            memoria.updateTemporal(result, direccion, result_type)
            quadr = quadruple(len(Quad), operator, left_operand, right_operand, direccion)
            Quad.append(quadr)
            AVAIL.append(result)
            PilaO.append(direccion)
            PTypes.append('bool')
    #else:
    #    print("ERROR")

def createQuadPrint():
    POperSize = len(POper)
    if POperSize > 0:
        if POper[POperSize-1] == 'print':
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



def moduloDos(id):
    quadr = quadruple(len(Quad), 'era', None, None, id)
    Quad.append(quadr)
    global paramCont
    paramCont = 1

quadAuxParaParametros = []


def moduloTres():
    argument = PilaO.pop()
    AVAIL.pop()
    quadr = quadruple(0, 'param', argument, None, 'param')
    quadAuxParaParametros.append(quadr)
    sumaParametro()

def sumaParametro():
    global paramCont
    paramCont = paramCont + 1

def moduloSeis(id, addres):
    for i in range(1,paramCont):
        x = quadAuxParaParametros.pop()
        num = str(i)
        x.contQua = len(Quad)
        x.result = 'param' + num
        Quad.append(x)
    quadr = quadruple(len(Quad), 'gosub', id, None, addres)
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