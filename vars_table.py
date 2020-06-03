import sys
import memoriaPadre

simbolos = []

tipo = None
Id = None
direccion = None
valor = None
funcion = None
esArreglo = False

#Objeto tabla variables#
class variable(object):
    def __init__(self, id, tipo, direccion, funcion, dimension = 0, value=None):
        self.id = str(id)
        self.tipo = str(tipo)
        self.direccion = direccion
        self.value = str(value)
        self.funcion = funcion
        self.dimension = dimension

#Inserta a la tabla de variables
def insert(id, tipo, direccion, funcion):
    temp = variable(id, tipo, direccion, funcion)
    if (len(simbolos) >= 1 and not repeatID(id, funcion)) or len(simbolos) == 0:
        simbolos.append(temp)

#Inserta a la tabla de variables
def insertDimensionada(id, tipo, direccion, funcion, dimension):
    aux = memoriaPadre.memoria_local[0].getDirvariableLocal('dimension')
    memoriaPadre.memoria_local[0].updateVariableLocal(dimension,aux,'dimension')
    temp = variable(id, tipo, direccion, funcion, aux)
    if (len(simbolos) >= 1 and not repeatID(id, funcion)) or len(simbolos) == 0:
        simbolos.append(temp)

#Funcion que checa si se repite una variable
def repeatID(id, funcion):
    aux = False

    for i in range (len(simbolos)):
        if simbolos[i].id == id and simbolos[i].funcion == funcion and esArreglo == False:
            aux = True
            print("ERROR: El ID ya existe: ", id)
            sys.exit()
    return aux

#Funcion que actualiza el valor de una variable
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

#Muestra las variables
def show():
    longitud = len(simbolos)
    for i in range(0, longitud):
        print(simbolos[i].id, simbolos[i].tipo, simbolos[i].direccion, simbolos[i].funcion, simbolos[i].dimension, simbolos[i].value)
        