import sys
import estructuraMemorias
from pprint import pprint

memoria_global = estructuraMemorias.memoria()
memoria_local = estructuraMemorias.memoria()
memoria_temporal = estructuraMemorias.memoria()

# Direccion de memoria globales
globalInt = 5000
globalFloat = 5100
globalChar = 5200

# Direccion de memoria variables locales
memoLocalInt = 15000
memoLocalFloat = 15100
memoLocalChar = 15200

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
memoFuncVoid = 7300

# Direccion de memoria del main
memoMainInt = 9000
memoMainFloat = 9100
memoMainChar = 9200

# Direccion temporal del main
tempMainInt = 2000
tempMainFloat = 2100
tempMainChar = 2200
tempMainBool = 2300


def getTipo(cte):
    tipo = str(type(cte))
    temp = None
    if cte == 'true' or cte == 'false':
        temp = 'bool'
        return temp
    if tipo == "<class 'float'>":
        temp = 'float'
        return temp
    if tipo == "<class 'int'>":
        temp = 'int'
        return temp
    if tipo == "<class 'str'>":
        temp = 'string'
        return temp


## MEMORIA CONSTANTES ##

# Funcion que checa si una cte es FLOAT,
# esta funcion se utiliza en getTipoCte para identificar el tipo
def is_float(cte):
    try:
        return float(cte) and '.' in cte
    except ValueError:
        return False

# Funcion que checa de que tipo es la constante
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

# Funcion que regresa una direccion para una constante
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

# Funcion que actualiza el valor de una direccion 
# en memoria local
def updateCte(valor, dir, tipo):
    if(tipo == "int"):
        memoria_local.int[dir] = valor
    if(tipo == "float"):
        memoria_local.float[dir] = valor
    if(tipo == "char"):
        memoria_local.char[dir] = valor
    if(tipo == "bool"):
        memoria_local.bool[dir] = valor

# Funcion que regresa el valor de una direccion 
# dada una direccion
def regresaValor(direccion, tipo):
    valor = None
    if(tipo == "int"):
        valor = memoria_local.int.get(direccion)
        return int(valor)
    if(tipo == "float"):
        valor = memoria_local.float.get(direccion)
        return float(valor)
    if(tipo == "char"):
        valor = memoria_local.char.get(direccion)
        return valor
    if(tipo == "bool"):
        valor = memoria_local.bool.get(direccion)
        return valor

# Funcion que regresa el valor dada una direccion y un tipo
def getValor(direccion, tipo):
    if tipo is None:
        tipo = getTipoDireccion(direccion)
    if(tipo == 'int'):
        temp = memoria_local.int[direccion]
    elif(tipo == 'float'):
        temp = memoria_local.float[direccion]
    elif(tipo == 'char'):
        temp = memoria_local.char[direccion]
    elif(tipo == 'bool'):
        temp = memoria_local.bool[direccion]
    return temp

# Funcion que checa si una constante ya se encuentra en
# memoria local CONSTANTES
def repeatCte(cte):
    tipo = getTipoCte(cte)

    global memoCteInt
    global memoCteFloat
    global memoCteChar

    ints = 20000
    floats = 21000
    chars = 22000

    if(tipo == 'int'):
        if(memoria_local.int):
            i = ints
            while(i < memoCteInt):
                if(cte == memoria_local.int[i]):
                    return True
                i += 1
            return False
        else:
            return False
    elif(tipo == 'float'):
        if(memoria_local.float):
            i = floats
            while(i < memoCteFloat):
                if(cte == memoria_local.float[i]):
                    return True
                i += 1
            return False
        else:
            return False
    elif(tipo == 'char'):
        if(memoria_local.char):
            i = chars
            while(i < memoCteFloat):
                if(cte == memoria_local.char[i]):
                    return True
                i += 1
            return False
        else:
            return False
    else:
        return False

# Funcion que regresa la direccion de una constante,
# esto cuando ya existe esta constante en memoria
def getDirRepeatCte(cte):
    global memoCteInt
    global memoCteFloat
    global memoCteChar

    cteInt = 20000
    cteFloat = 21000
    cteChar = 22000

    tipo = getTipoCte(cte)

    if tipo == 'int':
        for dir, value in memoria_local.int.items():
            if (dir >= cteInt) and (dir < cteFloat):
                if cte == value:
                    return dir
    elif tipo == 'float':
        for dir, value in memoria_local.float.items():
            if (dir >= cteFloat) and (dir < cteChar):
                if cte == value:
                    return dir
    elif tipo == 'char':
        for dir, value in memoria_local.char.items():
            if (dir >= cteChar) and (dir < cteChar + 1000):
                if cte == value:
                    return dir
    return "error"

## MEMORIA TEMPORALES ##

# Funcion que regresa una direccion para un temporal
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

# Funcion que actualiza el valor de una direccion
# en memoria local TEMPORALES
def updateTemporal(valor, dir, tipo):
    if(tipo == "int"):
        memoria_local.int[dir] = valor
    if(tipo == "float"):
        memoria_local.float[dir] = valor
    if(tipo == "char"):
        memoria_local.char[dir] = valor
    if(tipo == "bool"):
        memoria_local.bool[dir] = valor

# Funcion que regresa el tipo dada una direccion
def getTipoDireccion(direccion):
    if (direccion >= 10000 and direccion < 10100) or (direccion >= 20000 and direccion < 21000) or (direccion >= 7000 and direccion < 7100) or (direccion >= 9000 and direccion < 9100) or (direccion >= 2000 and direccion < 2100) or (direccion >= 15000 and direccion < 15100):
        tipo = "int"
        return tipo
    elif (direccion >= 10100 and direccion < 10200) or (direccion >= 21000 and direccion < 22000) or (direccion >= 7100 and direccion < 7200) or (direccion >= 9100 and direccion < 9200) or (direccion >= 2100 and direccion < 2200) or (direccion >= 15100 and direccion < 15200):
        tipo = "float"
        return tipo
    elif (direccion >= 10200 and direccion < 10300) or (direccion >= 22000) or (direccion >= 7200 and direccion < 7300) or (direccion >= 9200) or (direccion >= 22000 and direccion < 23000) or (direccion >= 15200 and direccion < 15300):
        tipo = "char"
        return tipo
    else:
        tipo = "bool"
        return tipo

# Funcion que agrega las variables globales a una
# memoria global
def getDirVarGlobal(tipo):
    global globalInt
    global globalFloat
    global globalChar

    if(tipo == 'int'):
        temp = globalInt
        globalInt += 1
    elif(tipo == 'float'):
        temp = globalFloat
        globalFloat += 1
    elif(tipo == 'char'):
        temp = globalChar
        globalChar += 1
    return temp

# Actualiza el valor de una direccion global dado un 
# tipo y una direccion
def updateGlobalVariable(valor, dir, tipo):
    if(tipo == "int"):
        memoria_global.int[dir] = valor
    if(tipo == "float"):
        memoria_global.float[dir] = valor
    if(tipo == "char"):
        memoria_global.char[dir] = valor

# Actualiza el valor de una direccion local dado un
# tipo y una direccion
def updateVariableLocal(valor, dir, tipo):
    if(tipo == "int"):
        memoria_local.int[dir] = valor
    if(tipo == "float"):
        memoria_local.float[dir] = valor
    if(tipo == "char"):
        memoria_local.char[dir] = valor
    if(tipo == "bool"):
        memoria_local.bool[dir] = valor

# Funcion que regresa una direccion para una fucion
# dependiendo de su tipo
def getDirFuncion(tipo):
    global memoFuncInt 
    global memoFuncFloat
    global memoFuncChar
    global memoFuncVoid
    if(tipo == 'int'):
        temp = memoFuncInt
        memoFuncInt += 1
    elif(tipo == 'float'):
        temp = memoFuncFloat
        memoFuncFloat += 1
    elif(tipo == 'char'):
        temp = memoFuncChar
        memoFuncChar += 1
    elif(tipo == 'void'):
        temp = memoFuncVoid
        memoFuncVoid += 1
    return temp

# Funcion que regresa una direccion para una variable
# dependiendo de su tipo
def getDirvariableLocal(tipo):
    global memoLocalInt
    global memoLocalFloat
    global memoLocalChar
    if(tipo == 'int'):
        temp = memoLocalInt
        memoLocalInt += 1
    elif(tipo == 'float'):
        temp = memoLocalFloat
        memoLocalFloat += 1
    elif(tipo == 'char'):
        temp = memoLocalChar
        memoLocalChar += 1
    return temp

# Funcion que limpia las direcciones de los temporales
def cleanMemory():
    global memoTempInt
    global memoTempFloat
    global memoTempBool
    global memoTempChar

    memoTempInt = 10000
    memoTempFloat = 10100
    memoTempChar = 10200
    memoTempBool = 10300

    #global memoLocalInt 
    #global memoLocalFloat
    #global memoLocalChar
    #memoLocalInt = 15000
    #memoLocalFloat = 15100
    #memoLocalChar = 15200
    #global memoCteInt 
    #global memoCteFloat
    #global memoCteChar
    #memoCteInt = 20000
    #memoCteFloat = 21000
    #memoCteChar = 22000

def show():
    print("GLOBAL")
    print("INT")
    pprint(memoria_global.int, width=1)
    #print("TEMPORALES")
    #print("INT")
    #pprint(memoria_temporal.int, width=1)
    #print("FLOAT")
    #pprint(memoria_temporal.float, width=1)
    #print("BOOL")
    #pprint(memoria_temporal.bool, width=1)
    print("LOCAAAAAAAAL")
    print("INT")
    pprint(memoria_local.int, width=1)
    print("FLOAT")
    pprint(memoria_local.float, width=1)
    print("CHAR")
    pprint(memoria_local.char, width=1)
    print("BOOL")
    pprint(memoria_local.bool, width=1)
