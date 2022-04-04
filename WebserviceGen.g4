grammar WebserviceGen;

// Parser

programa : servico+ EOF ;

servico : 'servico' IDENT '{' (linhaatributo (',' linhaatributo)*)? '}' ;

linhaatributo: TIPO_ATR ':' IDENT ':' TIPO_VAR ;

// Lexer

TIPO_ATR: ('in' | 'out');

TIPO_VAR: ('str' | 'float' | 'int');

IDENT: ('a'..'z'|'A'..'Z') ('a'..'z'|'A'..'Z'|'0'..'9')*;

WS:	( ' ' |'\t' | '\r' | '\n') -> skip ;