import sys
import vars_table as varsTable

funciones = []

tipo = None
Id = None

#Objeto directorio funciones#
class directorio(object):
    def __init__(self, id, type_data):
        self.id = str(id)
        self.type_data = str(type_data)

def show():
    longitud = len(funciones)
    i = 0
    for i in range(0, longitud):
        print(funciones[i].id, funciones[i].type_data)

def insert(id, type_data):
    temp = directorio(id, type_data)
    if len(funciones) >= 1 and not repeatID(id):
        funciones.append(temp)
    if len(funciones) == 0:
        funciones.append(temp)

def repeatID(id):
    aux = False
    for i in range (len(funciones)):
        if funciones[i].id == id:
            aux = True
            print("ERROR: El ID de la funcion ya existe: ", id)
            sys.exit()
    return aux

def show():
    longitud = len(funciones)
    i = 0
    for i in range(0, longitud):
        print(funciones[i].id, funciones[i].type_data)