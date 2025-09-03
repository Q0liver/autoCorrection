from lark import Lark 
from parser.grammar_parser.transformer.relational_calculus_transformer import AstRcTransformer
from deepdiff import DeepDiff
from pprint import pprint

ref="""Q = { (y, x) | ALL a, c, d, e, b (d = 'MAN' AND Bus(b, e, d) AND Einsatzplan(a, b, c, x, y)) }"""
sub="""Q = { (y, x) | ALL a, c, d, e, b (d = 'MAN' AND Bus(b, e, d) AND Einsatzplan(a, b, c, x, y)) }"""

parser = Lark.open("src/parser/grammar_parser/lark_grammar/relational_calculus.lark")

def relational_calculus_evaluator(ref, sub):
    """This function checks relaional calculus definitons on equality.

    Args:
        ref (str): reference expression
        sub (str): submission expression

    Returns:
        Boolean: When False, the source of error is added.
    """    
    diff = DeepDiff(AstRcTransformer().transform(parser.parse(sub)), 
                   AstRcTransformer().transform(parser.parse(ref)))
    if not diff:
        return True
    else:
        return False, diff

# for testing purposes
print(relational_calculus_evaluator(ref,sub))