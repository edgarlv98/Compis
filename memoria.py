import sys
import estructuraMemorias
from pprint import pprint

memoria_local = estructuraMemorias.memoria()
memoria_temporal = estructuraMemorias.memoria()

# contadores de direcciones de memoria
memoIntUsada = []
memoFloatUsada = []
memoCharUsada = []
memoBoolUsada = []

# Direccion de memoria globales
globalInt = 5000
globalFloat = 5100
globalChar = 5200

# Direccion de memoria temporales
memoTempInt = 10000
memoTempFloat = 10100
memoTempChar = 10200
memoTempBool = 10300

# Direccion de memoria de las constantes
memoCteInt = 20000
memoCteFloat = 21000
memoCteChar = 22000

# Direccion de memoria de las funciones
memoFuncInt = 7000
memoFuncFloat = 7100
memoFuncChar = 7200

# Direccion de memoria del main
memoMainInt = 9000
memoMainFloat = 9100
memoMainChar = 9200

# Direccion temporal del main
tempMainInt = 20000
tempMainFloat = 21000
tempMainChar = 22000
tempMainBool = 23000


## CONSTANTES ##
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
    if(tipo == 'int'):
        temp = memoCteInt
        memoCteInt += 1
    elif(tipo == 'float'):
        temp = memoCteFloat
        memoCteFloat += 1
    elif(tipo == 'char'):
        temp = memoCteChar
        memoCteChar += 1
    return temp

def updateCte(valor, dir, tipo):
    if(tipo == "int"):
        memoria_local.int[dir] = valor
    if(tipo == "float"):
        memoria_local.float[dir] = valor
    if(tipo == "char"):
        memoria_local.char[dir] = valor

def getValor(direccion, tipo):
    if(tipo == 'int'):
        temp = memoria_local.int[direccion]
    elif(tipo == 'float'):
        temp = memoria_local.float[direccion]
    elif(tipo == 'char'):
        temp = memoria_local.char[direccion]
    elif(tipo == 'bool'):
        temp = memoria_local.bool[direccion]
    return temp

## TEMPORALES ##

def getDirTemporal(tipo):
    global memoTempInt
    global memoTempFloat
    global memoTempChar
    global memoTempBool
    if(tipo == 'int'):
        temp = memoTempInt
        memoTempInt += 1
    elif(tipo == 'float'):
        temp = memoTempFloat
        memoTempFloat += 1
    elif(tipo == 'char'):
        temp = memoTempChar
        memoTempChar += 1
    elif(tipo == 'bool'):
        temp = memoTempBool
        memoTempBool += 1
    return temp


def updateTemporal(valor, dir, tipo):
    if(tipo == "int"):
        memoria_temporal.int[dir] = valor
    if(tipo == "float"):
        memoria_temporal.float[dir] = valor
    if(tipo == "char"):
        memoria_temporal.char[dir] = valor
    if(tipo == "bool"):
        memoria_temporal.bool[dir] = valor

def show():
    print("TEMPORALES")
    print("INT")
    pprint(memoria_temporal.int, width=1)
    print("FLOAT")
    pprint(memoria_temporal.float, width=1)
    print("BOOL")
    pprint(memoria_temporal.bool, width=1)

    print("CTEEE")
    print("INT")
    pprint(memoria_local.int, width=1)
    print("FLOAT")
    pprint(memoria_local.float, width=1)
