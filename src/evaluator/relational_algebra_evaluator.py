from lark import Lark 
from parser.grammar_parser.transformer.relatinal_algebra_transformer import AstRaTransformer
from deepdiff import DeepDiff

sub=""" RENAME auto->fahrer (a DIFFERENCE c JOIN b)"""
ref=""" RENAME auto->fahrer (a DIFFERENCE c JOIN b)"""

parser = Lark.open("src/parser/grammar_parser/lark_grammar/relational_algebra.lark")

def relational_algebra_evaluator(ref, sub):
    """This function checks relaional algebra definitons on equality.

    Args:
        ref (str): reference expression
        sub (str): submission expression

    Returns:
        Boolean: When False, the source of error is added.
    """
    diff = DeepDiff(AstRaTransformer().transform(parser.parse(ref)), 
                AstRaTransformer().transform(parser.parse(sub)))
    if not diff:
        return True
    else:
        return False, diff

# for testing purposes
#print(relational_algebra_evaluator(ref, sub))
