from antlr4 import *
from antlr4.tree.Trees import Trees
from graphviz import Digraph

from HaskellLexer import HaskellLexer
from HaskellParser import HaskellParser
from HaskellListener import HaskellListener


# Функция для анализа файла
def analyze_file(file_path):
    input_stream = FileStream(file_path, encoding='utf-8')
    lexer = HaskellLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = HaskellParser(stream)
    tree = parser.prog()

    # Визуализация дерева разбора
    visualize_tree(tree, parser)


def visualize_tree(tree, parser):
    dot = Digraph(comment='The Parse Tree')

    def add_nodes_edges(t, dot, parent=None):
        if not isinstance(t, TerminalNode):
            node_name = Trees.getNodeText(t, parser.ruleNames)
            dot.node(str(id(t)), node_name)
            if parent is not None:
                dot.edge(str(id(parent)), str(id(t)))
            for child in t.children:
                add_nodes_edges(child, dot, t)
        else:
            node_name = t.getText()
            dot.node(str(id(t)), node_name)
            if parent is not None:
                dot.edge(str(id(parent)), str(id(t)))

    add_nodes_edges(tree, dot)
    dot.render('output/parse_tree.gv', view=True)  # Сохраняет и отображает график


if __name__ == '__main__':
    analyze_file('example.hs')
