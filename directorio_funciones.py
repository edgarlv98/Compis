import sys
import vars_table

funciones = []

tipo = None
Id = None
direccion = None
variables = []
params = 0

#Objeto directorio funciones#
class funcion(object):
    def __init__(self, id, tipo, alcance, direccion):
        self.id = str(id)
        self.tipo = str(tipo)
        self.alcance = alcance
        self.direccion = direccion
        self.params = 0

def insert(id, tipo, alcance, direccion):
    temp = funcion(id, tipo, alcance, direccion)
    if (len(funciones) >= 1 and not repeatID(id)) or len(funciones) == 0:
        funciones.append(temp)

def repeatID(id):
    aux = False
    for i in range (len(funciones)):
        if funciones[i].id == id:
            aux = True
            print("ERROR: El ID de la funcion ya existe: ", id)
            sys.exit()
    return aux

def agregaSimbolos(simbolo):
    variables.append(simbolo)

def show():
    longitud = len(funciones)
    for i in range(0, longitud):
        print(funciones[i].id, funciones[i].tipo, funciones[i].direccion, funciones[i].params)