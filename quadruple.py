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
    def __init__(self, contQua, left_operand, right_operand, operator, result):
        self.contQua = contQua
        self.left_operand = left_operand
        self.right_operand = right_operand
        self.operator = operator
        self.result = result


