# Generated from Haskell.g4 by ANTLR 4.9.3
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .HaskellParser import HaskellParser
else:
    from HaskellParser import HaskellParser

# This class defines a complete listener for a parse tree produced by HaskellParser.
class HaskellListener(ParseTreeListener):

    # Enter a parse tree produced by HaskellParser#prog.
    def enterProg(self, ctx:HaskellParser.ProgContext):
        pass

    # Exit a parse tree produced by HaskellParser#prog.
    def exitProg(self, ctx:HaskellParser.ProgContext):
        pass


    # Enter a parse tree produced by HaskellParser#decl.
    def enterDecl(self, ctx:HaskellParser.DeclContext):
        pass

    # Exit a parse tree produced by HaskellParser#decl.
    def exitDecl(self, ctx:HaskellParser.DeclContext):
        pass


    # Enter a parse tree produced by HaskellParser#typeDecl.
    def enterTypeDecl(self, ctx:HaskellParser.TypeDeclContext):
        pass

    # Exit a parse tree produced by HaskellParser#typeDecl.
    def exitTypeDecl(self, ctx:HaskellParser.TypeDeclContext):
        pass


    # Enter a parse tree produced by HaskellParser#funcDecl.
    def enterFuncDecl(self, ctx:HaskellParser.FuncDeclContext):
        pass

    # Exit a parse tree produced by HaskellParser#funcDecl.
    def exitFuncDecl(self, ctx:HaskellParser.FuncDeclContext):
        pass


    # Enter a parse tree produced by HaskellParser#funcBody.
    def enterFuncBody(self, ctx:HaskellParser.FuncBodyContext):
        pass

    # Exit a parse tree produced by HaskellParser#funcBody.
    def exitFuncBody(self, ctx:HaskellParser.FuncBodyContext):
        pass


    # Enter a parse tree produced by HaskellParser#typeDeclType.
    def enterTypeDeclType(self, ctx:HaskellParser.TypeDeclTypeContext):
        pass

    # Exit a parse tree produced by HaskellParser#typeDeclType.
    def exitTypeDeclType(self, ctx:HaskellParser.TypeDeclTypeContext):
        pass


    # Enter a parse tree produced by HaskellParser#typeParams.
    def enterTypeParams(self, ctx:HaskellParser.TypeParamsContext):
        pass

    # Exit a parse tree produced by HaskellParser#typeParams.
    def exitTypeParams(self, ctx:HaskellParser.TypeParamsContext):
        pass


    # Enter a parse tree produced by HaskellParser#constructors.
    def enterConstructors(self, ctx:HaskellParser.ConstructorsContext):
        pass

    # Exit a parse tree produced by HaskellParser#constructors.
    def exitConstructors(self, ctx:HaskellParser.ConstructorsContext):
        pass


    # Enter a parse tree produced by HaskellParser#constructor.
    def enterConstructor(self, ctx:HaskellParser.ConstructorContext):
        pass

    # Exit a parse tree produced by HaskellParser#constructor.
    def exitConstructor(self, ctx:HaskellParser.ConstructorContext):
        pass


    # Enter a parse tree produced by HaskellParser#varList.
    def enterVarList(self, ctx:HaskellParser.VarListContext):
        pass

    # Exit a parse tree produced by HaskellParser#varList.
    def exitVarList(self, ctx:HaskellParser.VarListContext):
        pass


    # Enter a parse tree produced by HaskellParser#expr.
    def enterExpr(self, ctx:HaskellParser.ExprContext):
        pass

    # Exit a parse tree produced by HaskellParser#expr.
    def exitExpr(self, ctx:HaskellParser.ExprContext):
        pass


    # Enter a parse tree produced by HaskellParser#funcCall.
    def enterFuncCall(self, ctx:HaskellParser.FuncCallContext):
        pass

    # Exit a parse tree produced by HaskellParser#funcCall.
    def exitFuncCall(self, ctx:HaskellParser.FuncCallContext):
        pass


    # Enter a parse tree produced by HaskellParser#exprList.
    def enterExprList(self, ctx:HaskellParser.ExprListContext):
        pass

    # Exit a parse tree produced by HaskellParser#exprList.
    def exitExprList(self, ctx:HaskellParser.ExprListContext):
        pass


    # Enter a parse tree produced by HaskellParser#binOp.
    def enterBinOp(self, ctx:HaskellParser.BinOpContext):
        pass

    # Exit a parse tree produced by HaskellParser#binOp.
    def exitBinOp(self, ctx:HaskellParser.BinOpContext):
        pass


    # Enter a parse tree produced by HaskellParser#var.
    def enterVar(self, ctx:HaskellParser.VarContext):
        pass

    # Exit a parse tree produced by HaskellParser#var.
    def exitVar(self, ctx:HaskellParser.VarContext):
        pass


    # Enter a parse tree produced by HaskellParser#num.
    def enterNum(self, ctx:HaskellParser.NumContext):
        pass

    # Exit a parse tree produced by HaskellParser#num.
    def exitNum(self, ctx:HaskellParser.NumContext):
        pass


    # Enter a parse tree produced by HaskellParser#haskellType.
    def enterHaskellType(self, ctx:HaskellParser.HaskellTypeContext):
        pass

    # Exit a parse tree produced by HaskellParser#haskellType.
    def exitHaskellType(self, ctx:HaskellParser.HaskellTypeContext):
        pass


    # Enter a parse tree produced by HaskellParser#typeName.
    def enterTypeName(self, ctx:HaskellParser.TypeNameContext):
        pass

    # Exit a parse tree produced by HaskellParser#typeName.
    def exitTypeName(self, ctx:HaskellParser.TypeNameContext):
        pass



del HaskellParser