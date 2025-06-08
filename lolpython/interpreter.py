from . import ast_nodes as ast
from .errors import InterpreterError

class Interpreter:
    def init(self):
        self.symbol_table = {}

    def interpret(self, node: ast.ASTNode):
        method_name = f'_visit_{type(node).name}'
        visitor = getattr(self, method_name, self._generic_visit)
        return visitor(node)

    def _generic_visit(self, node):
        raise InterpreterError(f"No _visit_{type(node).name} method")
