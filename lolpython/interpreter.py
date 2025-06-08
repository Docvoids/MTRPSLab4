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

    def _visit_LiteralNode(self, node: ast.LiteralNode):
        return node.value

    def _visit_IdentifierNode(self, node: ast.IdentifierNode):
        var_name = node.name
        if var_name not in self.symbol_table:
            raise InterpreterError(f"Undeclared variable '{var_name}'")
        return self.symbol_table.get(var_name)
    
