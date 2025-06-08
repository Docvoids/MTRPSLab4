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

    def _visit_ProgramNode(self, node: ast.ProgramNode):
        for statement in node.statements:
            self.interpret(statement)

    def _visit_VarDeclNode(self, node: ast.VarDeclNode):
        if node.name in self.symbol_table:
            raise InterpreterError(f"Variable '{node.name}' already declared.")
        value = None
        if node.initializer:
            value = self.interpret(node.initializer)
        self.symbol_table[node.name] = value

    def _visit_VisibleNode(self, node: ast.VisibleNode):
        outputs = [str(self.interpret(expr)) for expr in node.expressions]
        print(" ".join(outputs))
        
    def _visit_AssignmentNode(self, node: ast.AssignmentNode):
        var_name = node.identifier.name
        if var_name not in self.symbol_table:
            raise InterpreterError(f"Undeclared variable '{var_name}'")
        self.symbol_table[var_name] = self.interpret(node.expression)
    
    def _visit_LiteralNode(self, node: ast.LiteralNode):
        return node.value

    def _visit_IdentifierNode(self, node: ast.IdentifierNode):
        var_name = node.name
        if var_name not in self.symbol_table:
            raise InterpreterError(f"Undeclared variable '{var_name}'")
        return self.symbol_table.get(var_name)
