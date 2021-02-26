
from visitor import *
from expr import *
from token import *
from token_type import *

class AstPrinter(Visitor):
    def __init__(self):
        pass

    def print(self, expr) -> str:
        return expr.accept(self)

    def visit_binary_expr(self, expr: BinaryExpr) -> str:
        return self.parenthesize(expr.operator.lexeme ,expr.left, expr.right)
    
    def visit_unary_expr(self, expr: UnaryExpr) -> str:
        return self.parenthesize(expr.operator.lexeme, expr.right)

    def visit_literal_expr(self, expr: LiteralExpr) -> str:
        if expr.value is None:
            return "nil"
        return str(expr.value)

    def visit_grouping_expr(self, expr: GroupingExpr) -> str:
        return self.parenthesize("group", expr.expression)
    
    def parenthesize(self, name: str, *exprs) -> str:
        builder = f"({name}"
        for expr in exprs:
            builder += f" {expr.accept(self)}"
        builder += ")"
        return builder


