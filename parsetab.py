
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'AND CHAR COLON COMA CTE_F CTE_I CTE_STRING DIFFERENT DIVIDE DOUBLEEQUAL ELSE EQUAL FLOAT FOR FUNCTION ID IF INT LBRACE LOWERTHAN LPAREN MAIN MINUS MORETHAN OR PLUS PRINT PROGRAM RBRACE RPAREN SEMICOLON TIMES VAR VOID WHILEprogram : PROGRAM ID COLON vars main function\n               | PROGRAM ID COLON main function\n               | PROGRAM ID COLON vars main\n               | PROGRAM ID COLON main\n    main : nomMain LPAREN RPAREN LBRACE bloqueAux RBRACE\n            | nomMain LPAREN RPAREN LBRACE vars bloqueAux RBRACE\n     nomMain : MAIN\n    vars : VAR varAux1\n    varAux1 : tipo varAux2 SEMICOLON\n               | tipo varAux2 SEMICOLON varAux1\n    varAux2 : ID\n            | ID COMA varAux2\n    tipo : INT\n            | FLOAT\n            | CHAR\n    tipoFunc : INT\n            | FLOAT\n            | CHAR\n            | VOID\n    bloque : LBRACE RBRACE\n              | LBRACE bloqueAux RBRACE\n    function : FUNCTION tipoFunc nomFunc LPAREN RPAREN LBRACE RBRACE\n              | FUNCTION tipoFunc nomFunc LPAREN RPAREN LBRACE vars bloqueAux RBRACE\n              | FUNCTION tipoFunc nomFunc LPAREN RPAREN LBRACE RBRACE function\n              | FUNCTION tipoFunc nomFunc LPAREN RPAREN LBRACE vars bloqueAux RBRACE function\n              | FUNCTION tipoFunc nomFunc LPAREN param RPAREN LBRACE RBRACE\n              | FUNCTION tipoFunc nomFunc LPAREN param RPAREN LBRACE vars bloqueAux RBRACE\n              | FUNCTION tipoFunc nomFunc LPAREN param RPAREN LBRACE RBRACE function\n              | FUNCTION tipoFunc nomFunc LPAREN param RPAREN LBRACE vars bloqueAux RBRACE function\n    param : tipo ID\n             | tipo ID COMA param\n    nomFunc : ID\n    bloqueAux : estatuto\n                 | estatuto bloqueAux\n    while : WHILE LPAREN expresion RPAREN bloque\n    estatuto : asignacion\n                | condicion\n                | escritura\n                | while\n                | comparacion\n    asignacion : ID push_id EQUAL push_poper expresion create_asign SEMICOLON\n    create_asign :comparacion : ID push_id DOUBLEEQUAL push_poper expresion SEMICOLON\n    condicion : IF LPAREN expresion RPAREN bloque SEMICOLON\n                 | IF LPAREN expresion RPAREN bloque ELSE bloque SEMICOLON\n    escritura : PRINT push_poper LPAREN exp RPAREN quad_print SEMICOLON\n    quad_print :escrituraAux : expresion\n                    | CTE_STRING\n                    | expresion COMA escrituraAux\n                    | CTE_STRING COMA escrituraAux\n    expresion : exp\n                 | exp LOWERTHAN push_poper exp quad_comp\n                 | exp MORETHAN push_poper exp quad_comp\n                 | exp DIFFERENT push_poper exp quad_comp\n    quad_comp :exp : termino quad_term\n           | termino quad_term exp1\n    exp1 : PLUS push_poper exp\n            | MINUS push_poper exp\n    quad_term :quad_fact :termino : factor quad_fact\n               | factor quad_fact termino1\n    termino1 : TIMES push_poper termino\n                | DIVIDE push_poper termino\n    factor : LPAREN expresion RPAREN\n              | factorAux\n    factorAux : PLUS push_poper var_cte\n                 | MINUS push_poper var_cte\n                 | var_cte \n    push_id :push_cte :push_poper :var_cte : ID push_id\n               | CTE_I push_cte\n               | CTE_F push_cte\n    '
    
_lr_action_items = {'VOID':([18,],[24,]),'EQUAL':([37,51,],[-72,61,]),'CHAR':([8,18,29,47,97,],[12,26,12,12,12,]),'VAR':([4,28,75,96,],[8,8,8,8,]),'WHILE':([16,28,29,33,35,36,39,42,43,44,45,95,110,115,119,122,128,130,138,139,144,151,],[-8,40,-9,40,40,-37,-36,-39,-40,-38,-10,40,40,-35,40,-43,-20,-44,-46,-41,-21,-45,]),'PROGRAM':([0,],[2,]),'PRINT':([16,28,29,33,35,36,39,42,43,44,45,95,110,115,119,122,128,130,138,139,144,151,],[-8,34,-9,34,34,-37,-36,-39,-40,-38,-10,34,34,-35,34,-43,-20,-44,-46,-41,-21,-45,]),'MORETHAN':([62,63,66,67,68,70,72,73,81,84,85,86,88,101,104,105,107,109,140,141,142,143,],[-71,-61,-62,-73,-73,-72,92,-68,-57,-63,-77,-76,-75,-58,-70,-69,-64,-67,-59,-60,-66,-65,]),'MINUS':([52,53,59,60,61,62,63,66,67,68,69,70,73,79,80,81,84,85,86,88,90,91,92,102,103,104,105,106,107,108,109,112,113,114,124,125,126,127,142,143,],[64,64,64,-74,-74,-71,-61,-62,-73,-73,64,-72,-68,64,64,103,-63,-77,-76,-75,-74,-74,-74,-74,-74,-70,-69,-74,-64,-74,-67,64,64,64,64,64,64,64,-66,-65,]),'DIVIDE':([62,66,67,68,70,73,84,85,86,88,104,105,109,],[-71,-62,-73,-73,-72,-68,106,-77,-76,-75,-70,-69,-67,]),'RPAREN':([11,47,56,62,63,66,67,68,70,71,72,73,74,77,78,81,84,85,86,87,88,101,104,105,107,109,120,132,133,134,140,141,142,143,146,147,148,],[20,55,76,-71,-61,-62,-73,-73,-72,89,-52,-68,93,-30,98,-57,-63,-77,-76,109,-75,-58,-70,-69,-64,-67,-31,-56,-56,-56,-59,-60,-66,-65,-55,-53,-54,]),'SEMICOLON':([21,22,46,62,63,66,67,68,70,72,73,81,84,85,86,88,98,99,100,101,104,105,107,109,111,121,123,128,132,133,134,140,141,142,143,144,145,146,147,148,],[29,-11,-12,-71,-61,-62,-73,-73,-72,-52,-68,-57,-63,-77,-76,-75,-47,122,-42,-58,-70,-69,-64,-67,130,138,139,-20,-56,-56,-56,-59,-60,-66,-65,-21,151,-55,-53,-54,]),'LOWERTHAN':([62,63,66,67,68,70,72,73,81,84,85,86,88,101,104,105,107,109,140,141,142,143,],[-71,-61,-62,-73,-73,-72,91,-68,-57,-63,-77,-76,-75,-58,-70,-69,-64,-67,-59,-60,-66,-65,]),'COLON':([3,],[4,]),'CTE_I':([52,53,59,60,61,64,65,69,79,80,82,83,90,91,92,102,103,106,108,112,113,114,124,125,126,127,],[68,68,68,-74,-74,-74,-74,68,68,68,68,68,-74,-74,-74,-74,-74,-74,-74,68,68,68,68,68,68,68,]),'CTE_F':([52,53,59,60,61,64,65,69,79,80,82,83,90,91,92,102,103,106,108,112,113,114,124,125,126,127,],[67,67,67,-74,-74,-74,-74,67,67,67,67,67,-74,-74,-74,-74,-74,-74,-74,67,67,67,67,67,67,67,]),'PLUS':([52,53,59,60,61,62,63,66,67,68,69,70,73,79,80,81,84,85,86,88,90,91,92,102,103,104,105,106,107,108,109,112,113,114,124,125,126,127,142,143,],[65,65,65,-74,-74,-71,-61,-62,-73,-73,65,-72,-68,65,65,102,-63,-77,-76,-75,-74,-74,-74,-74,-74,-70,-69,-74,-64,-74,-67,65,65,65,65,65,65,65,-66,-65,]),'$end':([1,9,10,17,19,54,58,94,116,118,135,136,149,150,152,],[0,-4,-3,-2,-1,-5,-6,-22,-24,-26,-23,-28,-25,-27,-29,]),'FUNCTION':([9,10,54,58,94,118,135,150,],[18,18,-5,-6,18,18,18,18,]),'DIFFERENT':([62,63,66,67,68,70,72,73,81,84,85,86,88,101,104,105,107,109,140,141,142,143,],[-71,-61,-62,-73,-73,-72,90,-68,-57,-63,-77,-76,-75,-58,-70,-69,-64,-67,-59,-60,-66,-65,]),'RBRACE':([35,36,39,41,42,43,44,48,50,75,96,110,115,117,122,128,129,130,137,138,139,144,151,],[-33,-37,-36,54,-39,-40,-38,58,-34,94,118,128,-35,135,-43,-20,144,-44,150,-46,-41,-21,-45,]),'DOUBLEEQUAL':([37,51,],[-72,60,]),'TIMES':([62,66,67,68,70,73,84,85,86,88,104,105,109,],[-71,-62,-73,-73,-72,-68,108,-77,-76,-75,-70,-69,-67,]),'LPAREN':([6,7,31,32,34,38,40,49,52,53,59,60,61,69,79,80,90,91,92,102,103,106,108,112,113,114,124,125,126,127,],[-7,11,47,-32,-74,52,53,59,69,69,69,-74,-74,69,69,69,-74,-74,-74,-74,-74,-74,-74,69,69,69,69,69,69,69,]),'COMA':([22,77,],[30,97,]),'ELSE':([111,128,144,],[131,-20,-21,]),'ID':([2,12,13,14,15,16,23,24,25,26,27,28,29,30,33,35,36,39,42,43,44,45,52,53,57,59,60,61,64,65,69,79,80,82,83,90,91,92,95,102,103,106,108,110,112,113,114,115,119,122,124,125,126,127,128,130,138,139,144,151,],[3,-15,22,-13,-14,-8,-16,-19,-17,-18,32,37,-9,22,37,37,-37,-36,-39,-40,-38,-10,70,70,77,70,-74,-74,-74,-74,70,70,70,70,70,-74,-74,-74,37,-74,-74,-74,-74,37,70,70,70,-35,37,-43,70,70,70,70,-20,-44,-46,-41,-21,-45,]),'IF':([16,28,29,33,35,36,39,42,43,44,45,95,110,115,119,122,128,130,138,139,144,151,],[-8,38,-9,38,38,-37,-36,-39,-40,-38,-10,38,38,-35,38,-43,-20,-44,-46,-41,-21,-45,]),'LBRACE':([20,55,76,89,93,131,],[28,75,96,110,110,110,]),'INT':([8,18,29,47,97,],[14,23,14,14,14,]),'FLOAT':([8,18,29,47,97,],[15,25,15,15,15,]),'MAIN':([4,5,16,29,45,],[6,6,-8,-9,-10,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'quad_fact':([66,],[84,]),'vars':([4,28,75,96,],[5,33,95,119,]),'var_cte':([52,53,59,69,79,80,82,83,112,113,114,124,125,126,127,],[62,62,62,62,62,62,104,105,62,62,62,62,62,62,62,]),'nomMain':([4,5,],[7,7,]),'termino':([52,53,59,69,79,80,112,113,114,124,125,126,127,],[63,63,63,63,63,63,63,63,63,63,63,142,143,]),'create_asign':([100,],[123,]),'tipoFunc':([18,],[27,]),'bloque':([89,93,131,],[111,115,145,]),'push_id':([37,70,],[51,88,]),'quad_print':([98,],[121,]),'tipo':([8,29,47,97,],[13,13,57,57,]),'exp1':([81,],[101,]),'estatuto':([28,33,35,95,110,119,],[35,35,35,35,35,35,]),'param':([47,97,],[56,120,]),'varAux2':([13,30,],[21,46,]),'program':([0,],[1,]),'varAux1':([8,29,],[16,45,]),'factor':([52,53,59,69,79,80,112,113,114,124,125,126,127,],[66,66,66,66,66,66,66,66,66,66,66,66,66,]),'main':([4,5,],[9,10,]),'function':([9,10,94,118,135,150,],[17,19,116,136,149,152,]),'push_poper':([34,60,61,64,65,90,91,92,102,103,106,108,],[49,79,80,82,83,112,113,114,124,125,126,127,]),'condicion':([28,33,35,95,110,119,],[36,36,36,36,36,36,]),'quad_term':([63,],[81,]),'push_cte':([67,68,],[85,86,]),'quad_comp':([132,133,134,],[146,147,148,]),'expresion':([52,53,69,79,80,],[71,74,87,99,100,]),'asignacion':([28,33,35,95,110,119,],[39,39,39,39,39,39,]),'bloqueAux':([28,33,35,95,110,119,],[41,48,50,117,129,137,]),'while':([28,33,35,95,110,119,],[42,42,42,42,42,42,]),'termino1':([84,],[107,]),'exp':([52,53,59,69,79,80,112,113,114,124,125,],[72,72,78,72,72,72,132,133,134,140,141,]),'nomFunc':([27,],[31,]),'factorAux':([52,53,59,69,79,80,112,113,114,124,125,126,127,],[73,73,73,73,73,73,73,73,73,73,73,73,73,]),'comparacion':([28,33,35,95,110,119,],[43,43,43,43,43,43,]),'escritura':([28,33,35,95,110,119,],[44,44,44,44,44,44,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> program","S'",1,None,None,None),
  ('program -> PROGRAM ID COLON vars main function','program',6,'p_program','lexAndSyn.py',117),
  ('program -> PROGRAM ID COLON main function','program',5,'p_program','lexAndSyn.py',118),
  ('program -> PROGRAM ID COLON vars main','program',5,'p_program','lexAndSyn.py',119),
  ('program -> PROGRAM ID COLON main','program',4,'p_program','lexAndSyn.py',120),
  ('main -> nomMain LPAREN RPAREN LBRACE bloqueAux RBRACE','main',6,'p_main','lexAndSyn.py',126),
  ('main -> nomMain LPAREN RPAREN LBRACE vars bloqueAux RBRACE','main',7,'p_main','lexAndSyn.py',127),
  ('nomMain -> MAIN','nomMain',1,'p_nomMain','lexAndSyn.py',131),
  ('vars -> VAR varAux1','vars',2,'p_vars','lexAndSyn.py',140),
  ('varAux1 -> tipo varAux2 SEMICOLON','varAux1',3,'p_varAux1','lexAndSyn.py',144),
  ('varAux1 -> tipo varAux2 SEMICOLON varAux1','varAux1',4,'p_varAux1','lexAndSyn.py',145),
  ('varAux2 -> ID','varAux2',1,'p_varAux2','lexAndSyn.py',149),
  ('varAux2 -> ID COMA varAux2','varAux2',3,'p_varAux2','lexAndSyn.py',150),
  ('tipo -> INT','tipo',1,'p_tipo','lexAndSyn.py',168),
  ('tipo -> FLOAT','tipo',1,'p_tipo','lexAndSyn.py',169),
  ('tipo -> CHAR','tipo',1,'p_tipo','lexAndSyn.py',170),
  ('tipoFunc -> INT','tipoFunc',1,'p_tipoFunc','lexAndSyn.py',175),
  ('tipoFunc -> FLOAT','tipoFunc',1,'p_tipoFunc','lexAndSyn.py',176),
  ('tipoFunc -> CHAR','tipoFunc',1,'p_tipoFunc','lexAndSyn.py',177),
  ('tipoFunc -> VOID','tipoFunc',1,'p_tipoFunc','lexAndSyn.py',178),
  ('bloque -> LBRACE RBRACE','bloque',2,'p_bloque','lexAndSyn.py',183),
  ('bloque -> LBRACE bloqueAux RBRACE','bloque',3,'p_bloque','lexAndSyn.py',184),
  ('function -> FUNCTION tipoFunc nomFunc LPAREN RPAREN LBRACE RBRACE','function',7,'p_function','lexAndSyn.py',188),
  ('function -> FUNCTION tipoFunc nomFunc LPAREN RPAREN LBRACE vars bloqueAux RBRACE','function',9,'p_function','lexAndSyn.py',189),
  ('function -> FUNCTION tipoFunc nomFunc LPAREN RPAREN LBRACE RBRACE function','function',8,'p_function','lexAndSyn.py',190),
  ('function -> FUNCTION tipoFunc nomFunc LPAREN RPAREN LBRACE vars bloqueAux RBRACE function','function',10,'p_function','lexAndSyn.py',191),
  ('function -> FUNCTION tipoFunc nomFunc LPAREN param RPAREN LBRACE RBRACE','function',8,'p_function','lexAndSyn.py',192),
  ('function -> FUNCTION tipoFunc nomFunc LPAREN param RPAREN LBRACE vars bloqueAux RBRACE','function',10,'p_function','lexAndSyn.py',193),
  ('function -> FUNCTION tipoFunc nomFunc LPAREN param RPAREN LBRACE RBRACE function','function',9,'p_function','lexAndSyn.py',194),
  ('function -> FUNCTION tipoFunc nomFunc LPAREN param RPAREN LBRACE vars bloqueAux RBRACE function','function',11,'p_function','lexAndSyn.py',195),
  ('param -> tipo ID','param',2,'p_param','lexAndSyn.py',199),
  ('param -> tipo ID COMA param','param',4,'p_param','lexAndSyn.py',200),
  ('nomFunc -> ID','nomFunc',1,'p_nomFunc','lexAndSyn.py',205),
  ('bloqueAux -> estatuto','bloqueAux',1,'p_bloqueAux','lexAndSyn.py',214),
  ('bloqueAux -> estatuto bloqueAux','bloqueAux',2,'p_bloqueAux','lexAndSyn.py',215),
  ('while -> WHILE LPAREN expresion RPAREN bloque','while',5,'p_while','lexAndSyn.py',219),
  ('estatuto -> asignacion','estatuto',1,'p_estatuto','lexAndSyn.py',223),
  ('estatuto -> condicion','estatuto',1,'p_estatuto','lexAndSyn.py',224),
  ('estatuto -> escritura','estatuto',1,'p_estatuto','lexAndSyn.py',225),
  ('estatuto -> while','estatuto',1,'p_estatuto','lexAndSyn.py',226),
  ('estatuto -> comparacion','estatuto',1,'p_estatuto','lexAndSyn.py',227),
  ('asignacion -> ID push_id EQUAL push_poper expresion create_asign SEMICOLON','asignacion',7,'p_asignacion','lexAndSyn.py',231),
  ('create_asign -> <empty>','create_asign',0,'p_create_asign','lexAndSyn.py',236),
  ('comparacion -> ID push_id DOUBLEEQUAL push_poper expresion SEMICOLON','comparacion',6,'p_comparacion','lexAndSyn.py',240),
  ('condicion -> IF LPAREN expresion RPAREN bloque SEMICOLON','condicion',6,'p_condicion','lexAndSyn.py',244),
  ('condicion -> IF LPAREN expresion RPAREN bloque ELSE bloque SEMICOLON','condicion',8,'p_condicion','lexAndSyn.py',245),
  ('escritura -> PRINT push_poper LPAREN exp RPAREN quad_print SEMICOLON','escritura',7,'p_escritura','lexAndSyn.py',249),
  ('quad_print -> <empty>','quad_print',0,'p_quad_print','lexAndSyn.py',253),
  ('escrituraAux -> expresion','escrituraAux',1,'p_escrituraAux','lexAndSyn.py',257),
  ('escrituraAux -> CTE_STRING','escrituraAux',1,'p_escrituraAux','lexAndSyn.py',258),
  ('escrituraAux -> expresion COMA escrituraAux','escrituraAux',3,'p_escrituraAux','lexAndSyn.py',259),
  ('escrituraAux -> CTE_STRING COMA escrituraAux','escrituraAux',3,'p_escrituraAux','lexAndSyn.py',260),
  ('expresion -> exp','expresion',1,'p_expresion','lexAndSyn.py',264),
  ('expresion -> exp LOWERTHAN push_poper exp quad_comp','expresion',5,'p_expresion','lexAndSyn.py',265),
  ('expresion -> exp MORETHAN push_poper exp quad_comp','expresion',5,'p_expresion','lexAndSyn.py',266),
  ('expresion -> exp DIFFERENT push_poper exp quad_comp','expresion',5,'p_expresion','lexAndSyn.py',267),
  ('quad_comp -> <empty>','quad_comp',0,'p_quad_comp','lexAndSyn.py',271),
  ('exp -> termino quad_term','exp',2,'p_exp','lexAndSyn.py',275),
  ('exp -> termino quad_term exp1','exp',3,'p_exp','lexAndSyn.py',276),
  ('exp1 -> PLUS push_poper exp','exp1',3,'p_exp1','lexAndSyn.py',280),
  ('exp1 -> MINUS push_poper exp','exp1',3,'p_exp1','lexAndSyn.py',281),
  ('quad_term -> <empty>','quad_term',0,'p_quad_term','lexAndSyn.py',285),
  ('quad_fact -> <empty>','quad_fact',0,'p_quad_fact','lexAndSyn.py',289),
  ('termino -> factor quad_fact','termino',2,'p_termino','lexAndSyn.py',293),
  ('termino -> factor quad_fact termino1','termino',3,'p_termino','lexAndSyn.py',294),
  ('termino1 -> TIMES push_poper termino','termino1',3,'p_termino1','lexAndSyn.py',298),
  ('termino1 -> DIVIDE push_poper termino','termino1',3,'p_termino1','lexAndSyn.py',299),
  ('factor -> LPAREN expresion RPAREN','factor',3,'p_factor','lexAndSyn.py',303),
  ('factor -> factorAux','factor',1,'p_factor','lexAndSyn.py',304),
  ('factorAux -> PLUS push_poper var_cte','factorAux',3,'p_factorAux','lexAndSyn.py',308),
  ('factorAux -> MINUS push_poper var_cte','factorAux',3,'p_factorAux','lexAndSyn.py',309),
  ('factorAux -> var_cte','factorAux',1,'p_factorAux','lexAndSyn.py',310),
  ('push_id -> <empty>','push_id',0,'p_push_id','lexAndSyn.py',314),
  ('push_cte -> <empty>','push_cte',0,'p_push_cte','lexAndSyn.py',319),
  ('push_poper -> <empty>','push_poper',0,'p_push_poper','lexAndSyn.py',324),
  ('var_cte -> ID push_id','var_cte',2,'p_var_cte','lexAndSyn.py',329),
  ('var_cte -> CTE_I push_cte','var_cte',2,'p_var_cte','lexAndSyn.py',330),
  ('var_cte -> CTE_F push_cte','var_cte',2,'p_var_cte','lexAndSyn.py',331),
]
