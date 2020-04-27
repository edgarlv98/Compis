import sys

simbolos = []

tipo = None
Id = None
direccion = None
valor = None

#Objeto tabla variables#
class variable(object):
    def __init__(self, id, tipo, direccion, value=None):
        self.id = str(id)
        self.tipo = str(tipo)
        self.direccion = direccion
        self.value = value

def insert(id, tipo, direccion, funcion):
    temp = variable(id, tipo, direccion)
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
    i = 0
    for i in range(0, longitud):
        print(simbolos[i].id, simbolos[i].tipo, simbolos[i].direccion, simbolos[i].value)