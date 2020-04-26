import sys
import ply.lex as lex
import ply.yacc as yacc

success = True
direccion_func = 1000
vars_int = 2000
vars_char = 2100
vars_float = 2200

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
t_DIFFERENT = r'\[<>]'
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

def p_main(p):
    '''main : MAIN LPAREN RPAREN LBRACE bloqueAux RBRACE
            | MAIN LPAREN RPAREN LBRACE vars bloqueAux RBRACE
    '''

    global direccion_func
    direccion_func = direccion_func + 1
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
        global vars_int
        vars_int = vars_int + 1
        varsTable.insert(p[1], varsTable.tipo, vars_int)
    elif varsTable.tipo == 'char':
        global vars_char
        vars_char = vars_char + 1
        varsTable.insert(p[1], varsTable.tipo, vars_char)
    elif varsTable.tipo == 'float':
        global vars_float
        vars_float = vars_float + 1
        varsTable.insert(p[1], varsTable.tipo, vars_float)


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
    '''function : FUNCTION tipoFunc ID LPAREN RPAREN LBRACE RBRACE
              | FUNCTION tipoFunc ID LPAREN RPAREN LBRACE vars bloqueAux RBRACE
              | FUNCTION tipoFunc ID LPAREN vars RPAREN LBRACE bloqueAux RBRACE
              | FUNCTION tipoFunc ID LPAREN vars RPAREN LBRACE vars bloqueAux RBRACE
              | FUNCTION tipoFunc ID LPAREN RPAREN LBRACE RBRACE function
              | FUNCTION tipoFunc ID LPAREN RPAREN LBRACE vars bloqueAux RBRACE function
              | FUNCTION tipoFunc ID LPAREN vars RPAREN LBRACE bloqueAux RBRACE function
              | FUNCTION tipoFunc ID LPAREN vars RPAREN LBRACE vars bloqueAux RBRACE function
    '''
    global direccion_func
    direccion_func = direccion_func + 1
    directorioFunc.insert(p[3], directorioFunc.tipo, direccion_func)


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
    '''asignacion : ID EQUAL expresion SEMICOLON
    '''
    varsTable.update(p[1], varsTable.valor)

def p_comparacion(p):
    '''comparacion : ID DOUBLEEQUAL expresion SEMICOLON
    '''

def p_condicion(p):
    '''condicion : IF LPAREN expresion RPAREN bloque SEMICOLON
                 | IF LPAREN expresion RPAREN bloque ELSE bloque SEMICOLON
    '''

def p_escritura(p):
    '''escritura : PRINT LPAREN escrituraAux RPAREN SEMICOLON
    '''

def p_escrituraAux(p):
    '''escrituraAux : expresion
                    | CTE_STRING
                    | expresion COMA escrituraAux
                    | CTE_STRING COMA escrituraAux
    '''

def p_expresion(p):
    '''expresion : exp
                 | exp LOWERTHAN exp
                 | exp MORETHAN exp
                 | exp DIFFERENT exp
    '''

def p_exp(p):
    '''exp : termino
           | termino PLUS exp
           | termino MINUS exp
    '''

def p_termino(p):
    '''termino : factor
               | factor TIMES termino
               | factor DIVIDE termino
    '''

def p_factor(p):
    '''factor : LPAREN expresion RPAREN
              | factorAux
    '''

def p_factorAux(p):
    '''factorAux : PLUS var_cte
                 | MINUS var_cte
                 | var_cte
    '''

def p_var_cte(p):
    '''var_cte : ID
               | CTE_I
               | CTE_F
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

if success == True:
    print("Archivo aprobado")
    print("Variables")
    varsTable.show()
    print("Funciones")
    directorioFunc.show()
    sys.exit()
else:
    print("Archivo no aprobado")
    sys.exit()
