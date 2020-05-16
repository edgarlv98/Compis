import sys
import ply.lex as lex
import ply.yacc as yacc
import quadruple as quad

success = True
funcionPadreDeVariables = 'global'

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
    'function' : 'FUNCTION',
    'while' : 'WHILE',
    'for' : 'FOR',
    'main' : 'MAIN'
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
    'DOUBLEEQUAL',
    'AND',
    'OR',
    'LPAREN',
    'RPAREN',
    'LBRACE',
    'RBRACE',
    'COMA',
    "SEMICOLON",
    "COLON"
]

# Operadores Aritmeticos
t_PLUS = r'\+'
t_MINUS = r'\-'
t_TIMES = r'\*'
t_DIVIDE = r'\/'

# Operadores de Comparacion
t_EQUAL = r'\='
t_DIFFERENT = r'\[!=]'
t_LOWERTHAN = r'\<'
t_MORETHAN = r'\>'
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
    '''program : PROGRAM ID COLON vars main function
               | PROGRAM ID COLON main function
               | PROGRAM ID COLON vars main
               | PROGRAM ID COLON main
    '''
    if p[4]== 'main':
        pass

def p_main(p):
    '''main : nomMain LPAREN RPAREN LBRACE bloqueAux RBRACE
            | nomMain LPAREN RPAREN LBRACE vars bloqueAux RBRACE
    '''

def p_nomMain(p):
    ''' nomMain : MAIN
    '''
    global funcionPadreDeVariables
    funcionPadreDeVariables = 'main'
    #global direccion_func
    #direccion_func = direccion_func + 1
    directorioFunc.insert(p[1], 'int', direccion_func)

def p_vars(p):
    '''vars : VAR varAux1
    '''

def p_varAux1(p):
    '''varAux1 : tipo varAux2 SEMICOLON
               | tipo varAux2 SEMICOLON varAux1
    '''

def p_varAux2(p):
    '''varAux2 : ID
            | ID COMA varAux2
    '''

    if varsTable.tipo == 'int':
        #global vars_int
        #vars_int = vars_int + 1
        varsTable.insert(p[1], varsTable.tipo, vars_int, funcionPadreDeVariables)
    elif varsTable.tipo == 'char':
        #global vars_char
        #vars_char = vars_char + 1
        varsTable.insert(p[1], varsTable.tipo, vars_char, funcionPadreDeVariables)
    elif varsTable.tipo == 'float':
        #global vars_float
        #vars_float = vars_float + 1
        varsTable.insert(p[1], varsTable.tipo, vars_float, funcionPadreDeVariables)


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

def p_function(p):
    '''function : FUNCTION tipoFunc nomFunc LPAREN RPAREN LBRACE RBRACE
              | FUNCTION tipoFunc nomFunc LPAREN RPAREN LBRACE vars bloqueAux RBRACE
              | FUNCTION tipoFunc nomFunc LPAREN RPAREN LBRACE RBRACE function
              | FUNCTION tipoFunc nomFunc LPAREN RPAREN LBRACE vars bloqueAux RBRACE function
              | FUNCTION tipoFunc nomFunc LPAREN param RPAREN LBRACE RBRACE
              | FUNCTION tipoFunc nomFunc LPAREN param RPAREN LBRACE vars bloqueAux RBRACE
              | FUNCTION tipoFunc nomFunc LPAREN param RPAREN LBRACE RBRACE function
              | FUNCTION tipoFunc nomFunc LPAREN param RPAREN LBRACE vars bloqueAux RBRACE function
    '''

def p_param(p):
    '''param : tipo ID
             | tipo ID COMA param
    '''
    varsTable.insert(p[2], varsTable.tipo, 0, funcionPadreDeVariables)

def p_nomFunc(p):
    '''nomFunc : ID
    '''
    global funcionPadreDeVariables
    funcionPadreDeVariables = p[1]
    #global direccion_func
    #direccion_func = direccion_func + 1
    directorioFunc.insert(p[1], directorioFunc.tipo, direccion_func)

def p_bloqueAux(p):
    '''bloqueAux : estatuto
                 | estatuto bloqueAux
    '''

def p_while(p):
    '''while : WHILE LPAREN expresion RPAREN bloque
    '''

def p_estatuto(p):
    '''estatuto : asignacion
                | condicion
                | escritura
                | while
                | comparacion
    '''

def p_asignacion(p):
    '''asignacion : ID push_id EQUAL push_poper expresion create_asign SEMICOLON
    '''
    varsTable.update(p[1], varsTable.valor)

def p_create_asign(p):
    "create_asign :"
    quad.createQuadAssign()

def p_comparacion(p):
    '''comparacion : ID push_id DOUBLEEQUAL push_poper expresion SEMICOLON
    '''

def p_condicion(p):
    '''condicion : IF LPAREN expresion RPAREN cond bloque SEMICOLON condFinal
                 | IF LPAREN expresion RPAREN cond bloque ELSE condElse bloque SEMICOLON condFinal
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
    '''escritura : PRINT push_poper LPAREN exp RPAREN quad_print SEMICOLON
    '''

def p_quad_print(p):
    "quad_print :"
    quad.createQuadPrint()

def p_escrituraAux(p):
    '''escrituraAux : expresion
                    | CTE_STRING
                    | expresion COMA escrituraAux
                    | CTE_STRING COMA escrituraAux
    '''

def p_expresion(p):
    '''expresion : exp
                 | exp LOWERTHAN push_poper exp quad_comp
                 | exp MORETHAN push_poper exp quad_comp
                 | exp DIFFERENT push_poper exp quad_comp
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
    #print("aqui va el id", p[-1])
    quad.pushID(p[-1])

def p_push_cte(p):
    "push_cte :"
    #print("aqui va la cte", p[-1])
    quad.pushCTE(p[-1])

def p_push_poper(p):
    "push_poper :"
    #print("operadores", p[-1])
    quad.pushPoper(p[-1])

def p_var_cte(p):
    '''var_cte : ID push_id
               | CTE_I push_cte
               | CTE_F push_cte
    '''
    varsTable.valor = p[1]

def p_error(p):
    global success
    success = False
    print("Error en la Sintaxis en '%s" % p.value)
    sys.exit()

parser = yacc.yacc()

archivo = "test.txt"
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

def printTablaDeVariablePorFuncion():
    for x in directorioFunc.funciones:
        x


if success == True:
    #print("Archivo aprobado")
    #print("Funciones")
    #directorioFunc.show()
    #print("Variables")
    #varsTable.show()
    #printGlobal()
    #printTablaDeVariablePorFuncion()
    quad.mostrarSize()
    quad.cuadruplos()
    sys.exit()
else:
    print("Archivo no aprobado")
    sys.exit()
