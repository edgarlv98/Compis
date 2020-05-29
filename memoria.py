import sys
import estructuraMemorias
from pprint import pprint



class memoria(object):
    memoria_global = None
    local = None
    temporal = None

    def __init__(self):
        self.memoria_global = estructuraMemorias.estrmemoria()
        self.local = estructuraMemorias.estrmemoria()
        self.temporal = estructuraMemorias.estrmemoria()

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


    def getTipo(self, cte):
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
    def is_float(self, cte):
        try:
            return float(cte) and '.' in cte
        except ValueError:
            return False

    # Funcion que checa de que tipo es la constante
    def getTipoCte(self, cte):
        isFloat = self.is_float(cte)
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
    def getDirCte(self, tipo):
        if(tipo == 'int'):
            temp = self.memoCteInt
            self.memoCteInt += 1
        elif(tipo == 'float'):
            temp = self.memoCteFloat
            self.memoCteFloat += 1
        elif(tipo == 'char'):
            temp = self.memoCteChar
            self.memoCteChar += 1
        return temp

    # Funcion que actualiza el valor de una direccion 
    # en memoria local
    def updateCte(self, valor, dir, tipo):
        if(tipo == "int"):
            self.local.int[dir] = valor
        if(tipo == "float"):
            self.local.float[dir] = valor
        if(tipo == "char"):
            self.local.char[dir] = valor
        if(tipo == "bool"):
            self.local.bool[dir] = valor

    # Funcion que regresa el valor de una direccion 
    # dada una direccion
    def regresaValor(self, direccion, tipo):
        valor = None
        if(tipo == "int"):
            valor = self.local.int.get(direccion)
            return int(valor)
        if(tipo == "float"):
            valor = self.local.float.get(direccion)
            return float(valor)
        if(tipo == "char"):
            valor = self.local.char.get(direccion)
            return valor
        if(tipo == "bool"):
            valor = self.local.bool.get(direccion)
            return valor

    # Funcion que regresa el valor dada una direccion y un tipo
    def getValor(self, direccion, tipo):
        if tipo is None:
            tipo = self.getTipoDireccion(direccion)
        if(tipo == 'int'):
            temp = self.local.int[direccion]
        elif(tipo == 'float'):
            temp = self.local.float[direccion]
        elif(tipo == 'char'):
            temp = self.local.char[direccion]
        elif(tipo == 'bool'):
            temp = self.local.bool[direccion]
        return temp

    # Funcion que checa si una constante ya se encuentra en
    # memoria local CONSTANTES
    def repeatCte(self, cte):
        tipo = self.getTipoCte(cte)

        self.ints = 20000
        self.floats = 21000
        self.chars = 22000

        if(tipo == 'int'):
            if(self.local.int):
                i = self.ints
                while(i < self.memoCteInt):
                    if(cte == self.local.int[i]):
                        return True
                    i += 1
                return False
            else:
                return False
        elif(tipo == 'float'):
            if(self.local.float):
                i = self.floats
                while(i < self.memoCteFloat):
                    if(cte == self.local.float[i]):
                        return True
                    i += 1
                return False
            else:
                return False
        elif(tipo == 'char'):
            if(self.local.char):
                i = self.chars
                while(i < self.memoCteFloat):
                    if(cte == self.local.char[i]):
                        return True
                    i += 1
                return False
            else:
                return False
        else:
            return False

    # Funcion que regresa la direccion de una constante,
    # esto cuando ya existe esta constante en memoria
    def getDirRepeatCte(self, cte):

        self.cteInt = 20000
        self.cteFloat = 21000
        self.cteChar = 22000

        tipo = self.getTipoCte(cte)

        if tipo == 'int':
            for dir, value in self.local.int.items():
                if (dir >= self.cteInt) and (dir < self.cteFloat):
                    if cte == value:
                        return dir
        elif tipo == 'float':
            for dir, value in self.local.float.items():
                if (dir >= self.cteFloat) and (dir < self.cteChar):
                    if cte == value:
                        return dir
        elif tipo == 'char':
            for dir, value in self.local.char.items():
                if (dir >= self.cteChar) and (dir < self.cteChar + 1000):
                    if cte == value:
                        return dir
        return "error"

    ## MEMORIA TEMPORALES ##

    # Funcion que regresa una direccion para un temporal
    def getDirTemporal(self, tipo):
        if(tipo == 'int'):
            temp = self.memoTempInt
            self.memoTempInt += 1
        elif(tipo == 'float'):
            temp = self.memoTempFloat
            self.memoTempFloat += 1
        elif(tipo == 'char'):
            temp = self.memoTempChar
            self.memoTempChar += 1
        elif(tipo == 'bool'):
            temp = self.memoTempBool
            self.memoTempBool += 1
        return temp

    # Funcion que actualiza el valor de una direccion
    # en memoria local TEMPORALES
    def updateTemporal(self, valor, dir, tipo):
        if(tipo == "int"):
            self.local.int[dir] = valor
        if(tipo == "float"):
            self.local.float[dir] = valor
        if(tipo == "char"):
            self.local.char[dir] = valor
        if(tipo == "bool"):
            self.local.bool[dir] = valor

    # Funcion que regresa el tipo dada una direccion
    def getTipoDireccion(self, direccion):
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
    def getDirVarGlobal(self, tipo):
        if(tipo == 'int'):
            temp = self.globalInt
            self.globalInt += 1
        elif(tipo == 'float'):
            temp = self.globalFloat
            self.globalFloat += 1
        elif(tipo == 'char'):
            temp = self.globalChar
            self.globalChar += 1
        return temp

    # Actualiza el valor de una direccion global dado un 
    # tipo y una direccion
    def updateGlobalVariable(self, valor, dir, tipo):
        if(tipo == "int"):
            self.memoria_global.int[dir] = valor
        if(tipo == "float"):
            self.memoria_global.float[dir] = valor
        if(tipo == "char"):
            self.memoria_global.char[dir] = valor

    # Actualiza el valor de una direccion local dado un
    # tipo y una direccion
    def updateVariableLocal(self, valor, dir, tipo):
        if(tipo == "int"):
            self.local.int[dir] = valor
        if(tipo == "float"):
            self.local.float[dir] = valor
        if(tipo == "char"):
            self.local.char[dir] = valor
        if(tipo == "bool"):
            self.local.bool[dir] = valor

    # Funcion que regresa una direccion para una fucion
    # dependiendo de su tipo
    def getDirFuncion(self, tipo):
        if(tipo == 'int'):
            temp = self.memoFuncInt
            self.memoFuncInt += 1
        elif(tipo == 'float'):
            temp = self.memoFuncFloat
            self.memoFuncFloat += 1
        elif(tipo == 'char'):
            temp = self.memoFuncChar
            self.memoFuncChar += 1
        elif(tipo == 'void'):
            temp = self.memoFuncVoid
            self.memoFuncVoid += 1
        return temp

    # Funcion que regresa una direccion para una variable
    # dependiendo de su tipo
    def getDirvariableLocal(self, tipo):
        if(tipo == 'int'):
            temp = self.memoLocalInt
            self.memoLocalInt += 1
        elif(tipo == 'float'):
            temp = self.memoLocalFloat
            self.memoLocalFloat += 1
        elif(tipo == 'char'):
            temp = self.memoLocalChar
            self.memoLocalChar += 1
        return temp

    # Funcion que limpia las direcciones de los temporales
    def cleanMemory(self):

        self.memoTempInt = 10000
        self.memoTempFloat = 10100
        self.memoTempChar = 10200
        self.memoTempBool = 10300

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

    def show(self):
        print("GLOBAL")
        print("INT")
        pprint(self.memoria_global.int, width=1)
        #print("TEMPORALES")
        #print("INT")
        #pprint(temporal.int, width=1)
        #print("FLOAT")
        #pprint(temporal.float, width=1)
        #print("BOOL")
        #pprint(temporal.bool, width=1)
        print("LOCAAAAAAAAL")
        print("INT")
        pprint(self.local.int, width=1)
        print("FLOAT")
        pprint(self.local.float, width=1)
        print("CHAR")
        pprint(self.local.char, width=1)
        print("BOOL")
        pprint(self.local.bool, width=1)
