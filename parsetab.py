
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'AND CHAR COLON COMA CTE_F CTE_I CTE_STRING DIFFERENT DIVIDE DO DOUBLEEQUAL ELSE EQUAL FLOAT FROM FUNCTION ID IF INT LBRACE LOWERTHAN LPAREN MAIN MINUS MORETHAN OR PLUS PRINT PROGRAM RBRACE RPAREN SEMICOLON TIMES TO VAR VOID WHILEprogram : PROGRAM ID COLON vars main function\n               | PROGRAM ID COLON main function\n               | PROGRAM ID COLON vars main\n               | PROGRAM ID COLON main\n    main : nomMain LPAREN RPAREN LBRACE bloqueAux RBRACE\n            | nomMain LPAREN RPAREN LBRACE vars bloqueAux RBRACE\n     nomMain : MAIN\n    vars : VAR varAux1\n    varAux1 : tipo varAux2 SEMICOLON\n               | tipo varAux2 SEMICOLON varAux1\n    varAux2 : ID\n            | ID COMA varAux2\n    tipo : INT\n            | FLOAT\n            | CHAR\n    tipoFunc : INT\n            | FLOAT\n            | CHAR\n            | VOID\n    bloque : LBRACE RBRACE\n              | LBRACE bloqueAux RBRACE\n    function : FUNCTION tipoFunc nomFunc LPAREN RPAREN LBRACE RBRACE \n              | FUNCTION tipoFunc nomFunc LPAREN  RPAREN LBRACE vars bloqueAux RBRACE\n              | FUNCTION tipoFunc nomFunc LPAREN RPAREN LBRACE RBRACE function \n              | FUNCTION tipoFunc nomFunc LPAREN RPAREN LBRACE vars bloqueAux RBRACE function\n              | FUNCTION tipoFunc nomFunc LPAREN param RPAREN LBRACE RBRACE\n              | FUNCTION tipoFunc nomFunc LPAREN param RPAREN LBRACE vars bloqueAux RBRACE\n              | FUNCTION tipoFunc nomFunc LPAREN param RPAREN LBRACE RBRACE function\n              | FUNCTION tipoFunc nomFunc LPAREN param RPAREN LBRACE vars bloqueAux RBRACE function\n    param : tipo ID \n             | tipo ID COMA param\n             | empty\n    empty : \n    nomFunc : ID\n    bloqueAux : estatuto\n                 | estatuto bloqueAux\n    while : WHILE while1 LPAREN expresion RPAREN while2 LBRACE bloqueAux RBRACE while3\n    while1 :while2 :while3 :loopFromDo : FROM LPAREN ID EQUAL expresion RPAREN TO LPAREN expresion RPAREN DO LBRACE bloqueAux RBRACE\n    estatuto : asignacion\n                | condicion\n                | escritura\n                | while\n                | loopFromDo\n                | comparacion\n                | llamadaAFuncion\n    llamadaAFuncion : ID generarEra LPAREN paramFuncion gosub endProc RPAREN expresion\n                        | ID generarEra LPAREN paramFuncion gosub endProc RPAREN SEMICOLON\n    endProc :\n    gosub :\n    generarEra :\n    paramFuncion : ID  push_id \n                     | ID push_id COMA paramFuncion\n                     | expresion\n                     | expresion COMA paramFuncion\n                     | empty\n    asignacion : ID push_id EQUAL push_poper expresion create_asign SEMICOLON\n    create_asign :comparacion : ID push_id DOUBLEEQUAL push_poper expresion SEMICOLON\n    condicion : IF LPAREN expresion RPAREN cond bloque condFinal\n                 | IF LPAREN expresion RPAREN cond bloque ELSE condElse bloque condFinal\n    cond :condElse :condFinal :escritura : PRINT push_poper LPAREN escrituraAux RPAREN quad_print SEMICOLON\n    quad_print :escrituraAux : expresion\n                    | CTE_STRING\n                    | expresion COMA escrituraAux\n                    | CTE_STRING COMA escrituraAux\n                    | llamadaAFuncion\n    expresion : exp\n                 | exp comp exp quad_comp\n    comp : LOWERTHAN push_poper\n            | MORETHAN push_poper\n            | DIFFERENT push_poper\n            | DOUBLEEQUAL push_poper\n    quad_comp :exp : termino quad_term\n           | termino quad_term exp1\n    exp1 : PLUS push_poper exp\n            | MINUS push_poper exp\n    quad_term :quad_fact :termino : factor quad_fact\n               | factor quad_fact termino1\n    termino1 : TIMES push_poper termino\n                | DIVIDE push_poper termino\n    factor : LPAREN expresion RPAREN\n              | factorAux\n    factorAux : PLUS push_poper var_cte\n                 | MINUS push_poper var_cte\n                 | var_cte \n    push_id :push_cte :push_poper :var_cte : ID push_id\n               | CTE_I push_cte\n               | CTE_F push_cte\n    '
    
_lr_action_items = {'CTE_STRING':([65,117,118,],[86,86,86,]),'DO':([194,],[196,]),'VOID':([18,],[24,]),'EQUAL':([38,55,81,],[-96,79,111,]),'CHAR':([8,18,29,50,116,],[12,26,12,12,12,]),'VAR':([4,28,83,115,],[8,8,8,8,]),'WHILE':([16,28,29,33,35,37,39,40,42,45,46,47,48,66,67,70,71,72,74,76,77,91,94,95,96,98,114,120,123,124,126,128,133,145,154,155,156,157,167,168,169,170,171,172,174,176,180,183,185,186,190,192,193,195,197,199,],[-8,43,-9,43,43,-43,-46,-48,-42,-45,-47,-44,-10,-95,-85,-86,-97,-97,-96,-74,-92,-81,-87,-101,-100,-99,43,-82,-94,-93,-88,-91,-80,43,43,-66,-75,-61,-67,-83,-84,-90,-89,-20,-62,-59,43,-21,-50,-49,-66,-40,-63,-37,43,-41,]),'PROGRAM':([0,],[2,]),'PRINT':([16,28,29,33,35,37,39,40,42,45,46,47,48,66,67,70,71,72,74,76,77,91,94,95,96,98,114,120,123,124,126,128,133,145,154,155,156,157,167,168,169,170,171,172,174,176,180,183,185,186,190,192,193,195,197,199,],[-8,34,-9,34,34,-43,-46,-48,-42,-45,-47,-44,-10,-95,-85,-86,-97,-97,-96,-74,-92,-81,-87,-101,-100,-99,34,-82,-94,-93,-88,-91,-80,34,34,-66,-75,-61,-67,-83,-84,-90,-89,-20,-62,-59,34,-21,-50,-49,-66,-40,-63,-37,34,-41,]),'MORETHAN':([66,67,70,71,72,74,76,77,88,91,94,95,96,98,109,120,123,124,126,128,138,168,169,170,171,],[-95,-85,-86,-97,-97,-96,104,-92,-96,-81,-87,-101,-100,-99,-96,-82,-94,-93,-88,-91,-99,-83,-84,-90,-89,]),'MINUS':([54,65,66,67,70,71,72,73,74,77,78,79,80,82,88,91,94,95,96,98,100,101,102,103,104,105,106,109,111,117,118,121,122,123,124,125,126,127,128,130,131,132,134,138,139,150,151,152,153,160,170,171,177,187,],[68,68,-95,-85,-86,-97,-97,68,-96,-92,-98,-98,68,68,-96,122,-87,-101,-100,-99,-98,-98,-98,68,-98,68,68,-96,68,68,68,-98,-98,-94,-93,-98,-88,-98,-91,-78,-79,-76,-77,-99,68,68,68,68,68,68,-90,-89,68,68,]),'DIVIDE':([66,70,71,72,74,77,88,94,95,96,98,109,123,124,128,138,],[-95,-86,-97,-97,-96,-92,-96,125,-101,-100,-99,-96,-94,-93,-91,-99,]),'RPAREN':([11,50,61,62,66,67,70,71,72,74,75,76,77,80,85,86,87,88,89,90,91,94,95,96,97,98,107,108,109,110,112,116,120,123,124,126,128,133,137,138,139,140,146,147,148,156,159,160,161,168,169,170,171,178,185,186,191,],[20,60,84,-32,-95,-85,-86,-97,-97,-96,99,-74,-92,-33,-30,-70,-69,-96,119,-73,-81,-87,-101,-100,128,-99,-52,-58,-96,-56,141,-33,-82,-94,-93,-88,-91,-80,-51,-54,-33,162,-31,-72,-71,-75,177,-33,-57,-83,-84,-90,-89,-55,-50,-49,194,]),'SEMICOLON':([21,22,49,66,67,70,71,72,74,76,77,91,94,95,96,98,119,120,123,124,126,128,133,135,136,149,156,158,168,169,170,171,177,],[29,-11,-12,-95,-85,-86,-97,-97,-96,-74,-92,-81,-87,-101,-100,-99,-68,-82,-94,-93,-88,-91,-80,157,-60,167,-75,176,-83,-84,-90,-89,185,]),'LOWERTHAN':([66,67,70,71,72,74,76,77,88,91,94,95,96,98,109,120,123,124,126,128,138,168,169,170,171,],[-95,-85,-86,-97,-97,-96,102,-92,-96,-81,-87,-101,-100,-99,-96,-82,-94,-93,-88,-91,-99,-83,-84,-90,-89,]),'TO':([162,],[179,]),'COLON':([3,],[4,]),'CTE_I':([54,65,68,69,73,78,79,80,82,92,93,100,101,102,103,104,105,106,111,117,118,121,122,125,127,130,131,132,134,139,150,151,152,153,160,177,187,],[72,72,-98,-98,72,-98,-98,72,72,72,72,-98,-98,-98,72,-98,72,72,72,72,72,-98,-98,-98,-98,-78,-79,-76,-77,72,72,72,72,72,72,72,72,]),'CTE_F':([54,65,68,69,73,78,79,80,82,92,93,100,101,102,103,104,105,106,111,117,118,121,122,125,127,130,131,132,134,139,150,151,152,153,160,177,187,],[71,71,-98,-98,71,-98,-98,71,71,71,71,-98,-98,-98,71,-98,71,71,71,71,71,-98,-98,-98,-98,-78,-79,-76,-77,71,71,71,71,71,71,71,71,]),'PLUS':([54,65,66,67,70,71,72,73,74,77,78,79,80,82,88,91,94,95,96,98,100,101,102,103,104,105,106,109,111,117,118,121,122,123,124,125,126,127,128,130,131,132,134,138,139,150,151,152,153,160,170,171,177,187,],[69,69,-95,-85,-86,-97,-97,69,-96,-92,-98,-98,69,69,-96,121,-87,-101,-100,-99,-98,-98,-98,69,-98,69,69,-96,69,69,69,-98,-98,-94,-93,-98,-88,-98,-91,-78,-79,-76,-77,-99,69,69,69,69,69,69,-90,-89,69,69,]),'$end':([1,9,10,17,19,59,64,113,142,144,164,165,181,182,189,],[0,-4,-3,-2,-1,-5,-6,-22,-24,-26,-23,-28,-25,-27,-29,]),'FUNCTION':([9,10,59,64,113,144,164,182,],[18,18,-5,-6,18,18,18,18,]),'DIFFERENT':([66,67,70,71,72,74,76,77,88,91,94,95,96,98,109,120,123,124,126,128,138,168,169,170,171,],[-95,-85,-86,-97,-97,-96,100,-92,-96,-81,-87,-101,-100,-99,-96,-82,-94,-93,-88,-91,-99,-83,-84,-90,-89,]),'RBRACE':([35,37,39,40,42,44,45,46,47,51,53,66,67,70,71,72,74,76,77,83,91,94,95,96,98,115,120,123,124,126,128,133,143,154,155,156,157,166,167,168,169,170,171,172,173,174,176,183,185,186,188,190,192,193,195,198,199,],[-35,-43,-46,-48,-42,59,-45,-47,-44,64,-36,-95,-85,-86,-97,-97,-96,-74,-92,113,-81,-87,-101,-100,-99,144,-82,-94,-93,-88,-91,-80,164,172,-66,-75,-61,182,-67,-83,-84,-90,-89,-20,183,-62,-59,-21,-50,-49,192,-66,-40,-63,-37,199,-41,]),'DOUBLEEQUAL':([38,55,66,67,70,71,72,74,76,77,88,91,94,95,96,98,109,120,123,124,126,128,138,168,169,170,171,],[-96,78,-95,-85,-86,-97,-97,-96,101,-92,-96,-81,-87,-101,-100,-99,-96,-82,-94,-93,-88,-91,-99,-83,-84,-90,-89,]),'TIMES':([66,70,71,72,74,77,88,94,95,96,98,109,123,124,128,138,],[-95,-86,-97,-97,-96,-92,-96,127,-101,-100,-99,-96,-94,-93,-91,-99,]),'LPAREN':([6,7,31,32,34,36,38,41,43,52,54,56,58,65,73,78,79,80,82,88,100,101,102,103,104,105,106,111,117,118,121,122,125,127,130,131,132,134,139,150,151,152,153,160,177,179,187,],[-7,11,50,-34,-98,54,-53,57,-38,65,73,80,82,73,73,-98,-98,73,73,-53,-98,-98,-98,73,-98,73,73,73,73,73,-98,-98,-98,-98,-78,-79,-76,-77,73,73,73,73,73,73,73,187,73,]),'COMA':([22,66,67,70,71,72,74,76,77,85,86,87,88,91,94,95,96,98,109,110,120,123,124,126,128,133,138,156,168,169,170,171,],[30,-95,-85,-86,-97,-97,-96,-74,-92,116,117,118,-96,-81,-87,-101,-100,-99,-96,139,-82,-94,-93,-88,-91,-80,160,-75,-83,-84,-90,-89,]),'ELSE':([155,172,183,],[175,-20,-21,]),'ID':([2,12,13,14,15,16,23,24,25,26,27,28,29,30,33,35,37,39,40,42,45,46,47,48,54,57,63,65,66,67,68,69,70,71,72,73,74,76,77,78,79,80,82,91,92,93,94,95,96,98,100,101,102,103,104,105,106,111,114,117,118,120,121,122,123,124,125,126,127,128,130,131,132,133,134,139,145,150,151,152,153,154,155,156,157,160,167,168,169,170,171,172,174,176,177,180,183,185,186,187,190,192,193,195,197,199,],[3,-15,22,-13,-14,-8,-16,-19,-17,-18,32,38,-9,22,38,38,-43,-46,-48,-42,-45,-47,-44,-10,74,81,85,88,-95,-85,-98,-98,-86,-97,-97,74,-96,-74,-92,-98,-98,109,74,-81,74,74,-87,-101,-100,-99,-98,-98,-98,74,-98,74,74,74,38,88,88,-82,-98,-98,-94,-93,-98,-88,-98,-91,-78,-79,-76,-80,-77,109,38,74,74,74,74,38,-66,-75,-61,109,-67,-83,-84,-90,-89,-20,-62,-59,74,38,-21,-50,-49,74,-66,-40,-63,-37,38,-41,]),'IF':([16,28,29,33,35,37,39,40,42,45,46,47,48,66,67,70,71,72,74,76,77,91,94,95,96,98,114,120,123,124,126,128,133,145,154,155,156,157,167,168,169,170,171,172,174,176,180,183,185,186,190,192,193,195,197,199,],[-8,36,-9,36,36,-43,-46,-48,-42,-45,-47,-44,-10,-95,-85,-86,-97,-97,-96,-74,-92,-81,-87,-101,-100,-99,36,-82,-94,-93,-88,-91,-80,36,36,-66,-75,-61,-67,-83,-84,-90,-89,-20,-62,-59,36,-21,-50,-49,-66,-40,-63,-37,36,-41,]),'LBRACE':([20,60,84,99,129,141,163,175,184,196,],[28,83,115,-64,154,-39,180,-65,154,197,]),'FROM':([16,28,29,33,35,37,39,40,42,45,46,47,48,66,67,70,71,72,74,76,77,91,94,95,96,98,114,120,123,124,126,128,133,145,154,155,156,157,167,168,169,170,171,172,174,176,180,183,185,186,190,192,193,195,197,199,],[-8,41,-9,41,41,-43,-46,-48,-42,-45,-47,-44,-10,-95,-85,-86,-97,-97,-96,-74,-92,-81,-87,-101,-100,-99,41,-82,-94,-93,-88,-91,-80,41,41,-66,-75,-61,-67,-83,-84,-90,-89,-20,-62,-59,41,-21,-50,-49,-66,-40,-63,-37,41,-41,]),'INT':([8,18,29,50,116,],[14,23,14,14,14,]),'FLOAT':([8,18,29,50,116,],[15,25,15,15,15,]),'MAIN':([4,5,16,29,48,],[6,6,-8,-9,-10,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'quad_fact':([70,],[94,]),'vars':([4,28,83,115,],[5,33,114,145,]),'condFinal':([155,190,],[174,193,]),'paramFuncion':([80,139,160,],[107,161,178,]),'endProc':([137,],[159,]),'var_cte':([54,65,73,80,82,92,93,103,105,106,111,117,118,139,150,151,152,153,160,177,187,],[66,66,66,66,66,123,124,66,66,66,66,66,66,66,66,66,66,66,66,66,66,]),'while3':([192,],[195,]),'while2':([141,],[163,]),'nomMain':([4,5,],[7,7,]),'cond':([99,],[129,]),'termino':([54,65,73,80,82,103,105,106,111,117,118,139,150,151,152,153,160,177,187,],[67,67,67,67,67,67,67,67,67,67,67,67,67,67,170,171,67,67,67,]),'create_asign':([136,],[158,]),'tipoFunc':([18,],[27,]),'bloque':([129,184,],[155,190,]),'push_id':([38,74,88,109,],[55,98,98,138,]),'quad_print':([119,],[149,]),'tipo':([8,29,50,116,],[13,13,63,63,]),'exp1':([91,],[120,]),'estatuto':([28,33,35,114,145,154,180,197,],[35,35,35,35,35,35,35,35,]),'param':([50,116,],[61,146,]),'varAux2':([13,30,],[21,49,]),'program':([0,],[1,]),'varAux1':([8,29,],[16,48,]),'factor':([54,65,73,80,82,103,105,106,111,117,118,139,150,151,152,153,160,177,187,],[70,70,70,70,70,70,70,70,70,70,70,70,70,70,70,70,70,70,70,]),'main':([4,5,],[9,10,]),'empty':([50,80,116,139,160,],[62,108,62,108,108,]),'function':([9,10,113,144,164,182,],[17,19,142,165,181,189,]),'escrituraAux':([65,117,118,],[89,147,148,]),'push_poper':([34,68,69,78,79,100,101,102,104,121,122,125,127,],[52,92,93,105,106,130,131,132,134,150,151,152,153,]),'comp':([76,],[103,]),'condElse':([175,],[184,]),'condicion':([28,33,35,114,145,154,180,197,],[37,37,37,37,37,37,37,37,]),'quad_term':([67,],[91,]),'push_cte':([71,72,],[95,96,]),'quad_comp':([133,],[156,]),'generarEra':([38,88,],[56,56,]),'loopFromDo':([28,33,35,114,145,154,180,197,],[39,39,39,39,39,39,39,39,]),'expresion':([54,65,73,80,82,105,106,111,117,118,139,160,177,187,],[75,87,97,110,112,135,136,140,87,87,110,110,186,191,]),'gosub':([107,],[137,]),'llamadaAFuncion':([28,33,35,65,114,117,118,145,154,180,197,],[40,40,40,90,40,90,90,40,40,40,40,]),'asignacion':([28,33,35,114,145,154,180,197,],[42,42,42,42,42,42,42,42,]),'while1':([43,],[58,]),'bloqueAux':([28,33,35,114,145,154,180,197,],[44,51,53,143,166,173,188,198,]),'while':([28,33,35,114,145,154,180,197,],[45,45,45,45,45,45,45,45,]),'termino1':([94,],[126,]),'exp':([54,65,73,80,82,103,105,106,111,117,118,139,150,151,160,177,187,],[76,76,76,76,76,133,76,76,76,76,76,76,168,169,76,76,76,]),'nomFunc':([27,],[31,]),'factorAux':([54,65,73,80,82,103,105,106,111,117,118,139,150,151,152,153,160,177,187,],[77,77,77,77,77,77,77,77,77,77,77,77,77,77,77,77,77,77,77,]),'comparacion':([28,33,35,114,145,154,180,197,],[46,46,46,46,46,46,46,46,]),'escritura':([28,33,35,114,145,154,180,197,],[47,47,47,47,47,47,47,47,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> program","S'",1,None,None,None),
  ('program -> PROGRAM ID COLON vars main function','program',6,'p_program','lexAndSyn.py',120),
  ('program -> PROGRAM ID COLON main function','program',5,'p_program','lexAndSyn.py',121),
  ('program -> PROGRAM ID COLON vars main','program',5,'p_program','lexAndSyn.py',122),
  ('program -> PROGRAM ID COLON main','program',4,'p_program','lexAndSyn.py',123),
  ('main -> nomMain LPAREN RPAREN LBRACE bloqueAux RBRACE','main',6,'p_main','lexAndSyn.py',129),
  ('main -> nomMain LPAREN RPAREN LBRACE vars bloqueAux RBRACE','main',7,'p_main','lexAndSyn.py',130),
  ('nomMain -> MAIN','nomMain',1,'p_nomMain','lexAndSyn.py',134),
  ('vars -> VAR varAux1','vars',2,'p_vars','lexAndSyn.py',143),
  ('varAux1 -> tipo varAux2 SEMICOLON','varAux1',3,'p_varAux1','lexAndSyn.py',147),
  ('varAux1 -> tipo varAux2 SEMICOLON varAux1','varAux1',4,'p_varAux1','lexAndSyn.py',148),
  ('varAux2 -> ID','varAux2',1,'p_varAux2','lexAndSyn.py',152),
  ('varAux2 -> ID COMA varAux2','varAux2',3,'p_varAux2','lexAndSyn.py',153),
  ('tipo -> INT','tipo',1,'p_tipo','lexAndSyn.py',171),
  ('tipo -> FLOAT','tipo',1,'p_tipo','lexAndSyn.py',172),
  ('tipo -> CHAR','tipo',1,'p_tipo','lexAndSyn.py',173),
  ('tipoFunc -> INT','tipoFunc',1,'p_tipoFunc','lexAndSyn.py',178),
  ('tipoFunc -> FLOAT','tipoFunc',1,'p_tipoFunc','lexAndSyn.py',179),
  ('tipoFunc -> CHAR','tipoFunc',1,'p_tipoFunc','lexAndSyn.py',180),
  ('tipoFunc -> VOID','tipoFunc',1,'p_tipoFunc','lexAndSyn.py',181),
  ('bloque -> LBRACE RBRACE','bloque',2,'p_bloque','lexAndSyn.py',186),
  ('bloque -> LBRACE bloqueAux RBRACE','bloque',3,'p_bloque','lexAndSyn.py',187),
  ('function -> FUNCTION tipoFunc nomFunc LPAREN RPAREN LBRACE RBRACE','function',7,'p_function','lexAndSyn.py',191),
  ('function -> FUNCTION tipoFunc nomFunc LPAREN RPAREN LBRACE vars bloqueAux RBRACE','function',9,'p_function','lexAndSyn.py',192),
  ('function -> FUNCTION tipoFunc nomFunc LPAREN RPAREN LBRACE RBRACE function','function',8,'p_function','lexAndSyn.py',193),
  ('function -> FUNCTION tipoFunc nomFunc LPAREN RPAREN LBRACE vars bloqueAux RBRACE function','function',10,'p_function','lexAndSyn.py',194),
  ('function -> FUNCTION tipoFunc nomFunc LPAREN param RPAREN LBRACE RBRACE','function',8,'p_function','lexAndSyn.py',195),
  ('function -> FUNCTION tipoFunc nomFunc LPAREN param RPAREN LBRACE vars bloqueAux RBRACE','function',10,'p_function','lexAndSyn.py',196),
  ('function -> FUNCTION tipoFunc nomFunc LPAREN param RPAREN LBRACE RBRACE function','function',9,'p_function','lexAndSyn.py',197),
  ('function -> FUNCTION tipoFunc nomFunc LPAREN param RPAREN LBRACE vars bloqueAux RBRACE function','function',11,'p_function','lexAndSyn.py',198),
  ('param -> tipo ID','param',2,'p_param','lexAndSyn.py',202),
  ('param -> tipo ID COMA param','param',4,'p_param','lexAndSyn.py',203),
  ('param -> empty','param',1,'p_param','lexAndSyn.py',204),
  ('empty -> <empty>','empty',0,'p_empty','lexAndSyn.py',208),
  ('nomFunc -> ID','nomFunc',1,'p_nomFunc','lexAndSyn.py',212),
  ('bloqueAux -> estatuto','bloqueAux',1,'p_bloqueAux','lexAndSyn.py',223),
  ('bloqueAux -> estatuto bloqueAux','bloqueAux',2,'p_bloqueAux','lexAndSyn.py',224),
  ('while -> WHILE while1 LPAREN expresion RPAREN while2 LBRACE bloqueAux RBRACE while3','while',10,'p_while','lexAndSyn.py',228),
  ('while1 -> <empty>','while1',0,'p_while1','lexAndSyn.py',232),
  ('while2 -> <empty>','while2',0,'p_while2','lexAndSyn.py',236),
  ('while3 -> <empty>','while3',0,'p_while3','lexAndSyn.py',240),
  ('loopFromDo -> FROM LPAREN ID EQUAL expresion RPAREN TO LPAREN expresion RPAREN DO LBRACE bloqueAux RBRACE','loopFromDo',14,'p_loopFromDo','lexAndSyn.py',244),
  ('estatuto -> asignacion','estatuto',1,'p_estatuto','lexAndSyn.py',256),
  ('estatuto -> condicion','estatuto',1,'p_estatuto','lexAndSyn.py',257),
  ('estatuto -> escritura','estatuto',1,'p_estatuto','lexAndSyn.py',258),
  ('estatuto -> while','estatuto',1,'p_estatuto','lexAndSyn.py',259),
  ('estatuto -> loopFromDo','estatuto',1,'p_estatuto','lexAndSyn.py',260),
  ('estatuto -> comparacion','estatuto',1,'p_estatuto','lexAndSyn.py',261),
  ('estatuto -> llamadaAFuncion','estatuto',1,'p_estatuto','lexAndSyn.py',262),
  ('llamadaAFuncion -> ID generarEra LPAREN paramFuncion gosub endProc RPAREN expresion','llamadaAFuncion',8,'p_llamadaAFuncion','lexAndSyn.py',265),
  ('llamadaAFuncion -> ID generarEra LPAREN paramFuncion gosub endProc RPAREN SEMICOLON','llamadaAFuncion',8,'p_llamadaAFuncion','lexAndSyn.py',266),
  ('endProc -> <empty>','endProc',0,'p_endProc','lexAndSyn.py',270),
  ('gosub -> <empty>','gosub',0,'p_gosub','lexAndSyn.py',275),
  ('generarEra -> <empty>','generarEra',0,'p_generarEra','lexAndSyn.py',285),
  ('paramFuncion -> ID push_id','paramFuncion',2,'p_paramFuncion','lexAndSyn.py',290),
  ('paramFuncion -> ID push_id COMA paramFuncion','paramFuncion',4,'p_paramFuncion','lexAndSyn.py',291),
  ('paramFuncion -> expresion','paramFuncion',1,'p_paramFuncion','lexAndSyn.py',292),
  ('paramFuncion -> expresion COMA paramFuncion','paramFuncion',3,'p_paramFuncion','lexAndSyn.py',293),
  ('paramFuncion -> empty','paramFuncion',1,'p_paramFuncion','lexAndSyn.py',294),
  ('asignacion -> ID push_id EQUAL push_poper expresion create_asign SEMICOLON','asignacion',7,'p_asignacion','lexAndSyn.py',299),
  ('create_asign -> <empty>','create_asign',0,'p_create_asign','lexAndSyn.py',303),
  ('comparacion -> ID push_id DOUBLEEQUAL push_poper expresion SEMICOLON','comparacion',6,'p_comparacion','lexAndSyn.py',309),
  ('condicion -> IF LPAREN expresion RPAREN cond bloque condFinal','condicion',7,'p_condicion','lexAndSyn.py',313),
  ('condicion -> IF LPAREN expresion RPAREN cond bloque ELSE condElse bloque condFinal','condicion',10,'p_condicion','lexAndSyn.py',314),
  ('cond -> <empty>','cond',0,'p_quad_cond','lexAndSyn.py',318),
  ('condElse -> <empty>','condElse',0,'p_quad_condElse','lexAndSyn.py',322),
  ('condFinal -> <empty>','condFinal',0,'p_quad_condFinal','lexAndSyn.py',326),
  ('escritura -> PRINT push_poper LPAREN escrituraAux RPAREN quad_print SEMICOLON','escritura',7,'p_escritura','lexAndSyn.py',330),
  ('quad_print -> <empty>','quad_print',0,'p_quad_print','lexAndSyn.py',334),
  ('escrituraAux -> expresion','escrituraAux',1,'p_escrituraAux','lexAndSyn.py',338),
  ('escrituraAux -> CTE_STRING','escrituraAux',1,'p_escrituraAux','lexAndSyn.py',339),
  ('escrituraAux -> expresion COMA escrituraAux','escrituraAux',3,'p_escrituraAux','lexAndSyn.py',340),
  ('escrituraAux -> CTE_STRING COMA escrituraAux','escrituraAux',3,'p_escrituraAux','lexAndSyn.py',341),
  ('escrituraAux -> llamadaAFuncion','escrituraAux',1,'p_escrituraAux','lexAndSyn.py',342),
  ('expresion -> exp','expresion',1,'p_expresion','lexAndSyn.py',346),
  ('expresion -> exp comp exp quad_comp','expresion',4,'p_expresion','lexAndSyn.py',347),
  ('comp -> LOWERTHAN push_poper','comp',2,'p_comp','lexAndSyn.py',351),
  ('comp -> MORETHAN push_poper','comp',2,'p_comp','lexAndSyn.py',352),
  ('comp -> DIFFERENT push_poper','comp',2,'p_comp','lexAndSyn.py',353),
  ('comp -> DOUBLEEQUAL push_poper','comp',2,'p_comp','lexAndSyn.py',354),
  ('quad_comp -> <empty>','quad_comp',0,'p_quad_comp','lexAndSyn.py',358),
  ('exp -> termino quad_term','exp',2,'p_exp','lexAndSyn.py',362),
  ('exp -> termino quad_term exp1','exp',3,'p_exp','lexAndSyn.py',363),
  ('exp1 -> PLUS push_poper exp','exp1',3,'p_exp1','lexAndSyn.py',367),
  ('exp1 -> MINUS push_poper exp','exp1',3,'p_exp1','lexAndSyn.py',368),
  ('quad_term -> <empty>','quad_term',0,'p_quad_term','lexAndSyn.py',372),
  ('quad_fact -> <empty>','quad_fact',0,'p_quad_fact','lexAndSyn.py',376),
  ('termino -> factor quad_fact','termino',2,'p_termino','lexAndSyn.py',380),
  ('termino -> factor quad_fact termino1','termino',3,'p_termino','lexAndSyn.py',381),
  ('termino1 -> TIMES push_poper termino','termino1',3,'p_termino1','lexAndSyn.py',385),
  ('termino1 -> DIVIDE push_poper termino','termino1',3,'p_termino1','lexAndSyn.py',386),
  ('factor -> LPAREN expresion RPAREN','factor',3,'p_factor','lexAndSyn.py',390),
  ('factor -> factorAux','factor',1,'p_factor','lexAndSyn.py',391),
  ('factorAux -> PLUS push_poper var_cte','factorAux',3,'p_factorAux','lexAndSyn.py',395),
  ('factorAux -> MINUS push_poper var_cte','factorAux',3,'p_factorAux','lexAndSyn.py',396),
  ('factorAux -> var_cte','factorAux',1,'p_factorAux','lexAndSyn.py',397),
  ('push_id -> <empty>','push_id',0,'p_push_id','lexAndSyn.py',401),
  ('push_cte -> <empty>','push_cte',0,'p_push_cte','lexAndSyn.py',405),
  ('push_poper -> <empty>','push_poper',0,'p_push_poper','lexAndSyn.py',409),
  ('var_cte -> ID push_id','var_cte',2,'p_var_cte','lexAndSyn.py',413),
  ('var_cte -> CTE_I push_cte','var_cte',2,'p_var_cte','lexAndSyn.py',414),
  ('var_cte -> CTE_F push_cte','var_cte',2,'p_var_cte','lexAndSyn.py',415),
]
