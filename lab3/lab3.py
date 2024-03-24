from antlr4 import *
from antlr4.tree.Trees import Trees
from graphviz import Digraph

from HaskellLexer import HaskellLexer
from HaskellParser import HaskellParser
from HaskellListener import HaskellListener


class SemanticAnalyzer(HaskellListener):
    def __init__(self):
        self.types = {"Int": "Int", "Maybe": "GenericType"}
        self.functionSignatures = {}
        self.errors = []

    def enterTypeDecl(self, ctx):
        # Регистрация пользовательских типов данных
        type_name = ctx.typeName().getText()
        self.types[type_name] = "GenericType"

    def enterFuncDecl(self, ctx):
        func_name = ctx.var().getText()
        # Для упрощения предполагаем, что возвращается всегда Int
        self.functionSignatures[func_name] = "Int"
        # Для упрощения предполагаем, что аргументы функций всегда Int
        if ctx.varList():  # Проверка списка переменных
            for var in ctx.varList().var():
                self.types[var.getText()] = "Int"

    def exitExpr(self, ctx):
        # Проверка типов
        if ctx.binOp():
            left = ctx.expr(0).getText()
            right = ctx.expr(1).getText()
            left_type = self.types.get(left, None)
            right_type = self.types.get(right, None)
            if left_type != "Int" or right_type != "Int":
                self.errors.append(f"Type error in expression: {ctx.getText()}")

    def exitProg(self, ctx):
        if self.errors:
            for error in self.errors:
                print(error)
        else:
            print("No errors found.")


def visualize_tree(tree, parser):
    dot = Digraph(comment='The Parse Tree')

    def __add_nodes_edges(t, dot, parent=None):
        if not isinstance(t, TerminalNode):
            node_name = Trees.getNodeText(t, parser.ruleNames)
            dot.node(str(id(t)), node_name)
            if parent is not None:
                dot.edge(str(id(parent)), str(id(t)))
            for child in t.children:
                __add_nodes_edges(child, dot, t)
        else:
            node_name = t.getText()
            dot.node(str(id(t)), node_name)
            if parent is not None:
                dot.edge(str(id(parent)), str(id(t)))

    __add_nodes_edges(tree, dot)
    dot.render('output/parse_tree.gv', view=True)


def analyze_file(file_path):
    input_stream = FileStream(file_path, encoding='utf-8')
    lexer = HaskellLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = HaskellParser(stream)
    tree = parser.prog()

    semantic_analyzer = SemanticAnalyzer()
    walker = ParseTreeWalker()
    walker.walk(semantic_analyzer, tree)
    visualize_tree(tree, parser)


if __name__ == '__main__':
    analyze_file('example.hs')
