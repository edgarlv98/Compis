import sys
import estructuraMemorias
from pprint import pprint

memoria_local = estructuraMemorias.memoria()

# contadores de direcciones de memoria
memoIntUsada = []
memoFloatUsada = []
memoCharUsada = []
memoBoolUsada = []

# Direccion de memorias globales
globalInt = 5000
globalFloat = 5100
globalChar = 5200

# Direccion de memorias temporales
memoTempInt = 43000
memoTempFloat = 43100
memoTempChar = 43200
memoTempBool = 43300

# Direccion de memorias de las constantes
memoCteInt = 20000
memoCteFloat = 21000
memoCteChar = 22000

# Direccion de memoria de las funciones
memoFuncInt = 9000
memoFuncFloat = 9100
memoFuncChar = 9200
memoFuncBool = 9300

# Direccion de memoria del main
memoMainInt = 8000
memoMainFloat = 8100
memoMainChar = 8200

# Direccion temporal del main
tempMainInt = 85000
tempMainFloat = 86000
tempMainChar = 87000
tempMainBool = 88000

def is_float(cte):
    try:
        return float(cte) and '.' in cte
    except ValueError:
        return False

def getTipoCte(cte):
    isFloat = is_float(cte)
    if(isFloat):
        temp = 'float'
        return temp
    else:
        isInt = cte.isdigit()
        if(isInt):
            temp = 'int'
            return temp
        else:
           temp = 'char'
           return temp

def getDirCte(tipo):
    global memoCteInt
    global memoCteFloat
    global memoCteChar
    if tipo == 'int':
        temp = memoCteInt
        memoCteInt += 1
    elif tipo == 'float':
        temp = memoCteFloat
        memoCteFloat += 1
    elif tipo == 'char':
        temp = memoCteChar
        memoCteChar += 1
    return temp

def updateCte(valor, dir, tipo):
    if tipo == "int":
        memoria_local.int[dir] = valor
    if tipo == "float":
        memoria_local.float[dir] = valor
    if tipo == "char":
        memoria_local.char[dir] = valor
    if tipo == "bool":
        memoria_local.booleanos[dir] = valor

def show():
    print("INT")
    pprint(memoria_local.int, width=1)
    print("FLOAT")
    pprint(memoria_local.float, width=1)