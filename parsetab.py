
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'AND CHAR COLON COMA CTE_F CTE_I CTE_STRING DIFFERENT DIVIDE DO DOUBLEEQUAL ELSE EQUAL FLOAT FROM FUNCTION ID IF INT LBRACE LOWERTHAN LPAREN MAIN MINUS MORETHAN OR PLUS PRINT PROGRAM RBRACE RPAREN SEMICOLON TIMES TO VAR VOID WHILEprogram : PROGRAM ID COLON vars main function\n               | PROGRAM ID COLON main function\n               | PROGRAM ID COLON vars main\n               | PROGRAM ID COLON main\n    main : nomMain LPAREN RPAREN LBRACE bloqueAux RBRACE\n            | nomMain LPAREN RPAREN LBRACE vars bloqueAux RBRACE\n     nomMain : MAIN\n    vars : VAR varAux1\n    varAux1 : tipo varAux2 SEMICOLON\n               | tipo varAux2 SEMICOLON varAux1\n    varAux2 : ID\n            | ID COMA varAux2\n    tipo : INT\n            | FLOAT\n            | CHAR\n    tipoFunc : INT\n            | FLOAT\n            | CHAR\n            | VOID\n    bloque : LBRACE RBRACE\n              | LBRACE bloqueAux RBRACE\n    function : FUNCTION tipoFunc nomFunc LPAREN RPAREN LBRACE RBRACE\n              | FUNCTION tipoFunc nomFunc LPAREN RPAREN LBRACE vars bloqueAux RBRACE\n              | FUNCTION tipoFunc nomFunc LPAREN RPAREN LBRACE RBRACE function\n              | FUNCTION tipoFunc nomFunc LPAREN RPAREN LBRACE vars bloqueAux RBRACE function\n              | FUNCTION tipoFunc nomFunc LPAREN param RPAREN LBRACE RBRACE\n              | FUNCTION tipoFunc nomFunc LPAREN param RPAREN LBRACE vars bloqueAux RBRACE\n              | FUNCTION tipoFunc nomFunc LPAREN param RPAREN LBRACE RBRACE function\n              | FUNCTION tipoFunc nomFunc LPAREN param RPAREN LBRACE vars bloqueAux RBRACE function\n    param : tipo ID\n             | tipo ID COMA param\n    nomFunc : ID\n    bloqueAux : estatuto\n                 | estatuto bloqueAux\n    while : WHILE while1 LPAREN expresion RPAREN while2 LBRACE bloqueAux RBRACE while3\n    while1 :while2 :while3 :loopFromDo : FROM LPAREN ID EQUAL expresion RPAREN TO LPAREN expresion RPAREN DO LBRACE bloqueAux RBRACE\n    estatuto : asignacion\n                | condicion\n                | escritura\n                | while\n                | loopFromDo\n                | comparacion\n    asignacion : ID push_id EQUAL push_poper expresion create_asign SEMICOLON\n    create_asign :comparacion : ID push_id DOUBLEEQUAL push_poper expresion SEMICOLON\n    condicion : IF LPAREN expresion RPAREN cond bloque condFinal\n                 | IF LPAREN expresion RPAREN cond bloque ELSE condElse bloque condFinal\n    cond :condElse :condFinal :escritura : PRINT push_poper LPAREN exp RPAREN quad_print SEMICOLON\n    quad_print :escrituraAux : expresion\n                    | CTE_STRING\n                    | expresion COMA escrituraAux\n                    | CTE_STRING COMA escrituraAux\n    expresion : exp\n                 | exp comp exp quad_comp\n    comp : LOWERTHAN push_poper\n            | MORETHAN push_poper\n            | DIFFERENT push_poper\n            | DOUBLEEQUAL push_poper\n    quad_comp :exp : termino quad_term\n           | termino quad_term exp1\n    exp1 : PLUS push_poper exp\n            | MINUS push_poper exp\n    quad_term :quad_fact :termino : factor quad_fact\n               | factor quad_fact termino1\n    termino1 : TIMES push_poper termino\n                | DIVIDE push_poper termino\n    factor : LPAREN expresion RPAREN\n              | factorAux\n    factorAux : PLUS push_poper var_cte\n                 | MINUS push_poper var_cte\n                 | var_cte \n    push_id :push_cte :push_poper :var_cte : ID push_id\n               | CTE_I push_cte\n               | CTE_F push_cte\n               | CTE_STRING push_cte\n    '
    
_lr_action_items = {'CTE_STRING':([53,62,65,66,71,76,77,79,85,86,94,95,96,97,98,99,100,101,109,110,113,115,118,119,120,122,133,134,135,136,163,],[69,69,-84,-84,69,-84,-84,69,69,69,-84,-84,-84,69,-84,69,69,69,-84,-84,-84,-84,-64,-65,-62,-63,69,69,69,69,69,]),'DO':([170,],[172,]),'VOID':([18,],[24,]),'EQUAL':([38,54,78,],[-82,77,101,]),'CHAR':([8,18,29,49,106,],[12,26,12,12,12,]),'VAR':([4,28,80,105,],[8,8,8,8,]),'WHILE':([16,28,29,33,35,37,39,41,44,45,46,47,104,130,137,138,140,147,152,154,156,158,161,166,168,169,171,173,175,],[-8,42,-9,42,42,-41,-44,-40,-43,-45,-42,-10,42,42,42,-53,-48,-54,-20,-49,-46,42,-21,-53,-38,-50,-35,42,-39,]),'PROGRAM':([0,],[2,]),'PRINT':([16,28,29,33,35,37,39,41,44,45,46,47,104,130,137,138,140,147,152,154,156,158,161,166,168,169,171,173,175,],[-8,34,-9,34,34,-41,-44,-40,-43,-45,-42,-10,34,34,34,-53,-48,-54,-20,-49,-46,34,-21,-53,-38,-50,-35,34,-39,]),'MORETHAN':([63,64,67,68,69,70,72,74,75,84,87,88,89,90,92,108,111,112,114,116,148,149,150,151,],[-81,-71,-72,-83,-83,-83,-82,98,-78,-67,-73,-87,-88,-86,-85,-68,-80,-79,-74,-77,-69,-70,-76,-75,]),'MINUS':([53,62,63,64,67,68,69,70,71,72,75,76,77,79,84,87,88,89,90,92,94,95,96,97,98,99,100,101,109,110,111,112,113,114,115,116,118,119,120,122,133,134,135,136,150,151,163,],[65,65,-81,-71,-72,-83,-83,-83,65,-82,-78,-84,-84,65,110,-73,-87,-88,-86,-85,-84,-84,-84,65,-84,65,65,65,-84,-84,-80,-79,-84,-74,-84,-77,-64,-65,-62,-63,65,65,65,65,-76,-75,65,]),'DIVIDE':([63,67,68,69,70,72,75,87,88,89,90,92,111,112,116,],[-81,-72,-83,-83,-83,-82,-78,113,-87,-88,-86,-85,-80,-79,-77,]),'RPAREN':([11,49,59,63,64,67,68,69,70,72,73,74,75,82,83,84,87,88,89,90,91,92,102,108,111,112,114,116,121,125,131,139,148,149,150,151,167,],[20,58,81,-81,-71,-72,-83,-83,-83,-82,93,-60,-78,-30,107,-67,-73,-87,-88,-86,116,-85,126,-68,-80,-79,-74,-77,-66,142,-31,-61,-69,-70,-76,-75,170,]),'SEMICOLON':([21,22,48,63,64,67,68,69,70,72,74,75,84,87,88,89,90,92,107,108,111,112,114,116,121,123,124,132,139,141,148,149,150,151,],[29,-11,-12,-81,-71,-72,-83,-83,-83,-82,-60,-78,-67,-73,-87,-88,-86,-85,-55,-68,-80,-79,-74,-77,-66,140,-47,147,-61,156,-69,-70,-76,-75,]),'LOWERTHAN':([63,64,67,68,69,70,72,74,75,84,87,88,89,90,92,108,111,112,114,116,148,149,150,151,],[-81,-71,-72,-83,-83,-83,-82,96,-78,-67,-73,-87,-88,-86,-85,-68,-80,-79,-74,-77,-69,-70,-76,-75,]),'TO':([142,],[157,]),'COLON':([3,],[4,]),'CTE_I':([53,62,65,66,71,76,77,79,85,86,94,95,96,97,98,99,100,101,109,110,113,115,118,119,120,122,133,134,135,136,163,],[70,70,-84,-84,70,-84,-84,70,70,70,-84,-84,-84,70,-84,70,70,70,-84,-84,-84,-84,-64,-65,-62,-63,70,70,70,70,70,]),'CTE_F':([53,62,65,66,71,76,77,79,85,86,94,95,96,97,98,99,100,101,109,110,113,115,118,119,120,122,133,134,135,136,163,],[68,68,-84,-84,68,-84,-84,68,68,68,-84,-84,-84,68,-84,68,68,68,-84,-84,-84,-84,-64,-65,-62,-63,68,68,68,68,68,]),'PLUS':([53,62,63,64,67,68,69,70,71,72,75,76,77,79,84,87,88,89,90,92,94,95,96,97,98,99,100,101,109,110,111,112,113,114,115,116,118,119,120,122,133,134,135,136,150,151,163,],[66,66,-81,-71,-72,-83,-83,-83,66,-82,-78,-84,-84,66,109,-73,-87,-88,-86,-85,-84,-84,-84,66,-84,66,66,66,-84,-84,-80,-79,-84,-74,-84,-77,-64,-65,-62,-63,66,66,66,66,-76,-75,66,]),'$end':([1,9,10,17,19,57,61,103,127,129,144,145,159,160,165,],[0,-4,-3,-2,-1,-5,-6,-22,-24,-26,-23,-28,-25,-27,-29,]),'FUNCTION':([9,10,57,61,103,129,144,160,],[18,18,-5,-6,18,18,18,18,]),'DIFFERENT':([63,64,67,68,69,70,72,74,75,84,87,88,89,90,92,108,111,112,114,116,148,149,150,151,],[-81,-71,-72,-83,-83,-83,-82,94,-78,-67,-73,-87,-88,-86,-85,-68,-80,-79,-74,-77,-69,-70,-76,-75,]),'RBRACE':([35,37,39,41,43,44,45,46,50,52,80,105,128,137,138,140,146,147,152,153,154,156,161,164,166,168,169,171,174,175,],[-33,-41,-44,-40,57,-43,-45,-42,61,-34,103,129,144,152,-53,-48,160,-54,-20,161,-49,-46,-21,168,-53,-38,-50,-35,175,-39,]),'DOUBLEEQUAL':([38,54,63,64,67,68,69,70,72,74,75,84,87,88,89,90,92,108,111,112,114,116,148,149,150,151,],[-82,76,-81,-71,-72,-83,-83,-83,-82,95,-78,-67,-73,-87,-88,-86,-85,-68,-80,-79,-74,-77,-69,-70,-76,-75,]),'TIMES':([63,67,68,69,70,72,75,87,88,89,90,92,111,112,116,],[-81,-72,-83,-83,-83,-82,-78,115,-87,-88,-86,-85,-80,-79,-77,]),'LPAREN':([6,7,31,32,34,36,40,42,51,53,56,62,71,76,77,79,94,95,96,97,98,99,100,101,109,110,113,115,118,119,120,122,133,134,135,136,157,163,],[-7,11,49,-32,-84,53,55,-36,62,71,79,71,71,-84,-84,71,-84,-84,-84,71,-84,71,71,71,-84,-84,-84,-84,-64,-65,-62,-63,71,71,71,71,163,71,]),'COMA':([22,82,],[30,106,]),'ELSE':([138,152,161,],[155,-20,-21,]),'ID':([2,12,13,14,15,16,23,24,25,26,27,28,29,30,33,35,37,39,41,44,45,46,47,53,55,60,62,65,66,71,76,77,79,85,86,94,95,96,97,98,99,100,101,104,109,110,113,115,118,119,120,122,130,133,134,135,136,137,138,140,147,152,154,156,158,161,163,166,168,169,171,173,175,],[3,-15,22,-13,-14,-8,-16,-19,-17,-18,32,38,-9,22,38,38,-41,-44,-40,-43,-45,-42,-10,72,78,82,72,-84,-84,72,-84,-84,72,72,72,-84,-84,-84,72,-84,72,72,72,38,-84,-84,-84,-84,-64,-65,-62,-63,38,72,72,72,72,38,-53,-48,-54,-20,-49,-46,38,-21,72,-53,-38,-50,-35,38,-39,]),'IF':([16,28,29,33,35,37,39,41,44,45,46,47,104,130,137,138,140,147,152,154,156,158,161,166,168,169,171,173,175,],[-8,36,-9,36,36,-41,-44,-40,-43,-45,-42,-10,36,36,36,-53,-48,-54,-20,-49,-46,36,-21,-53,-38,-50,-35,36,-39,]),'LBRACE':([20,58,81,93,117,126,143,155,162,172,],[28,80,105,-51,137,-37,158,-52,137,173,]),'FROM':([16,28,29,33,35,37,39,41,44,45,46,47,104,130,137,138,140,147,152,154,156,158,161,166,168,169,171,173,175,],[-8,40,-9,40,40,-41,-44,-40,-43,-45,-42,-10,40,40,40,-53,-48,-54,-20,-49,-46,40,-21,-53,-38,-50,-35,40,-39,]),'INT':([8,18,29,49,106,],[14,23,14,14,14,]),'FLOAT':([8,18,29,49,106,],[15,25,15,15,15,]),'MAIN':([4,5,16,29,47,],[6,6,-8,-9,-10,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'quad_fact':([67,],[87,]),'vars':([4,28,80,105,],[5,33,104,130,]),'var_cte':([53,62,71,79,85,86,97,99,100,101,133,134,135,136,163,],[63,63,63,63,111,112,63,63,63,63,63,63,63,63,63,]),'while3':([168,],[171,]),'while2':([126,],[143,]),'while1':([42,],[56,]),'cond':([93,],[117,]),'termino':([53,62,71,79,97,99,100,101,133,134,135,136,163,],[64,64,64,64,64,64,64,64,64,64,150,151,64,]),'create_asign':([124,],[141,]),'tipoFunc':([18,],[27,]),'bloque':([117,162,],[138,166,]),'push_id':([38,72,],[54,92,]),'quad_print':([107,],[132,]),'tipo':([8,29,49,106,],[13,13,60,60,]),'exp1':([84,],[108,]),'estatuto':([28,33,35,104,130,137,158,173,],[35,35,35,35,35,35,35,35,]),'param':([49,106,],[59,131,]),'varAux2':([13,30,],[21,48,]),'program':([0,],[1,]),'varAux1':([8,29,],[16,47,]),'factor':([53,62,71,79,97,99,100,101,133,134,135,136,163,],[67,67,67,67,67,67,67,67,67,67,67,67,67,]),'main':([4,5,],[9,10,]),'function':([9,10,103,129,144,160,],[17,19,127,145,159,165,]),'condFinal':([138,166,],[154,169,]),'push_poper':([34,65,66,76,77,94,95,96,98,109,110,113,115,],[51,85,86,99,100,118,119,120,122,133,134,135,136,]),'comp':([74,],[97,]),'condElse':([155,],[162,]),'condicion':([28,33,35,104,130,137,158,173,],[37,37,37,37,37,37,37,37,]),'quad_term':([64,],[84,]),'push_cte':([68,69,70,],[88,89,90,]),'quad_comp':([121,],[139,]),'loopFromDo':([28,33,35,104,130,137,158,173,],[39,39,39,39,39,39,39,39,]),'expresion':([53,71,79,99,100,101,163,],[73,91,102,123,124,125,167,]),'asignacion':([28,33,35,104,130,137,158,173,],[41,41,41,41,41,41,41,41,]),'nomMain':([4,5,],[7,7,]),'bloqueAux':([28,33,35,104,130,137,158,173,],[43,50,52,128,146,153,164,174,]),'while':([28,33,35,104,130,137,158,173,],[44,44,44,44,44,44,44,44,]),'termino1':([87,],[114,]),'exp':([53,62,71,79,97,99,100,101,133,134,163,],[74,83,74,74,121,74,74,74,148,149,74,]),'nomFunc':([27,],[31,]),'factorAux':([53,62,71,79,97,99,100,101,133,134,135,136,163,],[75,75,75,75,75,75,75,75,75,75,75,75,75,]),'comparacion':([28,33,35,104,130,137,158,173,],[45,45,45,45,45,45,45,45,]),'escritura':([28,33,35,104,130,137,158,173,],[46,46,46,46,46,46,46,46,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> program","S'",1,None,None,None),
  ('program -> PROGRAM ID COLON vars main function','program',6,'p_program','lexAndSyn.py',119),
  ('program -> PROGRAM ID COLON main function','program',5,'p_program','lexAndSyn.py',120),
  ('program -> PROGRAM ID COLON vars main','program',5,'p_program','lexAndSyn.py',121),
  ('program -> PROGRAM ID COLON main','program',4,'p_program','lexAndSyn.py',122),
  ('main -> nomMain LPAREN RPAREN LBRACE bloqueAux RBRACE','main',6,'p_main','lexAndSyn.py',128),
  ('main -> nomMain LPAREN RPAREN LBRACE vars bloqueAux RBRACE','main',7,'p_main','lexAndSyn.py',129),
  ('nomMain -> MAIN','nomMain',1,'p_nomMain','lexAndSyn.py',133),
  ('vars -> VAR varAux1','vars',2,'p_vars','lexAndSyn.py',142),
  ('varAux1 -> tipo varAux2 SEMICOLON','varAux1',3,'p_varAux1','lexAndSyn.py',146),
  ('varAux1 -> tipo varAux2 SEMICOLON varAux1','varAux1',4,'p_varAux1','lexAndSyn.py',147),
  ('varAux2 -> ID','varAux2',1,'p_varAux2','lexAndSyn.py',151),
  ('varAux2 -> ID COMA varAux2','varAux2',3,'p_varAux2','lexAndSyn.py',152),
  ('tipo -> INT','tipo',1,'p_tipo','lexAndSyn.py',170),
  ('tipo -> FLOAT','tipo',1,'p_tipo','lexAndSyn.py',171),
  ('tipo -> CHAR','tipo',1,'p_tipo','lexAndSyn.py',172),
  ('tipoFunc -> INT','tipoFunc',1,'p_tipoFunc','lexAndSyn.py',177),
  ('tipoFunc -> FLOAT','tipoFunc',1,'p_tipoFunc','lexAndSyn.py',178),
  ('tipoFunc -> CHAR','tipoFunc',1,'p_tipoFunc','lexAndSyn.py',179),
  ('tipoFunc -> VOID','tipoFunc',1,'p_tipoFunc','lexAndSyn.py',180),
  ('bloque -> LBRACE RBRACE','bloque',2,'p_bloque','lexAndSyn.py',185),
  ('bloque -> LBRACE bloqueAux RBRACE','bloque',3,'p_bloque','lexAndSyn.py',186),
  ('function -> FUNCTION tipoFunc nomFunc LPAREN RPAREN LBRACE RBRACE','function',7,'p_function','lexAndSyn.py',190),
  ('function -> FUNCTION tipoFunc nomFunc LPAREN RPAREN LBRACE vars bloqueAux RBRACE','function',9,'p_function','lexAndSyn.py',191),
  ('function -> FUNCTION tipoFunc nomFunc LPAREN RPAREN LBRACE RBRACE function','function',8,'p_function','lexAndSyn.py',192),
  ('function -> FUNCTION tipoFunc nomFunc LPAREN RPAREN LBRACE vars bloqueAux RBRACE function','function',10,'p_function','lexAndSyn.py',193),
  ('function -> FUNCTION tipoFunc nomFunc LPAREN param RPAREN LBRACE RBRACE','function',8,'p_function','lexAndSyn.py',194),
  ('function -> FUNCTION tipoFunc nomFunc LPAREN param RPAREN LBRACE vars bloqueAux RBRACE','function',10,'p_function','lexAndSyn.py',195),
  ('function -> FUNCTION tipoFunc nomFunc LPAREN param RPAREN LBRACE RBRACE function','function',9,'p_function','lexAndSyn.py',196),
  ('function -> FUNCTION tipoFunc nomFunc LPAREN param RPAREN LBRACE vars bloqueAux RBRACE function','function',11,'p_function','lexAndSyn.py',197),
  ('param -> tipo ID','param',2,'p_param','lexAndSyn.py',201),
  ('param -> tipo ID COMA param','param',4,'p_param','lexAndSyn.py',202),
  ('nomFunc -> ID','nomFunc',1,'p_nomFunc','lexAndSyn.py',207),
  ('bloqueAux -> estatuto','bloqueAux',1,'p_bloqueAux','lexAndSyn.py',216),
  ('bloqueAux -> estatuto bloqueAux','bloqueAux',2,'p_bloqueAux','lexAndSyn.py',217),
  ('while -> WHILE while1 LPAREN expresion RPAREN while2 LBRACE bloqueAux RBRACE while3','while',10,'p_while','lexAndSyn.py',221),
  ('while1 -> <empty>','while1',0,'p_while1','lexAndSyn.py',225),
  ('while2 -> <empty>','while2',0,'p_while2','lexAndSyn.py',229),
  ('while3 -> <empty>','while3',0,'p_while3','lexAndSyn.py',233),
  ('loopFromDo -> FROM LPAREN ID EQUAL expresion RPAREN TO LPAREN expresion RPAREN DO LBRACE bloqueAux RBRACE','loopFromDo',14,'p_loopFromDo','lexAndSyn.py',237),
  ('estatuto -> asignacion','estatuto',1,'p_estatuto','lexAndSyn.py',249),
  ('estatuto -> condicion','estatuto',1,'p_estatuto','lexAndSyn.py',250),
  ('estatuto -> escritura','estatuto',1,'p_estatuto','lexAndSyn.py',251),
  ('estatuto -> while','estatuto',1,'p_estatuto','lexAndSyn.py',252),
  ('estatuto -> loopFromDo','estatuto',1,'p_estatuto','lexAndSyn.py',253),
  ('estatuto -> comparacion','estatuto',1,'p_estatuto','lexAndSyn.py',254),
  ('asignacion -> ID push_id EQUAL push_poper expresion create_asign SEMICOLON','asignacion',7,'p_asignacion','lexAndSyn.py',258),
  ('create_asign -> <empty>','create_asign',0,'p_create_asign','lexAndSyn.py',262),
  ('comparacion -> ID push_id DOUBLEEQUAL push_poper expresion SEMICOLON','comparacion',6,'p_comparacion','lexAndSyn.py',268),
  ('condicion -> IF LPAREN expresion RPAREN cond bloque condFinal','condicion',7,'p_condicion','lexAndSyn.py',272),
  ('condicion -> IF LPAREN expresion RPAREN cond bloque ELSE condElse bloque condFinal','condicion',10,'p_condicion','lexAndSyn.py',273),
  ('cond -> <empty>','cond',0,'p_quad_cond','lexAndSyn.py',277),
  ('condElse -> <empty>','condElse',0,'p_quad_condElse','lexAndSyn.py',281),
  ('condFinal -> <empty>','condFinal',0,'p_quad_condFinal','lexAndSyn.py',285),
  ('escritura -> PRINT push_poper LPAREN exp RPAREN quad_print SEMICOLON','escritura',7,'p_escritura','lexAndSyn.py',289),
  ('quad_print -> <empty>','quad_print',0,'p_quad_print','lexAndSyn.py',293),
  ('escrituraAux -> expresion','escrituraAux',1,'p_escrituraAux','lexAndSyn.py',297),
  ('escrituraAux -> CTE_STRING','escrituraAux',1,'p_escrituraAux','lexAndSyn.py',298),
  ('escrituraAux -> expresion COMA escrituraAux','escrituraAux',3,'p_escrituraAux','lexAndSyn.py',299),
  ('escrituraAux -> CTE_STRING COMA escrituraAux','escrituraAux',3,'p_escrituraAux','lexAndSyn.py',300),
  ('expresion -> exp','expresion',1,'p_expresion','lexAndSyn.py',304),
  ('expresion -> exp comp exp quad_comp','expresion',4,'p_expresion','lexAndSyn.py',305),
  ('comp -> LOWERTHAN push_poper','comp',2,'p_comp','lexAndSyn.py',309),
  ('comp -> MORETHAN push_poper','comp',2,'p_comp','lexAndSyn.py',310),
  ('comp -> DIFFERENT push_poper','comp',2,'p_comp','lexAndSyn.py',311),
  ('comp -> DOUBLEEQUAL push_poper','comp',2,'p_comp','lexAndSyn.py',312),
  ('quad_comp -> <empty>','quad_comp',0,'p_quad_comp','lexAndSyn.py',316),
  ('exp -> termino quad_term','exp',2,'p_exp','lexAndSyn.py',320),
  ('exp -> termino quad_term exp1','exp',3,'p_exp','lexAndSyn.py',321),
  ('exp1 -> PLUS push_poper exp','exp1',3,'p_exp1','lexAndSyn.py',325),
  ('exp1 -> MINUS push_poper exp','exp1',3,'p_exp1','lexAndSyn.py',326),
  ('quad_term -> <empty>','quad_term',0,'p_quad_term','lexAndSyn.py',330),
  ('quad_fact -> <empty>','quad_fact',0,'p_quad_fact','lexAndSyn.py',334),
  ('termino -> factor quad_fact','termino',2,'p_termino','lexAndSyn.py',338),
  ('termino -> factor quad_fact termino1','termino',3,'p_termino','lexAndSyn.py',339),
  ('termino1 -> TIMES push_poper termino','termino1',3,'p_termino1','lexAndSyn.py',343),
  ('termino1 -> DIVIDE push_poper termino','termino1',3,'p_termino1','lexAndSyn.py',344),
  ('factor -> LPAREN expresion RPAREN','factor',3,'p_factor','lexAndSyn.py',348),
  ('factor -> factorAux','factor',1,'p_factor','lexAndSyn.py',349),
  ('factorAux -> PLUS push_poper var_cte','factorAux',3,'p_factorAux','lexAndSyn.py',353),
  ('factorAux -> MINUS push_poper var_cte','factorAux',3,'p_factorAux','lexAndSyn.py',354),
  ('factorAux -> var_cte','factorAux',1,'p_factorAux','lexAndSyn.py',355),
  ('push_id -> <empty>','push_id',0,'p_push_id','lexAndSyn.py',359),
  ('push_cte -> <empty>','push_cte',0,'p_push_cte','lexAndSyn.py',363),
  ('push_poper -> <empty>','push_poper',0,'p_push_poper','lexAndSyn.py',367),
  ('var_cte -> ID push_id','var_cte',2,'p_var_cte','lexAndSyn.py',371),
  ('var_cte -> CTE_I push_cte','var_cte',2,'p_var_cte','lexAndSyn.py',372),
  ('var_cte -> CTE_F push_cte','var_cte',2,'p_var_cte','lexAndSyn.py',373),
  ('var_cte -> CTE_STRING push_cte','var_cte',2,'p_var_cte','lexAndSyn.py',374),
]
