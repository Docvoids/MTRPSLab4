from dataclasses import dataclass
from typing import Any, List, Optional

# Базові вузли
@dataclass
class ASTNode:
    pass

@dataclass
class ExpressionNode(ASTNode):
    pass

# Літерали та ідентифікатори
@dataclass
class LiteralNode(ExpressionNode):
    value: Any

@dataclass
class IdentifierNode(ExpressionNode):
    name: str

# Операції
@dataclass
class BinaryOpNode(ExpressionNode):
    left: ExpressionNode
    op: str
    right: ExpressionNode

# Інструкції (Statements)
@dataclass
class StatementNode(ASTNode):
    pass

@dataclass
class ProgramNode(ASTNode):
    statements: List[StatementNode]

@dataclass
class VarDeclNode(StatementNode):
    name: str
    initializer: Optional[ExpressionNode]

@dataclass
class AssignmentNode(StatementNode):
    identifier: IdentifierNode
    expression: ExpressionNode

@dataclass
class VisibleNode(StatementNode):
    expressions: List[ExpressionNode]
