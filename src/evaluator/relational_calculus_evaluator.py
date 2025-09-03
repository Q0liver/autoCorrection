from lark import Lark 
from parser.grammar_parser.transformer.relational_calculus_transformer import AstRcTransformer
from deepdiff import DeepDiff
from pprint import pprint

ref="""Q = { (y, x) | ALL a, c, d, e, b (d = 'MAN' AND Bus(b, e, d) AND Einsatzplan(a, b, c, x, y)) }"""
sub="""Q = { (x, y) | ALL a, b, c, d, e (Einsatzplan(x, y, a, b, c) AND Bus(b, d, e) AND d = 'MAN') }"""

parser = Lark.open("src/parser/expression_parser/lark_grammar/relational_calculus.lark")

dif = DeepDiff(AstRcTransformer().transform(parser.parse(sub)), 
               AstRcTransformer().transform(parser.parse(ref)))
print(dif)
print(AstRcTransformer().transform(parser.parse(sub)) == AstRcTransformer().transform(parser.parse(ref)))

#print(parser.parse(sub).pretty())
#pprint(AstRcTransformer().transform(parser.parse(ref)))