## BNF Grammar

### Program Structure
```
<prog> ::= <decl>*
```

### Declarations
```
<decl> ::= <typeDecl> | <funcDecl>
```

#### Type Declarations
```
<typeDecl> ::= 'data' <typeName> [<typeParams>] '=' <constructors>
```

#### Function Declarations
```
<funcDecl> ::= <var> '::' <typeDeclType>
             | <var> [<varList>] '=' <funcBody>
```

### Function Body
```
<funcBody> ::= <expr>
             | <var> [<varList>] '=' <expr>
```

### Type Declaration Type
```
<typeDeclType> ::= <haskellType> ['->' <haskellType>]*
```

### Type Parameters
```
<typeParams> ::= <var> [<var>]*
```

### Constructors
```
<constructors> ::= <constructor> ['|' <constructor>]*
```

#### Constructor Definition
```
<constructor> ::= <typeName> [<typeParams>]
```

### Variable List
```
<varList> ::= <var> [<var>]*
```

### Expressions
```
<expr> ::= <var>
         | <num>
         | <expr> <binOp> <expr>
         | <funcCall>
         | <var> '=' <expr>
```

#### Function Call
```
<funcCall> ::= <var> [<exprList>]
```

#### Expression List
```
<exprList> ::= <expr> [<expr>]*
```

#### Binary Operators
```
<binOp> ::= '+' | '-' | '*' | '/'
```

### Variables, Numbers, and Types
```
<var> ::= <VAR>
<num> ::= <NUM>
<haskellType> ::= 'Int' | 'Bool' | <typeName> | '[' <haskellType> ']' | '(' <haskellType> ',' <haskellType> ')' | <haskellType> '->' <haskellType>
<typeName> ::= <TYPENAME>
```

### Token Definitions
```
<VAR> ::= [a-z][a-zA-Z0-9_]*
<NUM> ::= [0-9]+
<TYPENAME> ::= [A-Z][a-zA-Z0-9_]*
```

### Whitespace (Ignored)
```
<WS> ::= [ \t\r\n]+ -> skip
```