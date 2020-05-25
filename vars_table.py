import sys

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
    if (len(simbolos) >= 1 and not repeatID(id)) or len(simbolos) == 0:
        simbolos.append(temp)

def repeatID(id):
    aux = False

    for i in range (len(simbolos)):
        if simbolos[i].id == id:
            aux = True
            print("ERROR: El ID ya existe: ", id)
            sys.exit()
    return aux

def update(id, value):
    for i in range (len(simbolos)):
        if simbolos[i].id == id:
            simbolos[i].value = value

def show():
    longitud = len(simbolos)
    for i in range(0, longitud):
        print(simbolos[i].tipo, simbolos[i].id, simbolos[i].value)