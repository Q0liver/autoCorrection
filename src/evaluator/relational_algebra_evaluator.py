from lark import Lark 
from parser.grammar_parser.transformer.relatinal_algebra_transformer import AstRaTransformer
from deepdiff import DeepDiff

sub=""" RENAME auto->fahrer (a DIFFERENCE c JOIN b)"""
ref=""" RENAME fahrer<-auto (b JOIN c DIFFERENCE a)"""

parser = Lark.open("src/parser/grammar_parser/lark_grammar/relational_algebra.lark")

dif = DeepDiff(AstRaTransformer().transform(parser.parse(sub)), 
               AstRaTransformer().transform(parser.parse(ref)))
print(dif)
print(AstRaTransformer().transform(parser.parse(sub)) == AstRaTransformer().transform(parser.parse(ref)))
#print(parser.parse(sub).pretty())
#print(AstRaTransformer().transform(parser.parse(sub)))
#print(parser.parse(ref).pretty())
