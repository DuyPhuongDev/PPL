// 2212703
grammar MT22;

@lexer::header {
from lexererr import *
}

options{
	language=Python3;
}

program: decllist EOF ;

// rule of systax
decllist: decl decllist | decl;
decl: vardecl | funcdecl;

// variables
vardecl: idlist COLON typ SEMI_COLON | IDENTIFIERS listvar expr SEMI_COLON;
listvar: COMMA IDENTIFIERS listvar expr COMMA | COLON typ ASSIGN;

// function declcare
funcdecl: IDENTIFIERS COLON FUNCTION returntype paradecl (INHERIT IDENTIFIERS)? blockstmt;


// parameters
paradecl: LROUNDBR paramlist RROUNDBR;
paramlist: paramprime | ;
paramprime: param COMMA paramprime | param;
param: INHERIT? OUT? IDENTIFIERS COLON typ;

// array list
arraylit: LBRACES exprlist RBRACES;

// type
idlist: IDENTIFIERS COMMA idlist | IDENTIFIERS;
typ: atomtype | arraytype | AUTO;
atomtype: BOOLEAN | INTEGER | FLOAT | STRING;
arraytype: ARRAY LSQUAREBR dimensions RSQUAREBR OF atomtype;
dimensions: INTLIT COMMA dimensions | INTLIT;
returntype: VOID | atomtype | arraytype | AUTO;

// statements
//blockstmt: LBRACES stmtlist RBRACES;
//stmtlist: stmt stmtlist| ;
//stmt: matchstmt | unmatchstmt | vardecl;

blockstmt: LBRACES (body | ) RBRACES;
body: bodyprime body | bodyprime;
bodyprime: stmt | vardecl;
stmt: matchstmt | unmatchstmt;

matchstmt: matchifstmt | assignstmt | forstmt | whilestmt | dowhilestmt | breakstmt | contstmt | returnstmt | callstmt | blockstmt;
matchifstmt: IF LROUNDBR expr RROUNDBR matchstmt ELSE matchstmt;
unmatchstmt: IF LROUNDBR expr RROUNDBR stmt 
			| IF LROUNDBR expr RROUNDBR matchstmt ELSE unmatchstmt;

assignstmt: scalavar ASSIGN expr SEMI_COLON;
forstmt: FOR LROUNDBR scaladecl COMMA conditionexpr COMMA updateExpr RROUNDBR stmt;
scaladecl: scalavar ASSIGN expr;
conditionexpr: expr;
updateExpr: expr;
whilestmt: WHILE LROUNDBR expr RROUNDBR stmt;
dowhilestmt: DO blockstmt WHILE LROUNDBR expr RROUNDBR SEMI_COLON;
breakstmt: BREAK SEMI_COLON;
contstmt: CONTINUE SEMI_COLON;
returnstmt: RETURN (expr | ) SEMI_COLON;
callstmt: IDENTIFIERS LROUNDBR exprlist RROUNDBR SEMI_COLON; // use in statements


// expression
idxop: IDENTIFIERS LSQUAREBR exprprime RSQUAREBR;

exprlist: exprprime | ;
exprprime: expr COMMA exprprime | expr;
expr: expr1 DBCOLON expr1 | expr1;
expr1: expr2 (EQUAL | NOTEQUAL | LESSEQUAL | LESS | GREATER | GREATEREQUAL) expr2 | expr2;
expr2: expr2 (AND | OR) expr3 | expr3;
expr3: expr3 ( PLUS | MINUS) expr4 | expr4;
expr4: expr4 (MUL | DIV | MOD) expr5 | expr5;
expr5: NOT expr5 | expr6;
expr6: MINUS expr6 | expr7;
expr7: IDENTIFIERS LSQUAREBR exprprime RSQUAREBR | expr8;
expr8: INTLIT | FLOATLIT | STRINGLIT | BOOLEANLIT | IDENTIFIERS | callexpr | subexpr | arraylit;
callexpr: IDENTIFIERS LROUNDBR exprlist RROUNDBR;
subexpr: LROUNDBR expr RROUNDBR;

scalavar: IDENTIFIERS | idxop;




// lexer

// keywords
AUTO: 'auto';
INTEGER: 'integer';
VOID: 'void';
ARRAY: 'array';
BREAK: 'break';
FLOAT: 'float';
RETURN: 'return';
OUT: 'out';
BOOLEAN: 'boolean';
FOR: 'for';
STRING: 'string';
CONTINUE: 'continue';
DO: 'do';
FUNCTION: 'function';
OF: 'of';
ELSE: 'else';
IF: 'if';
WHILE: 'while';
INHERIT: 'inherit';

// operators
PLUS: [+];
MINUS: [-];
MUL: [*];
DIV: [/];
MOD: [%];
NOT: [!];
AND: '&&';
OR: '||';
EQUAL: '==';
NOTEQUAL: '!=';
LESS: '<';
LESSEQUAL: '<=';
GREATER: '>';
GREATEREQUAL: '>=';
DBCOLON: '::';

// seperators
LROUNDBR: '(';
RROUNDBR: ')';
LSQUAREBR: '[';
RSQUAREBR: ']';
DOT: '.';
COMMA: ',';
SEMI_COLON: ';';
COLON: ':';
LBRACES: '{';
RBRACES: '}';
ASSIGN: '=';

//comment
CPP_CMT: '//' ~[\n\r]* -> skip;
C_CMT: '/*' .*? '*/' -> skip;

BOOLEANLIT: TRUE | FALSE;
TRUE: 'true';
FALSE: 'false';

// identifiers
IDENTIFIERS: [A-Za-z_] [A-Za-z0-9_]*;

// literals
INTLIT: POSITIVE {self.text = self.text.replace("_","")};
FLOATLIT: POSITIVE DECIMAl EXPONENT? {self.text = self.text.replace("_","")}
			| (POSITIVE | DECIMAl) EXPONENT {self.text = self.text.replace("_","")};
fragment POSITIVE: '0' | [1-9] [0-9]* ('_'[0-9]+)* ;
fragment DECIMAl: DOT [0-9]+;
fragment EXPONENT: [eE] [+-]? [0-9]+;

STRINGLIT: '"' STR_CHAR* '"' {self.text = self.text[1:-1]};
fragment STR_CHAR: ESC_SEQ | '\\"' | ~([\n\r] | '"') ;
fragment ESC_SEQ: '\\' [bfrnt'\\];




WS : [ \t\r\n\b\f]+ -> skip ; // skip spaces, tabs, newlines, return, form feed, backspace

UNCLOSE_STRING: '"' STR_CHAR* {raise UncloseString(self.text[1:])};

ILLEGAL_ESCAPE:  '"' STR_CHAR* ILLESC
			{
				raise IllegalEscape(self.text[1:]);
			};
fragment ILLESC: '\\' ~( 'b' | 'f' | 'r' | 'n' | 't' | '\'' | '\\' );

ERROR_CHAR: . {raise ErrorToken(self.text)};