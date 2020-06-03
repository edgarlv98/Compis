import sys
import ply.lex as lex
import ply.yacc as yacc
import quadruple as quad
import maquinaVirtual as virtual
import memoriaPadre

success = True
funcionPadreDeVariables = 'global'
idFuncActual = None
tipoFuncion = None

quadMain = 0

#Direcciones de funciones
direccion_func = 1000

#Direcciones de variables
vars_int = 2000 #variables int
vars_char = 2100 #variables char
vars_float = 2200 #variables float

#Palabras reservadas
reserved = {
    'program' : 'PROGRAM',
    'var' : 'VAR',
    'if' : 'IF' ,
    'else' : 'ELSE',
    'float' : 'FLOAT',
    'int' : 'INT',
    'char' : 'CHAR',
    'void' : 'VOID',
    'print' : 'PRINT',
    'input' : 'INPUT',
    'function' : 'FUNCTION',
    'while' : 'WHILE',
    'from' : 'FROM',
    'do' : 'DO',
    'to' : 'TO',
    'main' : 'MAIN',
    'return' : 'RETURN',
    'break' : 'BREAK'
}

tokens = [
    'ID',
    'CTE_I',
    'CTE_F',
    'CTE_STRING',
    'PLUS',
    'MINUS',
    'TIMES',
    'DIVIDE',
    'EQUAL',
    "DIFFERENT",
    'LOWERTHAN',
    'MORETHAN',
    'LOWEREQUAL',
    'MOREEQUAL',
    'DOUBLEEQUAL',
    'AND',
    'OR',
    'LPAREN',
    'RPAREN',
    'LBRACE',
    'RBRACE',
    'COMA',
    "SEMICOLON",
    "COLON",
    'LCORCH',
    'RCORCH',
    'DETERMINANT',
    'TRANSPUESTA',
    'INVERSA'
]

# Operadores Aritmeticos
t_PLUS = r'\+'
t_MINUS = r'\-'
t_TIMES = r'\*'
t_DIVIDE = r'\/'

# Operadores de Comparacion
t_EQUAL = r'\='
t_DIFFERENT = r'\!='
t_LOWERTHAN = r'\<'
t_MORETHAN = r'\>'
t_LOWEREQUAL = r'\<='
t_MOREEQUAL = r'\=>'
t_DOUBLEEQUAL = r'\=='
t_AND = r'\&'
t_OR = r'\|'

# Simbolos
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_LBRACE = r'\{'
t_RBRACE = r'\}'
t_COMA = r'\,'
t_SEMICOLON = r'\;'
t_COLON = r'\:'
t_LCORCH = r'\['
t_RCORCH = r'\]'

# Caracteres especiales para operaciones especiales
t_DETERMINANT = r'\$'
t_TRANSPUESTA = r'\!' # No funciona con el otro signo
t_INVERSA = r'\?'

# Constantes
t_CTE_I = r'[0-9]+'
t_CTE_F = r'[0-9]+\.[0-9]+'
t_CTE_STRING = r'\"([^\\\n]|(\\.))*?\"'

# Caracteres ignorados
t_ignore = ' \t\n'

tokens = tokens + list(reserved.values())

# Definicion de ID
def t_ID(t):
    r'[a-zA-Z][a-zA-Z0-9]*'
    t.type = reserved.get(t.value,'ID')
    return t

def t_COMMENTS(t):
    r'%{2,}.*'
    pass

# Errores
def t_error(t):
    global success
    success = False
    print("Caracter ilegal '%s'" % t.value[0])
    t.lexer.skip(1)

lexer = lex.lex()

# GRAMATICA #
import vars_table as varsTable
import directorio_funciones as directorioFunc

def p_program(p):
    '''program : PROGRAM ID COLON varsGlobal function main endPrograma
               | PROGRAM ID COLON function main endPrograma
               | PROGRAM ID COLON varsGlobal main endPrograma
               | PROGRAM ID COLON main endPrograma
    '''
    if p[4]== 'main':
        pass

def p_endPrograma(p):
    "endPrograma :"
    quad.endPrograma()


def p_varsGlobal(p):
    '''varsGlobal : VAR varAuxGlobal1
    '''

def p_varAuxGlobal1(p):
    '''varAuxGlobal1 : tipo varAuxGlobal2 SEMICOLON
                     | tipo varAuxGlobal2 SEMICOLON varAuxGlobal1
    '''

def p_varAuxGlobal2(p):
    '''varAuxGlobal2 : ID
                     | ID COMA varAuxGlobal2
                     | ID LCORCH CTE_I RCORCH
                     | ID LCORCH CTE_I RCORCH COMA varAuxGlobal2
                     | ID LCORCH CTE_I RCORCH LCORCH CTE_I RCORCH
                     | ID LCORCH CTE_I RCORCH LCORCH CTE_I RCORCH COMA varAuxGlobal2
    '''
    tipo = varsTable.tipo
    direccion = memoriaPadre.memoria_local[0].getDirVarGlobal(tipo)
    memoriaPadre.memoria_local[0].updateGlobalVariable(None, direccion, tipo)
    varsTable.insert(p[1], tipo, direccion, funcionPadreDeVariables)

def p_main(p):
    '''main : nomMain LPAREN RPAREN LBRACE bloqueAux RBRACE
            | nomMain LPAREN RPAREN LBRACE vars bloqueAux RBRACE
            | nomMain LPAREN RPAREN LBRACE llamadaAFuncion RBRACE
    '''

def p_nomMain(p):
    ''' nomMain : MAIN
    '''
    global funcionPadreDeVariables
    funcionPadreDeVariables = 'main'
    direccion = memoriaPadre.memoria_local[0].getDirFuncion('int')
    directorioFunc.insert(p[1], 'int', len(quad.Quad), direccion)
    global quadMain
    quadMain = len(quad.Quad) - 1

def p_vars(p):
    '''vars : VAR varAux1
    '''

def p_varAux1(p):
    '''varAux1 : tipo varAux2 SEMICOLON
               | tipo varAux2 SEMICOLON varAux1
    '''

def p_varAux2(p):
    '''varAux2 : ID push_var
            | ID push_var COMA varAux2
            | ID LCORCH CTE_I RCORCH push_arreglo
            | ID LCORCH CTE_I RCORCH push_arreglo COMA varAux2
            | ID LCORCH CTE_I RCORCH LCORCH CTE_I RCORCH push_matriz
            | ID LCORCH CTE_I RCORCH LCORCH CTE_I RCORCH push_matriz COMA varAux2
    '''

def p_pushVariable(p):
    "push_var :"
    tipo = varsTable.tipo
    direccion = memoriaPadre.memoria_local[0].getDirvariableLocal(tipo)
    varsTable.insert(p[-1], tipo, direccion, funcionPadreDeVariables)

def p_arreglo(p):
    "push_arreglo :"
    varsTable.esArreglo = True
    tipo = varsTable.tipo
    dimension = int(p[-2])
    i = 0
    while(i < dimension):
        direccion = memoriaPadre.memoria_local[0].getDirvariableLocal(tipo)
        varsTable.insertDimensionada(p[-4], tipo, direccion, funcionPadreDeVariables, dimension)
        i = i + 1

def p_matriz(p):
    "push_matriz :"
    varsTable.esArreglo = True
    dim1 = int(p[-5])
    dim2 = int(p[-2])
    dimension = dim1 * dim2
    valor = (p[-5], p[-2])
    tipo = varsTable.tipo
    i = 0
    while(i < dimension):
        direccion = memoriaPadre.memoria_local[0].getDirvariableLocal(tipo)
        varsTable.insertDimensionada(p[-7], tipo, direccion, funcionPadreDeVariables, valor)
        i = i + 1
        

def p_tipo(p):
    '''tipo : INT
            | FLOAT
            | CHAR
    '''
    varsTable.tipo = p[1]

def p_tipoFunc(p):
    '''tipoFunc : INT
            | FLOAT
            | CHAR
            | VOID
    '''
    directorioFunc.tipo = p[1]

def p_bloque(p):
    '''bloque : LBRACE RBRACE
              | LBRACE bloqueAux RBRACE
    '''

boolNeedsReturn = False

def p_function(p):
    '''function : FUNCTION tipoFunc nomFunc LPAREN RPAREN LBRACE functionReturn RBRACE endProc
              | FUNCTION tipoFunc nomFunc LPAREN RPAREN LBRACE vars bloqueAux functionReturn RBRACE endProc
              | FUNCTION tipoFunc nomFunc LPAREN RPAREN LBRACE functionReturn RBRACE endProc function 
              | FUNCTION tipoFunc nomFunc LPAREN RPAREN LBRACE vars bloqueAux functionReturn RBRACE endProc function
              | FUNCTION tipoFunc nomFunc LPAREN RPAREN LBRACE bloqueAux functionReturn RBRACE endProc
              | FUNCTION tipoFunc nomFunc LPAREN RPAREN LBRACE bloqueAux functionReturn RBRACE endProc function
              | FUNCTION tipoFunc nomFunc LPAREN param RPAREN LBRACE functionReturn RBRACE endProc 
              | FUNCTION tipoFunc nomFunc LPAREN param RPAREN LBRACE bloqueAux functionReturn RBRACE endProc
              | FUNCTION tipoFunc nomFunc LPAREN param RPAREN LBRACE bloqueAux functionReturn RBRACE endProc function
              | FUNCTION tipoFunc nomFunc LPAREN param RPAREN LBRACE vars bloqueAux functionReturn RBRACE endProc
              | FUNCTION tipoFunc nomFunc LPAREN param RPAREN LBRACE functionReturn RBRACE endProc function
              | FUNCTION tipoFunc nomFunc LPAREN param RPAREN LBRACE vars bloqueAux functionReturn RBRACE endProc function
    '''

def p_functionReturn(p):
    '''functionReturn : RETURN exp creaCuadReturn SEMICOLON
                    | empty
    '''

def p_creaCuadReturn(p):
    '''creaCuadReturn :
    '''
    quad.createQuadReturn(funcionPadreDeVariables)

def p_endProc(p):
    '''endProc :
    '''
    quad.endproc()

def p_param(p):
    '''param : tipo ID paramAvarTable
             | tipo ID paramAvarTable COMA param
             | empty
    '''


def p_paramAvarTable(p):
    'paramAvarTable : '
    tipo = varsTable.tipo
    direccion = memoriaPadre.memoria_local[0].getDirvariableLocal(tipo)
    varsTable.insert(p[-1], tipo, direccion, funcionPadreDeVariables)

def p_empty(p):
    '''empty : 
    '''

def p_push_function(p):
    "push_function :"
    if(directorioFunc.tipo != 'void'):
        tipo = directorioFunc.tipo
        direccion = memoriaPadre.memoria_local[0].getDirVarGlobal(tipo)
        memoriaPadre.memoria_local[0].updateGlobalVariable(None, direccion, tipo)
        varsTable.insert(p[-1], tipo, direccion, 'global')


def p_nomFunc(p):
    '''nomFunc : ID push_function
    '''
    global funcionPadreDeVariables
    funcionPadreDeVariables = p[1]
    tipo = directorioFunc.tipo
    direccion = memoriaPadre.memoria_local[0].getDirFuncion(tipo)
    directorioFunc.insert(p[1], tipo, len(quad.Quad), direccion)

def p_bloqueAux(p):
    '''bloqueAux : estatuto
                 | estatuto bloqueAux
    '''

def p_while(p):
    '''while : WHILE while1 LPAREN expresion RPAREN while2 LBRACE bloqueAux RBRACE while3
    '''

def p_while1(p):
    "while1 :"
    quad.while1()

def p_while2(p):
    "while2 :"
    quad.while2()

def p_while3(p):
    "while3 :"
    quad.while3()

def p_loopFromDo(p):
    '''loopFromDo : FROM LPAREN ID EQUAL expresion RPAREN TO LPAREN expresion RPAREN DO LBRACE bloqueAux RBRACE
    '''

#def p_loop1(p):
#    "loop1 :"
#    quad.loop1()
#
#def p_loop2(p):
#    "loop2 :"
#    quad.loop2()

def p_estatuto(p):
    '''estatuto : asignacion
                | condicion
                | escritura
                | while
                | loopFromDo
                | comparacion
                | llamadaAFuncion SEMICOLON
                | lectura
                | BREAK generaCuadbreak SEMICOLON
                | transpuesta
                | inversa
    '''

def p_transpuesta(p):
    '''transpuesta : ID push_id TRANSPUESTA creaTrans SEMICOLON
    '''
def p_inversa(p):
    '''inversa : ID push_id INVERSA creaInversa SEMICOLON
    '''

def p_creaInversa(p):
    "creaInversa : "
    quad.creaInversa( p[-3], funcionPadreDeVariables)

def p_creaTrans(p):
    "creaTrans : "
    quad.creaTrans( p[-3], funcionPadreDeVariables)

def p_generaCuadbreak(p):
    "generaCuadbreak : "
    quad.breakk()

def p_llamadaAFuncion(p):
    '''llamadaAFuncion : ID actualizaFuncion generarEra LPAREN paramFuncion gosub RPAREN expresion
                       | ID actualizaFuncion generarEra LPAREN paramFuncion gosub RPAREN
    '''
    
def p_actualizaFuncion(p):
    'actualizaFuncion : '
    global idFuncActual
    idFuncActual = p[-1]

def p_gosub(p):
    '''gosub :
    '''
    for x in directorioFunc.funciones:
        if x.id == idFuncActual:
            if p[-5] == 'void':
                for y in varsTable.simbolos:
                    if y.funcion == x.id:
                        quad.moduloSeis(x.id, x.alcance, y.direccion)
                        break
            else:
                quad.moduloSeis(x.id, x.alcance, 0)
def p_generarEra(p):
    '''generarEra :
    '''
    for x in directorioFunc.funciones:
        if x.id == p[-2]:
            quad.moduloDos(x.direccion)
            break

def p_paramFuncion(p):
    '''paramFuncion : ID push_id2 paramFuncionAux
                     | ID push_id2 paramFuncionAux COMA paramFuncion
                     | exp paramFuncionAux
                     | exp paramFuncionAux COMA paramFuncion
                     | empty
    '''

def p_paramFuncionAux(p):
    "paramFuncionAux : "
    quad.moduloTres()

def p_push_id2(p):
    "push_id2 :"
    quad.pushID(p[-1], funcionPadreDeVariables)

def p_array(p):
    '''arreglo : ID push_id LCORCH exp RCORCH ver_dim1
    '''

def p_matrix(p):
    ''' matrix : ID push_id LCORCH exp RCORCH LCORCH exp RCORCH ver_dim2
    '''

def p_ver_dim2(p):
    " ver_dim2 : "
    quad.verificaDim2(p[-8], funcionPadreDeVariables)

def p_asignacion(p):
    '''asignacion : ID push_id EQUAL push_poper expresion create_asign SEMICOLON
                  | arreglo EQUAL push_poper exp create_asign SEMICOLON
                  | matrix EQUAL push_poper exp create_asign SEMICOLON
                  | ID push_id EQUAL push_poper llamadaAFuncion create_asign SEMICOLON
                  | ID push_id EQUAL push_poper determinante SEMICOLON
    '''

def p_determinante(p):
    '''determinante : ID push_id DETERMINANT
    '''
    quad.determinante(p[1], p[-4], funcionPadreDeVariables)

def p_push_id_dimensionada(p):
    "push_id_dimensionada :"

def p_create_asign_dim(p):
    "create_asign_dim :"
    quad.asignacionDimensionada()

def p_ver_dim1(p):
    "ver_dim1 :"
    quad.verificaDim(p[-5], funcionPadreDeVariables)

def p_create_asign(p):
    "create_asign :"
    quad.createQuadAssign()

def p_comparacion(p):
    '''comparacion : ID push_id DOUBLEEQUAL push_poper expresion SEMICOLON
    '''

def p_condicion(p):
    '''condicion : IF LPAREN expresion RPAREN cond bloque condFinal
                 | IF LPAREN expresion RPAREN cond bloque ELSE condElse bloque condFinal
    '''

def p_quad_cond(p):
    "cond :"
    quad.createQuadCond()

def p_quad_condElse(p):
    "condElse :"
    quad.updateQuadCondIfElseJump()

def p_quad_condFinal(p):
    "condFinal :"
    quad.updateQuadCondIFJump()

def p_escritura(p):
    '''escritura : PRINT push_poper LPAREN escrituraAux RPAREN quad_print SEMICOLON
                | PRINT push_poper LPAREN llamadaAFuncion RPAREN quad_print SEMICOLON
    '''

def p_lectura(p):
    '''lectura : INPUT push_poper LPAREN ID push_id RPAREN quad_print SEMICOLON
    '''

def p_quad_print(p):
    "quad_print :"
    quad.createQuadPrint()

def p_escrituraAux(p):
    '''escrituraAux : expresion
                    | CTE_STRING push_cte
                    | expresion COMA escrituraAux
                    | CTE_STRING push_cte COMA escrituraAux
                    | llamadaAFuncion
    '''

def p_expresion(p):
    '''expresion : exp
                 | exp comp exp quad_comp
    '''

def p_comp(p):
    '''comp : LOWERTHAN push_poper
            | MORETHAN push_poper
            | DIFFERENT push_poper
            | DOUBLEEQUAL push_poper
            | LOWEREQUAL push_poper
            | MOREEQUAL push_poper
    '''

def p_quad_comp(p):
    "quad_comp :"
    quad.createQuadComp()

def p_exp(p):
    '''exp : termino quad_term
           | termino quad_term exp1
    '''

def p_exp1(p):
    '''exp1 : PLUS push_poper exp
            | MINUS push_poper exp
    '''

def p_quad_term(p):
    "quad_term :"
    quad.createQuadTerm()

def p_quad_fact(p):
    "quad_fact :"
    quad.createQuadFact()

def p_termino(p):
    '''termino : factor quad_fact
               | factor quad_fact termino1
    '''

def p_termino1(p):
    '''termino1 : TIMES push_poper termino
                | DIVIDE push_poper termino
    '''

def p_factor(p):
    '''factor : LPAREN expresion RPAREN
              | factorAux
    '''

def p_factorAux(p):
    '''factorAux : PLUS push_poper var_cte
                 | MINUS push_poper var_cte
                 | var_cte 
    '''

def p_push_id(p):
    "push_id :"
    quad.pushID(p[-1], funcionPadreDeVariables)

def p_push_cte(p):
    "push_cte :"
    tipo = memoriaPadre.memoria_local[0].getTipoCte(p[-1])
    repeat = memoriaPadre.memoria_local[0].repeatCte(p[-1])
    if(repeat == False):
        direccion = memoriaPadre.memoria_local[0].getDirCte(tipo)
        memoriaPadre.memoria_local[0].updateCte(p[-1], direccion, tipo)
    direccion = memoriaPadre.memoria_local[0].getDirRepeatCte(p[-1])
    quad.pushCTE(p[-1], direccion)

def p_push_poper(p):
    "push_poper :"
    quad.pushPoper(p[-1])

def p_var_cte(p):
    '''var_cte : ID push_id
               | CTE_I push_cte
               | CTE_F push_cte
               | CTE_STRING push_cte
               | arreglo
               | matrix
    '''
    varsTable.valor = p[1]

def p_error(p):
    global success
    success = False
    print("Error en la Sintaxis en '%s" % p.value)
    sys.exit()

def funcionDos(id):
    quad.moduloDos(id)


parser = yacc.yacc()

archivo = "fibonacci.txt"
f = open(archivo, 'r')
s = f.read()

parser.parse(s)

#variablesGlobales
varsTableGlobal = []
for x in varsTable.simbolos:
    if(x.funcion == 'global'):
        varsTableGlobal.append(x)
    elif(x.funcion != 'global'):
        break

#variablesPorFuncion
varsTableAux = []
auxInt = 0
for x in varsTable.simbolos:
    if x.funcion == directorioFunc.funciones[auxInt].id:
        varsTableAux.append(directorioFunc.funciones[auxInt])
    elif x.funcion != directorioFunc.funciones[auxInt].id and auxInt + 1 < len(directorioFunc.funciones):
        directorioFunc.funciones[auxInt].variables = varsTableAux
        auxInt = 1 + auxInt
        varsTableAux = []
    else:
        break

def printGlobal():
    for x in varsTableGlobal:
        print(x.id)


if success == True:
    #print("Archivo aprobado")
    #print("Variables")
    #varsTable.show()
    #printGlobal()
    #printTablaDeVariablePorFuncion()
    #quad.mostrarSize()
    
    #quad.cuadruplos()
    #memoriaPadre.memoria_local[0].show()
    virtual.inicio(quadMain)
    #memoriaPadre.memoria_local[0].show()
    #varsTable.show()
    #directorioFunc.show()
    #quad.mostraPilaDim()
    sys.exit()
else:
    print("Archivo no aprobado")
    sys.exit()
