import sys
import memoriaPadre

simbolos = []

tipo = None
Id = None
direccion = None
valor = None
funcion = None

#Objeto tabla variables#
class variable(object):
    def __init__(self, id, tipo, direccion, funcion, value=None):
        self.id = str(id)
        self.tipo = str(tipo)
        self.direccion = direccion
        self.value = str(value)
        self.funcion = funcion

def insert(id, tipo, direccion, funcion):
    temp = variable(id, tipo, direccion, funcion)
    if (len(simbolos) >= 1 and not repeatID(id, funcion)) or len(simbolos) == 0:
        simbolos.append(temp)

def repeatID(id, funcion):
    aux = False

    for i in range (len(simbolos)):
        if simbolos[i].id == id and simbolos[i].funcion == funcion:
            aux = True
            print("ERROR: El ID ya existe: ", id)
            sys.exit()
    return aux

def update(id, value):
    for i in range (len(simbolos)):
        if simbolos[i].id == id:
            simbolos[i].value = value
            direccion = simbolos[i].direccion
            tipo = simbolos[i].tipo
            if(simbolos[i].funcion == 'global'):
                memoriaPadre.memoria_global.updateGlobalVariable(value, direccion, tipo)
            else:
                memoriaPadre.memoria_local[0].updateVariableLocal(value, direccion, tipo)

def show():
    longitud = len(simbolos)
    for i in range(0, longitud):
        print(simbolos[i].tipo, simbolos[i].id, simbolos[i].value, simbolos[i].direccion, simbolos[i].funcion)