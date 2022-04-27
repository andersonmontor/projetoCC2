grammar WebserviceGen;

// Parser

programa : servico+ EOF ;

servico : 'servico' IDENT ('[' TIPO_HTTP ']')? '{' (linhaatributo (',' linhaatributo)*)? '}' ;

linhaatributo: TIPO_ATR ('[' TIPO_ATR_IN ']')? ':' IDENT ':' TIPO_VAR ;

// Lexer

TIPO_ATR: ('in' | 'out');

TIPO_VAR: ('str' | 'float' | 'int');

TIPO_HTTP: ('get' | 'put' | 'post' | 'delete');

TIPO_ATR_IN : ('query' | 'path');

IDENT: ('a'..'z'|'A'..'Z') ('a'..'z'|'A'..'Z'|'0'..'9')*;

WS:	( ' ' |'\t' | '\r' | '\n') -> skip ;