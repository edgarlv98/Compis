import sys

simbolos = []

tipo = None
Id = None
valor = None

#Objeto tabla variables#
class tabla(object):
    def __init__(self, id, type_data, value=None):
        self.id = str(id)
        self.type_data = str(type_data)
        self.value = value

def insert(id, type_data):
    temp = tabla(id, type_data)
    if len(simbolos) >= 1 and not repeatID(id):
        simbolos.append(temp)
    if len(simbolos) == 0:
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
        print(simbolos[i].id, simbolos[i].type_data, simbolos[i].value)