from . import ast_nodes as ast
from .errors import ParserError

class Parser:
    def __init__(self, tokens: list):
        self.tokens = tokens
        self.pos = 0

    def _current(self):
        return self.tokens[self.pos]

    def _advance(self):
        self.pos += 1
        return self.tokens[self.pos - 1]

    def _eat(self, token_type):
        token = self._current()
        if token.type == token_type:
            self._advance()
            return token
        raise ParserError(f"Expected token {token_type} but got {token.type} at line {token.line}")

    def parse(self) -> ast.ProgramNode:
        self._eat('HAI')
        statements = self._parse_statement_list()
        self._eat('KTHXBYE')
        self._eat('EOF')
        return ast.ProgramNode(statements=statements)

    def _parse_statement_list(self):
        statements = []
        while self._current().type not in ('KTHXBYE', 'EOF'):
            statements.append(self._parse_statement())
        return statements

    def _parse_statement(self):
        token_type = self._current().type
        if token_type == 'I_HAS_A':
            return self._parse_var_decl()
        if token_type == 'VISIBLE':
            return self._parse_visible()
        # Assignment will be added later
        raise ParserError(f"Unexpected statement start with token {self._current()} at line {self._current().line}")

    def _parse_var_decl(self):
        self._eat('I_HAS_A')
        name = self._eat('IDENTIFIER').value
        initializer = None
        if self._current().type == 'ITZ':
            self._eat('ITZ')
            initializer = self._parse_expression()
        return ast.VarDeclNode(name=name, initializer=initializer)

    def _parse_visible(self):
        self._eat('VISIBLE')
        expressions = [self._parse_expression()]
        while self._current().type not in ('KTHXBYE', 'EOF', 'I_HAS_A', 'VISIBLE', 'IDENTIFIER'):
            expressions.append(self._parse_expression())
        return ast.VisibleNode(expressions=expressions)

    def _parse_expression(self):
        token = self._current()
        # Binary ops will be added later
        if token.type in ('NUMBR', 'YARN', 'TROOF'):
            return self._parse_literal()
        elif token.type == 'IDENTIFIER':
            return ast.IdentifierNode(name=self._advance().value)
        raise ParserError(f"Unexpected token in expression: {token} at line {token.line}")

    def _parse_literal(self):
        token = self._advance()
        if token.type == 'NUMBR':
            return ast.LiteralNode(value=float(token.value))
        if token.type == 'YARN':
            return ast.LiteralNode(value=token.value[1:-1])
        if token.type == 'TROOF':
            return ast.LiteralNode(value=True if token.value == 'WIN' else False)
        raise ParserError(f"Invalid literal token: {token}")
