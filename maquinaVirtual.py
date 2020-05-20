from quadruple import Quad


def inicio():
    i = 0
    for i in range(len(Quad)):
        print(Quad[i].contQua, Quad[i].operator, Quad[i].left_operand, Quad[i].right_operand, Quad[i].result)