from antlr4 import *
from antlr4.tree.Trees import Trees
from graphviz import Digraph

from HaskellLexer import HaskellLexer
from HaskellParser import HaskellParser
from HaskellListener import HaskellListener


class ExecutionListener(HaskellListener):
    def __init__(self):
        self.functions = {}

    def enterFuncDecl(self, ctx):
        func_name = ctx.var().getText()
        params = [param.getText() for param in ctx.varList().var()] if ctx.varList() else []
        body = ctx.funcBody() if ctx.funcBody() else ctx.expr()
        self.functions[func_name] = (params, body)

    def visitFuncCall(self, ctx):
        var_context = ctx.var()
        if var_context is not None:
            func_name = var_context.getText()
            if ctx.exprList() is not None:
                args = [int(arg.getText()) for arg in ctx.exprList().expr()]
            else:
                args = []

            if func_name in self.functions:
                result = self.executeFunction(func_name, args)
                print(f"Результат выполнения {func_name}: {result}")
            else:
                print(f"Функция {func_name} не определена.")

    @staticmethod
    def executeFunction(func_name, args):
        if func_name == 'sum' and len(args) == 2:
            return args[0] + args[1]
        else:
            print(f"Функция '{func_name}' не определена или не поддерживается.")
            return None

    def exitProg(self, ctx):
        if "main" in self.functions:
            _, main_body_ctx = self.functions["main"]
            func_call_ctx = self.findFuncCall(main_body_ctx)
            if func_call_ctx:
                self.visitFuncCall(func_call_ctx)
            else:
                print("Не удалось найти вызов функции в main")
        else:
            print("Функция main не найдена.")

    def findFuncCall(self, node):
        if isinstance(node, HaskellParser.FuncCallContext):
            return node
        elif hasattr(node, 'children'):
            for child in node.children:
                result = self.findFuncCall(child)
                if result is not None:
                    return result
        return None


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

    execution_listener = ExecutionListener()
    walker = ParseTreeWalker()
    walker.walk(execution_listener, tree)
    visualize_tree(tree, parser)


if __name__ == '__main__':
    analyze_file('simple.hs')
