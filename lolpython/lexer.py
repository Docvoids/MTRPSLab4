import re
from collections import namedtuple
from .errors import LexerError

Token = namedtuple('Token', ['type', 'value', 'line', 'column'])

class Lexer:
    def __init__(self, code: str):
        self.code = code
        self.line = 1
        self.column = 1
        self.pos = 0

    def _get_token(self, token_specs):
        # Logic will be here
        return None

    def tokenize(self) -> list[Token]:
        # Logic will be here
        tokens = []
        return tokens
