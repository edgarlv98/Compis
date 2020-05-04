import sys

operators = ['+', '-', '*', '/']
comparators = ['==', '>', '<', '!=']

def semantic(left, right, operator):
    if(left == 'int'):
        if(right == 'int'):
            if(operator in operators or operator == '='):
                return 'int'
            elif(operator in comparators):
                return 'bool'
            else:
                return 'error'
        elif(right == 'float'):
            if(operator in operators):
                return 'float'
            elif(operator in comparators):
                return 'bool'
            else:
                return 'error'
        else:
            return 'error'
    elif(left == 'float'):
        if(right == 'float'):
            if(operator in operators or operator == '='):
                return 'float'
            elif(operator in comparators):
                return 'bool'
            else:
                return 'error'
        elif(right == 'int'):
            if(operator in operators):
                return 'float'
            elif(operator in comparators):
                return 'bool'
            else:
                return 'error'
        else:
            return 'error'
    elif(left == 'char'):
        if(right == 'char'):
            if(operator == '=' or operator == '+'):
                return 'char'
            elif(operator == '==' or operator == '!='):
                return 'bool'
            else:
                return 'error'
        else:
            return 'error'
    else:
        return 'error'


