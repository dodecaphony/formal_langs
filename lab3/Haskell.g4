grammar Haskell;

prog: decl* ;

decl: typeDecl | funcDecl ;

typeDecl: 'data' typeName typeParams? '=' constructors ;

funcDecl: var '::' typeDeclType
        | var varList? '=' funcBody ;

funcBody: expr
        | var varList '=' expr ;

typeDeclType: haskellType ('->' haskellType)* ;

typeParams: var (var)* ;

constructors: constructor ('|' constructor)* ;

constructor: typeName (typeParams)? ;

varList: var (var)* ;

expr: var
    | num
    | expr binOp expr
    | funcCall
    | var '=' expr ;

funcCall: var exprList? ;

exprList: expr (expr)* ;

binOp: '+' | '-' | '*' | '/' ;

var: VAR ;

num: NUM ;

haskellType: 'Int' | 'Bool' | typeName | '[' haskellType ']' | '(' haskellType ',' haskellType ')' | haskellType '->' haskellType ;

typeName: TYPENAME ;

VAR: [a-z][a-zA-Z0-9_]* ;

NUM: [0-9]+ ;

TYPENAME: [A-Z][a-zA-Z0-9_]* ;

WS: [ \t\r\n]+ -> skip ;
