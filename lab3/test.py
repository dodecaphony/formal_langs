import re
from antlr4 import *

# Импортируйте сгенерированные классы
from HaskellLexer import HaskellLexer
from HaskellParser import HaskellParser
from HaskellListener import HaskellListener

class SemanticAnalyzer(HaskellListener):
    def __init__(self):
        self.functions = {}

    # Переопределите методы для обработки интересующих узлов AST
    def enterFuncDecl(self, ctx):
        # Допустим, funcName и args - это псевдокод для доступа к имени функции и аргументам
        funcName = ctx.funcName().getText()
        args = [arg.getText() for arg in ctx.args()]
        body = ctx.body().getText()  # Тело функции
        self.functions[funcName] = (args, body)

    def enterMainDecl(self, ctx):
        # Псевдокод для обработки объявления main
        body = ctx.body().getText()
        self.executeFunction('main', body)

    def executeFunction(self, name, body):
        if name in self.functions:
            args, funcBody = self.functions[name]
            # Простая логика исполнения для демонстрации
            print(f'Executing {name} with body: {funcBody}')
        else:
            print(f'Function {name} not defined.')

def analyze_code(code):
    input_stream = InputStream(code)
    lexer = HaskellLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = HaskellParser(stream)
    tree = parser.prog()

    semantic_analyzer = SemanticAnalyzer()
    walker = ParseTreeWalker()
    walker.walk(semantic_analyzer, tree)

# Пример Haskell кода для анализа
code = """
sum x y = x + y
main = sum 5 3
"""

analyze_code(code)
