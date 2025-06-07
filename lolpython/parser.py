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
        # statements = self._parse_statement_list() # To be implemented
        statements = []
        self._eat('KTHXBYE')
        self._eat('EOF')
        return ast.ProgramNode(statements=statements)
