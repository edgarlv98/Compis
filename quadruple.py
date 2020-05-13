import sys
from vars_table import simbolos
from sematic_cube import semantic

#Pilas
POper = []
PilaO = []
PTypes = []
Quad = []
AVAIL = []
PJumps = []


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


def pushCTE(cte):
    PilaO.append(cte)
    tipo = str(type(cte))
    #if cte == 'true' or cte == 'false':
    #    tipo = "<type 'bool'>"
    #if tipo == "<type 'float'>":
    #    PTypes.append('float')
    #if tipo == "<type 'int'>":
    #    PTypes.append('int')
    #if tipo == "<type 'str'>":
    #    PTypes.append('string')
    #if tipo == "<type 'bool'>":
    #    PTypes.append('bool')
    AVAIL.append(cte)
    PTypes.append('int')

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
            PTypes.append(result_type)
            if(result_type != 'error'):
                quadr = quadruple(len(Quad), operator, right_operand, None, left_operand)
                Quad.append(quadr)
    else:
        print("ERROR")

def cuadruplosAsignacion():
    for i in range(len(Quad)):
        print(Quad[i].contQua, Quad[i].operator, Quad[i].left_operand, Quad[i].right_operand, Quad[i].result)

def createQuadTerm():
    POperSize = len(POper)
    print(POperSize)
    if(POper[POperSize] == '+' or POper[POperSize] == '-'):
        right_operand = PilaO.pop()
        left_operand = PilaO.pop()
        operator = POper.pop()
        #if(operator == '+'):
        #    result = left_operand + right_operand
        #else:
        #    result = left_operand - right_operand
        #quadr = quadruple(len(Quad), operator, left_operand, right_operand)
        #Quad.append(quadr)
    else:
        print("ERROR")

def createQuadFact():
    POperSize = len(POper)
    if(POperSize > 0):
        if (POper[POperSize-1] == '*' or POper[POperSize-1] == '/'):
            right_operand = PilaO.pop()
            right_type = PTypes.pop()
            right_value = AVAIL.pop()
            left_operand = PilaO[POperSize-1]
            left_type = PTypes[POperSize-1]
            left_value = AVAIL.pop()
            operator = POper.pop()
            result_type = semantic(left_type, right_type, operator)
            if(operator == '*'):
                result = int(left_value) * int(right_value)
                AVAIL.append(result)
            else:
                result = int(left_value) / int(right_value)
                AVAIL.append(result)
            quadr = quadruple(len(Quad), operator, left_operand, right_operand, result)
            Quad.append(quadr)
            PTypes.append(result_type)
    else:
        print("ERROR")

def createQuadComp():
    POperSize = len(POper)
    if(POper[POperSize] == '>' or POper[POperSize-1] == '<' or POper[POperSize] == '==' or POper[POperSize] == '!='):
        right_operand = PilaO.pop()
        left_operand = PilaO.pop()
        operator = POper.pop()
        #if(operator == '>'):
        #    result = left_operand > right_operand
        #elif(operator == '<'):
        #    result = left_operand < right_operand
        #elif(operator == '=='):
        #    result = left_operand == right_operand
        #elif(operator == '!='):
        #    result = left_operand != right_operand
        #quadr = quadruple(len(Quad), operator, left_operand, right_operand)
        #Quad.append(quadr)
    else:
        print("ERROR")

def mostrarSize():
    for i in range(len(POper)):
        print(POper[i])
    