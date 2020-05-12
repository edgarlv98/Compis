import sys

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

def pushCTE(id):
    PilaO.append(id)

def pushTipo(tipo):
    PTypes.append(tipo)

def pushPoper(operador):
    POper.append(operador)

def createQuadAssign():
    POperSize = len(POper)
    if(POper[POperSize] == '='):
        right_operand = PilaO.pop()
        left_operand = PilaO.pop()
        operator = POper.pop()
        quadr = quadruple(len(Quad), operator, right_operand, None, left_operand)
        Quad.append(quadr)
    else:
        print("ERROR")

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
    if (POper[POperSize] == '*' or POper[POperSize] == '/'):
        right_operand = PilaO.pop()
        left_operand = PilaO.pop()
        operator = POper.pop()
        #if(operator == '*'):
        #    result = left_operand * right_operand
        #else:
        #    result = left_operand / right_operand
        #quadr = quadruple(len(Quad), operator, left_operand, right_operand)
        #Quad.append(quadr)
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
    print(len(POper))
    